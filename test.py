import requests

# документация https://yandex.ru/dev/translate/doc/dg/reference/translate-docpage/

API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'


def translate_it(from_lang1, from_lang2, from_lang3, to_lang1='ru', to_lang2='ru', to_lang3='ru'):
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
    enter1 = '/home/mishanya/Python/дз/HW11/ES.txt'
    enter2 = '/home/mishanya/Python/дз/HW11/DE.txt'
    enter3 = '/home/mishanya/Python/дз/HW11/FR.txt'

    with open(enter1) as f_enter1:
        text_read1 = []
        for i in f_enter1:
            text_read1.append(i)

    with open(enter2) as f_enter2:
        text_read2 = []
        for i in f_enter2:
            text_read2.append(i)

    with open(enter3) as f_enter3:
        text_read3 = []
        for i in f_enter3:
            text_read3.append(i)

    langs1 = f'{from_lang1}-{to_lang1}'
    langs2 = f'{from_lang2}-{to_lang2}'
    langs3 = f'{from_lang3}-{to_lang3}'

    text_read2 = 'Starke 45 Minuten waren genug'

    params = {
        'key': API_KEY,
        'text': [text_read1, text_read2, text_read3],
        'lang': [langs1, langs2, langs3],
    }

    response = requests.post(URL, params=params)
    json_ = response.json()

    out = '/home/mishanya/Python/test2.txt'
    with open(out, 'w') as f_out:
        f_out.write(''.join(json_['text']))

    return ''.join(json_['text'])


if __name__ == '__main__':
    print(translate_it('es', 'de', 'fr',))