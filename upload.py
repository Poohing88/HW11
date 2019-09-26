import requests

def load(result):
    token = 'AgAAAAA4Q0F2AADLW_C_PepsWEr_nJHOml9Knh0'
    URL_load = 'https://cloud-api.yandex.net/v1/disk/resources/upload'

    headers = {"accept": "application/json",
               "accept-language": "ru",
               "authorization": "OAuth {}".format(token),
               "content-type": "application/json"}

    param_load = {
        'path': '/answer.txt',
        'overwrite': 'True'
    }
    load = requests.get(URL_load, headers=headers, params=param_load)
    link_load = load.json()['href']
    with open('answer.txt', mode='w', encoding='utf-8') as f:
        f.write(result)
        requests.put(link_load, data=result.encode('utf-8'))




