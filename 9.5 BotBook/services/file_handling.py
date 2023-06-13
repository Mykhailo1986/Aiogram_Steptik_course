import os

BOOK_PATH = r'9.5 BotBook\book\book.txt'

PAGE_SIZE = 1050

book: dict[int, str] = {}


# Функция, возвращающая строку с текстом страницы и ее размер
def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:

    end:int = min(start+size,len(text))
    end_syntax_symbols :tulple(int) = ('.' , '!' , ',' , ';' , '?', ':' )

    for i in range (end, start, -1):

        if text[i-1] in end_syntax_symbols :
            end = i
            try:
                if not text[end] in end_syntax_symbols:
                    break
            except: break
    txt=text[start:end]
    # import re
    # txt = re.sub(r'\n(?![A-Z ])', ' ', txt)
    # txt = txt.replace('\n\n', '\n').replace('TAB', ' A')
    return txt, len(txt)


# text = '''The Project Gutenberg eBook of The first French Republic, by Horace
# Mann Conaway

# This eBook is for the use of anyone anywhere in the United States and
# most other parts of the world at no cost and with almost no restrictions
# whatsoever. You may copy it, give it away or re-use it under the terms
# of the Project Gutenberg License included with this eBook or online at
# www.gutenberg.org. If you are not located in the United States, you
# will have to check the laws of the country where you are located before
# using this eBook.

# Title: The first French Republic
#        A study of the origin and the contents of the declaration of the
#        rights of man, of the constitution, and of the adoption of the
#        republican form of government in 1792'''
# # a,b=(_get_part_text(text, 10, 2000))
# # print(repr(a))
# print(*_get_part_text(text, 10, 2000), sep='\n')






# Функция, формирующая словарь книги
def prepare_book(path: str) -> None:\

    i : int = 0
    start : int = 0

    with open(path, 'r', encoding='utf-8') as file:
        contents = file.read()

    while start != len(contents):
        text, step = _get_part_text(contents, start, PAGE_SIZE)
        book[i] = text.lstrip()
        start += step
        i +=  1




# # Вызов функции prepare_book для подготовки книги из текстового файла
prepare_book(os.path.join(os.getcwd(), BOOK_PATH))