import json


def ler_json(arq_json):
    with open(arq_json, 'r', encoding='utf-8-sig') as f:
        return json.load(f)