import time
import csv
import inspect
import os
import sys
from datetime import datetime
from typing import Dict, List, Tuple
from setup import outsider


class Lil_error(Exception):
    pass


csv_files = list()
csv_files_folder = str()
headers = ["begin", "end", "time interval", "login", "mac ab", "ULSK1",
           "BRAS ip", "start count", "alive count", "stop count",
           "incoming", "outcoming", "error_count", "code 0", "code 1011",
           "code 1100", "code -3", "code -52", "code -42", "code -21",
           "code -40", "code -44", "code -46", "code -38"]


def get_script_dir(follow_symlinks=True) -> str:
    '''получить директорию со скриптом'''

    # https://clck.ru/P8NUA
    if getattr(sys, 'frozen', False):  # type: ignore
        path = os.path.abspath(sys.executable)
    else:
        path = inspect.getabsfile(get_script_dir)
    if follow_symlinks:
        path = os.path.realpath(path)
    return os.path.dirname(path)


def list_csv(index=None, all=False) -> List[str]:
    '''вернуть имя csv по индексу или список всех имён csv'''

    if all:
        return csv_files
    else:
        return csv_files[index]


def dir_to(csv_file, write=False) -> str:
    '''путь до file.csv'''

    global csv_files_folder
    if write is True:
        path = os.path.join(get_script_dir(), "get_csv_here")

        return os.path.join(path, csv_file)
    if write is False:
        return os.path.join(get_script_dir(), csv_files_folder, csv_file)


def init_note_list() -> None:
    '''определить список csv'''
    try:
        global csv_files_folder
        global csv_files
        path = os.path.join(get_script_dir(), csv_files_folder)

        files = os.listdir(path)
        for file in files:
            if file[-4:] == ".csv":
                csv_files.append(file)

        if len(csv_files) == 0:
            raise Lil_error("Error: folder does not contain '.csv' files.")

        file_info = dict()
        for csv in csv_files:
            try:
                with open(dir_to(csv), 'r') as f:
                    for _ in range(2):
                        cur_dict = f.readline()
                    first_begin = cur_dict.split(',')[0]
                    file_info.update({csv: first_begin})
            except FileNotFoundError as e:
                raise Lil_error("Error: There is no such file or directory.")
        csv_files = sorted(file_info, key=file_info.get)

        return None
    except Lil_error as e:
        raise Lil_error(str(e))


def csv_reader(file_dir) -> List[Dict[str, str]]:
    '''вернуть содержимое csv файла по его file_dir'''
    try:
        global headers

        with open(file_dir, 'r') as f_check:
            first_row = f_check.readline()
        for key in headers:
            if key not in first_row:
                raise Lil_error("Error: Incorrect headers in csv.")

        with open(file_dir, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            data = list()
            for row in reader:
                data.append(row)
        return data
    except Lil_error as e:
        raise Lil_error(str(e))


def csv_writer(data, file_name) -> None:
    global headers

    try:
        new_file_dir = dir_to(file_name, write=True)
        with open(new_file_dir, 'a', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=headers)
            if os.path.getsize(new_file_dir) == 0:
                writer.writeheader()
            for row in data:
                writer.writerow(row)
        del data
        return None
    except Lil_error as e:
        raise Lil_error(str(e))


def get_csv_when(index=None, login=None, date_range=[None, None]):
    '''вернуть содержимое одного csv по фильтрам'''

    try:
        begin = date_range[0]
        end = date_range[1]

        try:
            csv = csv_reader(dir_to(list_csv(index)))
        except lil_error as e:
            raise lil_error(str(e))

        filtred_csv = list()
        if login is None:
            for iter_dict in csv:
                if iter_dict["begin"] >= begin and \
                        iter_dict["end"] <= end:
                    filtred_csv.append(iter_dict)

        elif login is not None:
            for iter_dict in csv:
                if iter_dict["login"] == login:
                    filtred_csv.append(iter_dict)

            filtred_csv_2 = list()
            for iter_dict in filtred_csv:
                if iter_dict["begin"] >= begin and \
                        iter_dict["end"] <= end:
                    filtred_csv_2.append(iter_dict)
            return filtred_csv_2

        del csv
        return filtred_csv
    except Lil_error as e:
        raise Lil_error(str(e))


def ok_to_unix(ok):
    ''' возвращает <class 'str'> '''
    ok = datetime.strptime(str(ok), "%Y-%m-%d %H:%M:%S")
    return str(int((ok-datetime(1970, 1, 1)).total_seconds()))


def unixtime_to_ok(unixtime):
    ''' возвращает <class 'datetime.datetime'> '''
    return datetime.utcfromtimestamp(int(unixtime))


def check_and_read_csv_single_file(file):
    try:
        path = os.path.join(get_script_dir(), file)
        if not os.access(path, os.F_OK):
            raise Lil_error("Error: file does not exist.")
        if not os.path.isfile(path):
            raise Lil_error("Error: path does not point to file.")
        if not os.access(path, os.R_OK):
            raise Lil_error("Error: access to file is denied.")
        if file[-4:] != ".csv":
            raise Lil_error("Error: Incorrect file extension.")

        try:
            return csv_reader(os.path.join(get_script_dir(), file))
        except lil_error as e:
            raise lil_error(str(e))
    except Lil_error as e:
        raise Lil_error(str(e))


def show_page_from_csv(path_to_file, page_number):

    try:
        csv = check_and_read_csv_single_file(path_to_file)

        page_size = 100
        if len(csv) / 100 > 1:
            if len(csv) % page_size == 0:
                pages_total = len(csv) // page_size
            else:
                pages_total = len(csv) // page_size + 1
        else:
            pages_total = 1

        if page_number < 1:
            raise Lil_error("Error1: Incorrect page number")
        if pages_total == 1 and page_number > 1:
            raise Lil_error("Error2: Incorrect page number")
        if page_number > pages_total:
            raise Lil_error("Error3: Incorrect page number")

        page_begin = page_size * page_number - page_size
        page_end = page_size * page_number

        data = list()
        try:
            for iter_dict in range(page_begin, page_end):
                data.append(csv[iter_dict])
        except IndexError:
            pass

        return (data, pages_total)
    except Lil_error as e:
        raise Lil_error(str(e))


def filter(login=None, date_range=[None, None]) -> None:
    csv_name = gen_new_csv_name()

    maax = len(list_csv(all=True))
    for i in range(maax):
        data = get_csv_when(i, login=login, date_range=date_range)
        csv_writer(data, csv_name)

        outsider(int((i + 1) * (100 / maax)))
        del data
    return None


def gen_new_csv_name():
    path = os.path.join(get_script_dir(), "get_csv_here")
    if not os.path.exists(path):
        os.mkdir(path)
    files = os.listdir(path)
    i = 1
    while f"result{i}.csv" in files:
        i += 1
    return f"result{i}.csv"


def check_csv_files_folder(folder):
    try:
        global csv_files_folder
        path = os.path.join(get_script_dir(), folder)
        if not os.access(path, os.F_OK):
            raise Lil_error("Error: folder does not exist.")
        if not os.path.isdir(path):
            raise Lil_error("Error: path does not point to folder.")
        if not os.access(path, os.R_OK):
            raise Lil_error("Error: access to folder is denied.")
        if len(os.listdir(path)) == 0:
            raise Lil_error("Error: folder is empty.")

        csv_files_folder = folder
    except Lil_error as e:
        raise Lil_error(str(e))
