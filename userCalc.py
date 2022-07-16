from furthrapi import APIv1


def calc(config):
    """
    config contains: projectId, groupId, sampleId, experimentId, rawdataId, callbackUrl, apiKey
    """
    api = APIv1(config)
    api.setResult({"result": "test"})

    print('Hello World!')
