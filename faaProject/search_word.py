#!/usr/bin/env python3

path_to_user = '../../'

import pandas as pd
import re

# find out more about word
def lookup(find_word, data, search_col, show_cols, acronym_find=False, loose_match=False, output=True):
    indices = []
    for index in data[search_col].dropna().index:
        if acronym_find:
            search_data = data[search_col]
            letters = [letter for letter in find_word]
            pat_str = '.* '
            for letter in letters:
                pat_str = pat_str + f'({letter}[a-z]*) '
            pat_str = pat_str + '.*'
            p = re.compile(pat_str)
            match = re.match(p, data[search_col].iat[index].lower()+' ')
            if match:
                indices.append(index)
                if out_put:
                    print(index)
                    print(match.groups())
                    for column in show_cols :
                        print(data[column].iat[index])
                    print()
        else:
            for word in data[search_col].iat[index].lower().split():
                hit = False
                if loose_match and find_word in word:
                    hit = True
                elif find_word == word:
                    hit = True
                    
                if hit:
                    indices.append(index)
                    if output:
                        print(index)
                        print(word)
                        for column in show_cols :
                            print(data[column].iat[index])
                        print()
    return indices