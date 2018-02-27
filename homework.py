import requests
import os.path

API_KEY = "trnsl.1.1.20180227T185839Z.03497994de3ce513.9a8649af6781f3d2e82971e8a27344afbd878604"
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'


def translate_it(text, from_lang, to_lang):

     #https://translate.yandex.net/api/v1.5/tr.json/translate ?
    #key=<API-ключ>
     #& text=<переводимый текст>
     #& lang=<направление перевода>
     #& [format=<формат текста>]
     #& [options=<опции перевода>]
     #& [callback=<имя callback-функции>]
    #:param to_lang:
    #:return:


    params = {
        'key': API_KEY,
        'text': text,
        'lang': '{}-{}'.format(from_lang, to_lang),
    }

    response = requests.get(URL, params=params)
    json_ = response.json()
    return ''.join(json_['text'])


def main():
    file = input('Введите имя файла для перевода:')
    with open(file, 'r',) as f:
        text = f.read()
    from_lang = os.path.splitext(file)[0]
    to_lang = input('Введите направление перевода(ru, en, fr, etc):')
    newfile = input('Введите имя файла для перевода:')
    with open(newfile, 'w') as f:
        f.write(translate_it(text, from_lang, to_lang))
    print('Перевод выполнен')

main()