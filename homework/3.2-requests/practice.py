import requests
import os
import chardet

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()                                                           # Clear console screen.  
    
files_list = os.listdir('.\\')
print ('Список файлов:', files_list)
file_input = input('Введите имя файла для перевода:')
path_file1 = os.path.join('.\\',file_input)
print('Путь к файлу: ',path_file1)
if os.path.isfile(path_file1) == True:    
    with open(path_file1, 'rb') as f:                       # Get literal encode.  
        text_string = f.read()
        result = chardet.detect(text_string)        
        text_enc = result['encoding']        
        with open(path_file1, encoding = text_enc) as file1: # Search the words in the file list.  
            read_file1 = file1.read() 
else:
    print('Ошибка ввода имени файла!')
print('Текст для перевода:', read_file1)

def translate_it(read_file1):
    """
    YANDEX translation plugin
    docs: https://tech.yandex.ru/translate/doc/dg/reference/translate-docpage/

    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
    & text=<переводимый текст>
    & lang=<направление перевода>
    & [format=<формат текста>]
    & [options=<опции перевода>]
    & [callback=<имя callback-функции>]
    :param text: <str> text for translation.
    :return: <str> translated text.
    """
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    key = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'
    lang_input = ('Введите направление перевода, например, с русского на английский: ru-en')
    params = {'key': key,'lang': lang_input,'text': read_file1,}
    response = requests.get(url, params=params).json()
    print('Ответ YANDEX API:  ',response )    
    file_input2 = input('Введите имя файла для вывода:')
    path_file2 = os.path.join('.\\',file_input2)
    if os.path.isfile(path_file2) == False:
        with open(path_file2, 'w') as f2: 
            f2.write(str(response))
    return ' '.join(response.get('text', []))
a = translate_it(read_file1)
print(a)
