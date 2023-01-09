  """ Задание 1 и 2 """

def odd_num(to):
    
    for i in range(1, to + 1, 2):
        yield i

def odd_num_no_yield(to):
    
    return (x for x in range(1, to + 1, 2))

if __name__ == "__main__":
    a_gen = odd_num(15)
    b_gen = odd_num_no_yield(15)

    print("a_gen type", type(a_gen))
    print("b_gen type", type(b_gen))

    for elem in a_gen:
        print(elem)

    print(f"empty {list(a_gen)}")

""" Задание 3 """

from sys import getsizeof

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена' ]
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

def my_zip_gen():

    len_klasses = len(klasses)

    return ((tut, klasses[i]) if i < len_klasses else (tut, None)
            for i, tut in enumerate(tutors))
if __name__ == '__main__':

    gen = my_zip_gen()
    print(type(gen))
    print(getsizeof(gen))
    print(*gen)

""" Задание 4 """

import time
import sys

def my_filter(*argv):
    return (argv[i] for i in range(1, len(argv)) if argv[i] > argv[i - 1])

if __name__ == "__main__":

    src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
    result = [12, 44, 4, 10, 78, 123]
    
    answ = my_filter(*src)
   
    print(sys.getsizeof(answ))
    

""" Задание 5 """

import time  
import sys  

def my_set(*argv):
  
    answ = set()

    for elem in argv:
        if not elem in answ:
            answ.add(elem)
        else:
            answ.remove(elem)

    return [x for x in argv if x in answ]  

if __name__ == "__main__":

    src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
    result = [23, 1, 3, 10, 4, 11]

    t = time.perf_counter()
    r = my_set(*src)
    print(r)
