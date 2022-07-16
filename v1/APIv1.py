# API v1

import requests


class APIv1:
    def __init__(self, config):
        self.target = config['callbackUrl']
        self.key = config['apiKey']
        self.headers = {'Content-Type': 'application/json',
                        'X-API-Key': self.key}

    def getRawData(self, id):
        url = self.target + "/rawdata/" + id
        return requests.get(url, headers=self.headers).json()

    def getSample(self, id):
        url = self.target + "/samples/" + id
        return requests.get(url, headers=self.headers).json()

    def getExperiment(self, id):
        url = self.target + "/experiments/" + id
        return requests.get(url, headers=self.headers).json()

    def getFile(self, id):
        url = self.target + "/files/" + id
        return requests.get(url, headers=self.headers).content

    def setFieldValue(self, targetType, targetId, fieldName, fieldValue, fieldType='Numeric'):
        if targetType != "experiments":
            raise ValueError("targetType not implemented")
        url = self.target + "/api1/" + targetType + "/" + targetId + "/fields"
        data = {
            'fieldName': fieldName,
            'fieldType': fieldType,
            'value': fieldValue
        }
        return requests.post(url, headers=self.headers, json=data).json()
