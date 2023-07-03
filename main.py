import os
import sys
import shutil
directory = sys.argv[1]

def translate(name):
    CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
    TRANSLATION = (
        "a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
        "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")
    TRANS = {}
    for symbol in range(len(CYRILLIC_SYMBOLS)):
        TRANS.update({ord(CYRILLIC_SYMBOLS[symbol]): TRANSLATION[symbol]})
        TRANS.update({ord(CYRILLIC_SYMBOLS[symbol].upper()): TRANSLATION[symbol].upper()})
    name = name.translate(TRANS)
    return name

#змінює назви з кирилиці на латиницю
def normalize(path_to_folder) -> None:
    for filename in os.listdir(path_to_folder):
        os.rename(path_to_folder + f'\\{filename}', path_to_folder + f'\\{translate(filename)}')

#видалення пустих папок
def delete_empty_folders(directory):
    ignore_folders = ['archives', 'images','video','documents','audio']
    for root, dirs, files in os.walk(directory, topdown=False):
        for folder in dirs:
            folder_path = os.path.join(root, folder)
            if not os.listdir(folder_path) and not str(folder) in ignore_folders:  # Check if the folder is empty
                os.rmdir(folder_path)

#назва папки у яку має бути переміщений файл
def dst_folder(filename):
    extensions = {"images": ['JPEG', 'PNG', 'JPG', 'SVG'], 'video': ['AVI', 'MP4', 'MOV', 'MKV'],
                  'documents': ['DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX'], 'audio': ['MP3', 'OGG', 'WAV', 'AMR'],
                  'archives': ['ZIP', 'GZ', 'TAR']}
    for key in extensions:
        for value in extensions[key]:
            if filename.upper().endswith('.' + value):
                return key

#Переміщення файлів
def move_folders(directory):
    for item in os.listdir(directory):
        if not os.path.isdir(directory+f'\\{item}'):
            src = directory+f'\\{item}'
            #print(src)
            if dst_folder(item) is not None:
                dst = 'D:\lessons\GoIT_Python\Мотлох'+f'\\{dst_folder(item)}'
                #print(dst)
                #розпакування архівів
                if item.endswith(('.zip', '.gz', '.tar')):
                    #print(item)
                    shutil.unpack_archive(src, f'{directory}\\archives')
                    os.remove(src)
                else:
                    shutil.move(src,dst)
        if os.path.isdir(directory+f'\\{item}') and item!='video':
            move_folders(directory+f'\\{item}')

#головна функція для сортування файлів
def sorting(directory):
    normalize(directory)
    # створення потрібних папок
    ignore_folders = ['archives', 'images', 'video', 'documents', 'audio']
    for folder in ignore_folders:
        if not os.path.exists((os.path.join(directory, folder))):
            os.mkdir(os.path.join(directory, folder))

    #сортування файлів по відповідним папкам
    move_folders(directory)
    #видалення усіх пустих папок, що залишились
    delete_empty_folders(directory)

sorting(directory)