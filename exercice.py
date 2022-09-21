#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import re


def get_num_letters(text: str):
    return sum(1 if lett.isalnum() else 0 for lett in text)


def get_word_length_histogram(text):
    pattern = re.compile("\\W")
    words = list(filter(lambda x: x, [pattern.sub("", single_w) for single_w in text.strip().split(" ")]))
    words_num_map = [len(word) for word in words]

    max_len = max(words_num_map)
    histogram = []
    for i in range(0, max_len+1):
        histogram.append(words_num_map.count(i))

    return histogram


def format_histogram(histogram):
    ROW_CHAR = "*"
    NB_SPACE_BEF = math.floor(math.log(len(histogram)-1, 10))
    res = ""

    iter_hist = iter(histogram)
    next(iter_hist)  # omits first index (0 characters)
    for i, num in enumerate(iter_hist):
        res += f"{' '*(NB_SPACE_BEF-math.floor(math.log(i+1, 10)))}{i+1} {ROW_CHAR*num}\n"

    return res


def format_horizontal_histogram(histogram):
    BLOCK_CHAR = "|"
    LINE_CHAR = "¯"
    res = ""
    max_len = max(histogram)
    len_histo = len(histogram)

    for i in range(max_len, 0, -1):
        iter_hist = iter(histogram)
        next(iter_hist)
        for j, num in enumerate(iter_hist):
            if num == i:
                res += BLOCK_CHAR
                histogram[j+1] = num - 1
            else:
                res += " "
        res += "\n"

    res += LINE_CHAR*len_histo
    return res


if __name__ == "__main__":
    spam = "Stop right there criminal scum! shouted the guard confidently."
    eggs = get_word_length_histogram(spam)
    print(eggs, "\n")
    print(format_histogram(eggs), "\n")
    print(format_horizontal_histogram(eggs))
