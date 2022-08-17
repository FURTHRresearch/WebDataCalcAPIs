import requests


class APIv1:
    def __init__(self, config):
        self.config = config
        self.session = requests.session()
        self.session.headers.update({"X-API-Key": config['apiKey']})
        self.target = config['callbackUrl']

    def getRawData(self, id):
        url = self.target + "/rawdata/" + id
        return self.session.get(url).json()

    def getSample(self, id):
        url = self.target + "/samples/" + id
        return self.session.get(url).json()

    def getExperiment(self, id):
        url = self.target + "/experiments/" + id
        return self.session.get(url).json()

    def getFile(self, id):
        url = self.target + "/files/" + id
        return self.session.get(url).content

    def setFieldValue(self, targetType, targetId, fieldName, fieldValue, fieldType='Numeric'):
        if targetType != "experiments":
            raise ValueError("targetType not implemented")
        url = self.target + "/api1/" + targetType + "/" + targetId + "/fields"
        data = {
            'fieldName': fieldName,
            'fieldType': fieldType,
            'value': fieldValue
        }
        return self.session.post(url, json=data).json()

    def setResult(self, result):
        url = self.target + \
            f"/fields/{self.config['fieldId']}/calculationresults"
        return self.session.post(url, json=result)
