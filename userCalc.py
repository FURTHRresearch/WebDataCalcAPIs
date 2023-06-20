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
    field = exp["fielddata"][0]
    print("field_data_id: ", field["id"])
    print("field_id: ", field["fieldid"])            # id of field definition, type name etc
    print("field_name: ", field["fieldname"])

    # getting all groups
    url = f"{base_url}/project/{config['projectId']}/groups"
    response = session.get(url)
    response = response.json()
    status = response["status"]  # ok or error
    message = response["message"]  # if error, error message provide
    group = response["results"][0]  # request results

    print("number of exp: ", len(group["experiments"]))
    print("name and id of first exp: ", group["experiments"][0]["name"],group["experiments"][0]["id"])

if __name__ == "__main__":
    config = {'projectId': '631893e1ca17478734063e5b',
              'groupId': '63189479ca1747873406e77a',
              'sampleId': '63189479ca1747873406e9cc',
              'experimentId': '6318947eca1747873406fbec',
              'rawdataId': '63189534ca174787340985a6',
              # 'callbackUrl': 'https://test.furthrmind.app',
              'callbackUrl': 'http://127.0.0.1:5000',
              'apiKey': 'E8WHB1EQE4S44SK0D04AS4RY2EHQX8OB',
              'fieldId': '636285c0cafe2adcd010fdea'}

    calc(config)
