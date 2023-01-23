  #  Задание 1

import os

folder_struct = {
    "my_project": [
        {
            "settings": [{"bar": [], "foo":[]}],
            "mainapp": [],
            "adminapp": [],
            "authapp": []
        }]
}


def project_starter(pth, struct):

    for fold_node, ch_node in struct.items():

        test_path = os.path.join(pth, fold_node)

        if not os.path.exists(test_path):
            os.mkdir(test_path)

        if len(ch_node) > 0:
            for node in ch_node:
                project_starter(test_path, node)


if __name__ == "__main__":

    project_starter(os.getcwd(), struct=folder_struct)

  #  Задание 3


if __name__ == "__main__":

    import os
    import sys
    import shutil

    glb_path = sys.argv[1]
    files = [os.path.relpath(os.path.join(root, file), glb_path) for root, _, files in os.walk(
        glb_path) for file in files if file.endswith(".html")]
    for rel_path in files:
        path, file = os.path.split(rel_path)
        test_path = os.path.join(glb_path, "template", path)
        if not os.path.exists(test_path):
            os.makedirs(test_path)
        shutil.copyfile(os.path.join(glb_path,rel_path), os.path.join(test_path, file))

   #  Задание 4

import os
import sys
import time

size = {}


def scan_mem(pth):

    for root, _, files in os.walk(pth):
        for file in files:
            correct_file = os.path.join(root, file)
            mem = 10 ** len(str(os.stat(correct_file).st_size))
            size[mem] = size.get(mem, 0) + 1


def scan_mem_recursion(pth):

    if not os.path.exists(pth):
        return
    with os.scandir(pth) as files:

        for node in files:

            if os.path.isfile(node):

                mem = 10 ** (len(str(os.stat(node).st_size)) - 1)
                size[mem] = size.get(mem, 0) + 1
            elif os.path.isdir(node):
                scan_mem(os.path.join(pth, node))


if __name__ == "__main__":

    if len(sys.argv) == 2:
        pth = sys.argv[1]
    else:
        pth = os.getcwd()
    print(f"{'soution with os.walk':^39}")
    time_now = time.perf_counter()
    scan_mem(pth)
    print(size, f"\n as { time.perf_counter() - time_now}")

    size = {}
    print(f"{'soution with resursion':^39}")
    time_now = time.perf_counter()
    scan_mem_recursion(pth)
    print(size, f"\n as { time.perf_counter() - time_now}")