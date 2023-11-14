import os

from furthrapi import APIv1
from FileLoader import FileLoader
import requests

def calc(config):
    """
    config is d dict and contains: projectId, groupId, sampleId, experimentId, rawdataId, fieldId, callbackUrl, apiKey
    """
    """ Examples using APIv1 """
    api = APIv1(config)
    api.setResult({"result": "test"})

    # get experiment
    exp = api.getExperiment(config["experimentId"])
    # print(exp)

    """ examples using REST-API """
    session = requests.session()
    session.headers.update( {"X-API-KEY": config["apiKey"]})
    base_url = f"{config['callbackUrl']}/api2"

    # four urls to access the content of an experiment. With and without project, singular and plural
    # url = f"{base_url}/projects/{config['projectId']}/experiments/{config['experimentId']}"
    # url = f"{base_url}/project/{config['projectId']}/experiment/{config['experimentId']}"
    # url = f"{base_url}/experiments/{config['experimentId']}"
    url = f"{base_url}/experiment/{config['experimentId']}"
    response = session.get(url)
    response = response.json()
    status = response["status"]         # ok or error
    message = response["message"]       # if error, error message provide
    exp = response["results"][0]          # request results

    print("keys of experiment: ", exp.keys())

    # getting all fields of an experiment
    if exp["fielddata"]:
        field = exp["fielddata"][0]
        print("field_data_id: ", field["id"])
        print("field_id: ", field["fieldid"])            # id of field definition, type name etc
        print("field_name: ", field["fieldname"])

    # downloading a file
    files = exp["files"]
    if files:
        file = files[0]
        file_id = file["id"]
        file_loader = FileLoader(config["callbackUrl"], config["apiKey"])
        folder = os.getcwd()
        file_loader.downloadFile(file_id, folder)
        print("File exists: ", os.path.isfile(f"{folder}/{file['name']}"))

    # getting all groups
    url = f"{base_url}/project/{config['projectId']}/groups"
    response = session.get(url)
    response = response.json()
    status = response["status"]  # ok or error
    message = response["message"]  # if error, error message provide
    group = response["results"][0]  # request results

    print("number of exp: ", len(group["experiments"]))
    if group["experiments"]:
        print("name and id of first exp: ", group["experiments"][0]["name"],group["experiments"][0]["id"])

    # write new calc result
    url = f"{base_url}/set-result/{config['fieldId']}"
    result = {"key": "value",
              "key2": "value2"}
    session.post(url, json=result)



