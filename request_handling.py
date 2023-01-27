import requests
import json


def to_dict(response):
    data = {}
    for idx, story in enumerate(response):
        data[idx] = story
    return data
