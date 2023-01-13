  #  Задание 1

def parse_log(pth_file="./nginx_logs.txt"):

    if pth_file:
        with open(pth_file, "r", encoding="utf-8") as file:
            for line in file:
                ip = line.split(" - - ")[0]
                rsp_and_pth = line.split('"')[1]
                rsp = rsp_and_pth.split()[0]
                pth = rsp_and_pth.split()[1]
                yield(ip, rsp, pth)


#  Задание  2

def find_spamer(pth_file="./nginx_logs.txt"):

    if not pth_file:
        return None

    parsed = parse_log(pth_file)

    db = {}

    for log in parsed:

        db[log[0]] = db.get(log[0], 0) + 1

    return max(db.items(), key=lambda x: x[1])


if __name__ == "__main__":
    parsed = parse_log()

    print(type(parsed))

    for _ in range(5):
        print(next(parsed))

    spamer = find_spamer()
    if spamer:
        print(f"ip spamer: {spamer[0]}, count: {spamer[1]}")

  #  Задание  3 

import os
import json

from itertools import zip_longest

def groping(
        output_pth="./out.txt",
        user_pth="./users.csv",
        hobby_pth="./hobby.csv"):

    if not (os.path.isfile(user_pth) or
            os.path.isfile(hobby_pth)):
        return -1
    user_lines = None
    hobby_lines = None

    with open(user_pth, "r", encoding="utf-8") as user_file:
        user_lines = user_file.readlines()

    with open(hobby_pth, "r", encoding="utf-8") as hobby_file:
        hobby_lines = hobby_file.readlines()

    if len(user_lines) < len(hobby_lines):
        return 1

    group = {}

    for fio, hobby in zip_longest(user_lines, hobby_lines):
        fio = fio.replace("\n", "")
        group[fio] = hobby.replace("\n", "") if hobby else None

    with open(output_pth, "w+", encoding="utf-8") as out_file:
        json.dump(group, out_file)  

    return 0


if __name__ == "__main__":
    exit(groping())

  #  Задание  6 

PRICE_FILE = "./bakery.csv"


def file_reader(start=-1, end=-1):

    with open(PRICE_FILE, "r", encoding="utf-8") as price_list:

        if start > 0:
            for _ in range(start - 1):
                price_list.readline()
        
        if end > 0:
            for _ in range(abs(end - start) + 1):
                yield price_list.readline().replace("\n", "")
        else:
            for line in price_list:
                yield line.replace("\n", "")


if __name__ == "__main__":

    import sys

    start_pos = -1
    end_pos = -1

    if len(sys.argv) >= 2 and sys.argv[1].isdigit():
        start_pos = int(sys.argv[1])

    if len(sys.argv) == 3 and sys.argv[2].isdigit():
        end_pos = int(sys.argv[2])

    for l in file_reader(start_pos, end_pos):
        print(f"{float(l):.2f}")