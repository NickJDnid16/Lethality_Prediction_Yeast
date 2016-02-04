'''
        Copyright 2016 - Keiron O'Shea
'''

import csv


def get_columns(lst, indices):
    new_rows = []
    for row in lst:
        items = []
        for index, item in enumerate(row):
            if index in indices:
                items.append(item)
        new_rows.append(items)
        items = []
    return new_rows


def keep_columns(lst, func, headers=True):
    keep_columns = []
    for row in lst:
        if headers:
            headers = False
            continue
        for index, item in enumerate(row):
            if func(item):
                keep_columns.append(index)
    return set(keep_columns)



if __name__ == "__main__":
    fn = "/home/mintvm/Dropbox/CURRENT/Worm/Worm.csv"

    with open(fn, "r") as csvf:
        rdr = csv.reader(csvf, delimiter=",")

        data = list(rdr)
        keep = keep_columns(data, lambda x: not x == "0")

        for col in get_columns(data, keep):
            print(",".join(col))
            

