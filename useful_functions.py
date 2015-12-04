 #!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import generators
import numpy as np
import random
import unicodedata
import codecs

def prefi_freqs(name_list):
    start_freqs = {}
    for name in name_list:
        if len(name) > 2:
            prefi = name[:3]
            if prefi not in start_freqs.keys():
                start_freqs[prefi] = [1, name]
            else:
                start_freqs[prefi][0] += 1
                start_freqs[prefi].append(name)
    return start_freqs

def full_prefi_freqs(name_list):
    start_freqs = {}
    for line in name_list:
        name = line[0]
        #if (len(name) > 2) & (line[1]=='m'):
        if (len(name) > 2):
            prefi = name[:3]
            if prefi not in start_freqs.keys():
                if line[2]:
                    start_freqs[prefi] = [1, set(line[2][0]), name]
                else:
                    start_freqs[prefi] = [1, set(), name]
            else:
                start_freqs[prefi][0] += 1
                if line[2]:
                    start_freqs[prefi][1].add(line[2][0])
                start_freqs[prefi].append(name)

    for pref in start_freqs:
        start_freqs[pref][1] = ''.join(list(start_freqs[pref][1]))
    return start_freqs

def load_Pi():
    Pi = ''
    Pi_open = open('pi_10_million.txt', 'r')
    Pi_lines = Pi_open.readlines()
    for i in Pi_lines:
        Pi += i[:-1]
    return Pi

def generate_name_list(filename):
    name_list = []
    f_open = open(filename, 'r')
    f_lines = f_open.readlines()
    for name in f_lines:
        name_list.append(name[:-1])
    return name_list

def number_letter_dict():
    letters = 'abcdefghijklmnopqrstuvwxyz'
    num_let_dict = {}
    for i, let in enumerate(letters):
        num_let_dict[let] = str(i+1)
    return num_let_dict

def remove_symbols(name):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    simplified_name = ''
    for let in name.lower():
        if let in letters:
            simplified_name += let
    return simplified_name

def names_to_numbers(name):
    num_dict = number_letter_dict()
    coded_name = ''
    for let in name.lower():
        print let
        coded_name += num_dict[let]
    return coded_name

if __name__ == "__main__":

    i_num = names_to_numbers('Alpha')
    Pi = load_Pi()
    print i_num
    if i_num in Pi:
        print 'yes!', 'position = ', Pi.find(i_num)
    else:
        print 'no....'

    boy_list = generate_name_list('vhs_male_names.txt')
    girl_list = generate_name_list('vhs_female_names.txt')
    both_list = generate_name_list('vhs_names.txt')

    caca

    names_set = set()
    all_list = []

    Pi = load_Pi()
    #names_set.add('nori')
    #a = names_to_numbers(names_set)
    #print Pi.index(str(a['nori']))

    prenoms_list = []
    prenoms_open = codecs.open('Prenoms.csv','r','utf-8')
    prenoms = prenoms_open.readlines()
    for line in prenoms[:]:
        #line = [x.lower() for x in line]
        line = line.lower()
        name = line.split(',')[:3][0]
        if name not in names_set:
            names_set.add(name)
            prenoms_list.append(line.split(',')[:3])
            all_list.append(line.split(',')[:3])
    #for name in prenoms_list:
        #names_set.add(name[0])

    boy_france_list = []
    boy_france_open = codecs.open('boy-names-france.txt','r','utf-8')
    boy_france = boy_france_open.readlines()
    for name in boy_france:
        name = name[:-1].lower()
        if name not in names_set:
            names_set.add(name)
            boy_france_list.append([name, 'm', 'french'])
            all_list.append([name, 'm', 'french'])

    gringo_name_list = []
    gringo_set_b = set([])
    gringo_set_g = set([])
    gringo_open = codecs.open('baby-names.csv', 'r', 'utf-8')
    gringo_names = gringo_open.readlines()
    for name_line in gringo_names[3:]:
        temp = name_line[:-1].split(',')
        name = temp[1][1:-1].lower()
        if name not in names_set:
            print name
            names_set.add(name)
            sex = temp[3][1:-1]
            if sex == 'boy':
                gringo_name_list.append([name, 'm', 'english'])
                all_list.append([name, 'm', 'english'])
            if sex == 'girl':
                gringo_name_list.append([name, 'm', 'english'])
                all_list.append([name, 'f', 'english'])

    boy_mexico_list = []
    boy_mexico_open = codecs.open('boy-names-mexico','r','utf-8')
    boy_mexico = boy_mexico_open.readlines()
    for name in boy_mexico:
        name = name.lower()
        if name not in names_set:
            names_set.add(name)
            boy_mexico_list.append([name[:-1], 'm', 'spanish'])
            all_list.append([name[:-1], 'm', 'spanish'])

    boy_mexico2_list = []
    boy_mexico2_open = codecs.open('boy-names-mexico2','r','utf-8')
    boy_mexico2 = boy_mexico2_open.readlines()
    for name in boy_mexico2:
        name = name.lower()
        if name not in names_set:
            names_set.add(name)
            boy_mexico2_list.append([name[:-1], 'm', 'spanish'])
            all_list.append([name[:-1], 'm', 'spanish'])

    girl_france_list = []
    girl_france_open = codecs.open('girl-names-france.txt','r','utf-8')
    girl_france = girl_france_open.readlines()
    for name in girl_france:
        name = name.lower()
        if name not in names_set:
            names_set.add(name)
            girl_france_list.append([name[:-1], 'f', 'french'])
            all_list.append([name[:-1], 'f', 'french'])

    girl_mexico_list = []
    girl_mexico_open = codecs.open('girl-names-mexico','r','utf-8')
    girl_mexico = girl_mexico_open.readlines()
    for name in girl_mexico:
        name = name.lower()
        if name not in names_set:
            names_set.add(name)
            girl_mexico_list.append([name[:-1], 'f', 'spanish'])
            all_list.append([name[:-1], 'f', 'spanish'])

    girl_mexico2_list = []
    girl_mexico2_open = codecs.open('girl-names-mexico2','r','utf-8')
    girl_mexico2 = girl_mexico2_open.readlines()
    for name in girl_mexico2:
        name = name.lower()
        if name not in names_set:
            names_set.add(name)
            girl_mexico2_list.append([name[:-1], 'f', 'spanish'])
            all_list.append([name[:-1], 'f', 'spanish'])

    #all_dict = names_to_numbers(names_set)

    #names = all_dict.keys()
    #print fibo_names(names, 666), '\n'
    #print prime_names(names)
    #prefis = prefi_freqs(names)

    franco_mexa = []
    for line in all_list:
        lang = line[2][:6]
        langs = ['french', 'spanis', 'basque', 'catalan', 'portug', 'proven', 'litera', 'late r', 'breton','englis']
        #if lang in langs:
        #if lang != 'englis':
        if lang:
            franco_mexa.append(line)

    counter = 0
    prefis = full_prefi_freqs(franco_mexa)
    for prefi in prefis.keys():
        #if prefis[prefi][0] > 5:
        if len(prefis[prefi][1]) >= 1:
            names = ''
            for name in prefis[prefi][2:]:
                names += name+', '
            print prefi, prefis[prefi][1],
            print names
            print '\n'
            counter +=  1
    print 'total = ', counter
    print remove_accents(prefis[prefi][2])
