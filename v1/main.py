import json

from calc import calc

from API import API

experiment = json.load(open('experiment.json'))
config = json.load(open('config.json'))

api = API(config)

calc(experiment, api)
