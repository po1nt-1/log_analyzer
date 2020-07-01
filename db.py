import csv
import inspect


def input_filter(dir):
    pass


def get_script_dir(follow_symlinks: bool = True) -> str:
    # https://clck.ru/P8NUA
    if getattr(sys, 'frozen', False):  # type: ignore
        path = os.path.abspath(sys.executable)
    else:
        path = inspect.getabsfile(get_script_dir)
    if follow_symlinks:
        path = os.path.realpath(path)
    return os.path.dirname(path)


def csv_reader(file_dir):
    with open(file_dir, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
    for row in reader:
        print(" ".join(row))
