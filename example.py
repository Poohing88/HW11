import requests
# документация https://yandex.ru/dev/translate/doc/dg/reference/translate-docpage/

API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'


def translate_it(from_file, to_file, from_lang, to_lang='ru'):
    """
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]
    :param to_lang:
    :return:
    """
    enter = from_file
    with open(enter) as f_enter:
        text_read = []
        for i in f_enter:
            text_read.append(i)
    langs = f'{from_lang}-{to_lang}'

    params = {
        'key': API_KEY,
        'text': text_read,
        'lang': langs,
    }

    response = requests.get(URL, params=params)
    json_ = response.json()

    out = to_file
    with open(out, 'w') as f_out:
        f_out.write(''.join(json_['text']))

    return ''.join(json_['text'])


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


if __name__ == '__main__':
    print(translate_it('/home/mishanya/Python/дз/HW11/ES.txt', '/home/mishanya/Python/дз/HW11/answer.txt', 'es'))

translate = translate_it('/home/mishanya/Python/дз/HW11/ES.txt', '/home/mishanya/Python/дз/HW11/answer.txt', 'es')
load(translate)