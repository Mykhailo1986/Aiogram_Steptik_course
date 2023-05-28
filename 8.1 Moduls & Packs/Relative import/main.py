print('Это основной файл relative_import main.py, его имя в процессе выполнения программы:', __name__)


from pack_1.file_11 import result


print('result =', result)