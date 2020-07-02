import csv
import os
import sys
import inspect
from datetime import datetime
import time
from typing import List, Dict

csv_files = list()


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
    if write is True:
        path = os.path.join(get_script_dir(), "filtred_csv")
        if not os.path.exists(path):
            os.mkdir(path)
        return os.path.join(path, csv_file)
    if write is False:
        return os.path.join(get_script_dir(), csv_file)


def init_note_list() -> None:
    '''определить список csv'''

    global csv_files

    files = os.listdir(get_script_dir())
    for file in files:
        if file[-4:] == ".csv":
            csv_files.append(file)

    file_info = dict()
    for csv in csv_files:
        with open(dir_to(csv), 'r') as f:
            for _ in range(2):
                cur_dict = f.readline()
            first_begin = cur_dict.split(',')[0]
            file_info.update({csv: first_begin})
    csv_files = sorted(file_info, key=file_info.get)

    return None


def csv_reader(file_dir) -> List[Dict[str, str]]:
    '''вернуть содержимое csv файла по его file_dir'''

    with open(file_dir, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        data = list()
        for row in reader:
            data.append(row)
    return data


def csv_writer(data) -> None:
    new_file_dir = dir_to("result.csv", write=True)
    headers = ["begin", "end", "time interval", "login", "mac ab", "ULSK1",
               "BRAS ip", "start count", "alive count", "stop count",
               "incoming", "outcoming", "error_count", "code 0", "code 1011",
               "code 1100", "code -3", "code -52", "code -42", "code -21",
               "code -40", "code -44", "code -46", "code -38"]

    with open(new_file_dir, 'a', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=headers)
        if os.path.getsize(new_file_dir) == 0:
            writer.writeheader()
        for row in data:
            writer.writerow(row)

    return None


def get_csv_when(index=None, login=None, date_range=(None, None)):
    '''вернуть содержимое одного csv по фильтрам'''

    begin = date_range[0]
    end = date_range[1]
    csv = csv_reader(dir_to(list_csv(index)))
    filtred_csv = list()
    if (login is not None) and (begin is None or end is None):
        for iter_dict in csv:
            if "login" in iter_dict:
                if iter_dict["login"] == login:
                    filtred_csv.append(iter_dict)

    elif (login is None) and (begin is not None) and (end is not None):
        for iter_dict in csv:
            if "begin" in iter_dict and "end" in iter_dict:
                if iter_dict["begin"] >= begin and \
                        iter_dict["end"] <= end:
                    filtred_csv.append(iter_dict)

    elif (login is not None) and (begin is not None) and (end is not None):
        for iter_dict in csv:
            if "login" in iter_dict:
                if iter_dict["login"] == login:
                    filtred_csv.append(iter_dict)

        filtred_csv_2 = list()
        for iter_dict in filtred_csv:
            if "begin" in iter_dict and "end" in iter_dict:
                if iter_dict["begin"] >= begin and \
                        iter_dict["end"] <= end:
                    filtred_csv_2.append(iter_dict)
        return filtred_csv_2

    del csv

    if len(filtred_csv) == 0:
        return None

    return filtred_csv


def unixtime_to_ok(unixtime):
    ok = datetime.fromtimestamp(unixtime)
    return ok.strftime("%Y-%m-%d %H:%M:%S")


def ok_to_unixtime(ok):
    return str(datetime.strptime(ok, "%Y-%m-%d %H:%M:%S"))


def filter(login=None, date_range=(None, None)) -> None:
    for i in range(len(list_csv(all=True))):
        query_result = get_csv_when(i, login=login, date_range=date_range)
        if query_result is None:
            continue
        csv_writer(query_result)
        del query_result
    return None


if __name__ == "__main__":
    init_note_list()

    filter()
