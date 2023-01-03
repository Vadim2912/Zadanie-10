""" 1 and 2 """

DICT_NUM = {

    "zero": "ноль",
    "one": "один",
    "two": "два",
    "three": "три",
    "four": "четире",
    "five": "пять",
    "six": "шесть",
    "seven": "семь",
    "eight": "восемь",
    "nine": "девять",
}


def num_translate(num_word):
    """ convert one to один...nine to девять """
    return DICT_NUM.get(num_word)


def num_translate_adv(num_word):
    """ convert one to один...nine to девять with firt char capitalize """
    to_key = DICT_NUM.get(num_word.lower())

    if to_key:
        return to_key.capitalize() if num_word[0].isupper() else to_key

    return None 

""" 3 and 4 """

def thesaurus(*args):
    """ conver name list to dictionary like {A: [Alex..] , B:[Bob..]} """
    out_dict = {}

    for name in args:

        if out_dict.get(name[0]):
            out_dict[name[0]].append(name)
        else:
            out_dict[name[0]] = [name]

    return out_dict


def thesaurus_adv(*args):
    """ conver name list to dictionary like second_name[0]:{name[0]: name + second_name} """
    out_dict = {}
    for elem in args:
        name, second_name = elem.split()
        if not out_dict.get(second_name[0]):
            out_dict[second_name[0]] = { name[0] : [elem] }
        elif not out_dict[second_name[0]].get(name[0]):
            (out_dict[second_name[0]])[name[0]] = [elem]
        else:
            (out_dict[second_name[0]])[name[0]].append(elem)

    return out_dict

""" 5 """

from random import choice


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def gen(from_, used_, unique):
    while True:
        n_nouns = choice(from_)

        if not (unique and n_nouns in used_):
            used_.append(n_nouns)
            break

    return (n_nouns, used_)