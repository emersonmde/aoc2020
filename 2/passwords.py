#!/usr/bin/env python3

import re

def validate1():
    f = open('input')
    regex = re.compile('(\d+)-(\d+) ([a-zA-Z]{1}): ([a-zA-Z]+)')
    valid_passwords = 0
    for line in f:
        matches = regex.match(line)
        if matches is None:
            continue
        groups = matches.groups()
        min_letters = int(groups[0])
        max_letters = int(groups[1])
        letter = groups[2]
        password = groups[3]
        
        letter_count = 0
        for i in password:
            if i == letter:
                letter_count += 1
        if min_letters <= letter_count <= max_letters:
            valid_passwords += 1
    return valid_passwords

def validate2():
    f = open('input')
    regex = re.compile('(\d+)-(\d+) ([a-zA-Z]{1}): ([a-zA-Z]+)')
    valid_passwords = 0
    for line in f:
        matches = regex.match(line)
        if matches is None:
            continue

        groups = matches.groups()
        first_position = int(groups[0]) - 1
        second_position = int(groups[1]) - 1
        letter = groups[2]
        password = groups[3]

        first_valid = 0 <= first_position < len(password) and password[first_position] == letter
        second_valid = 0 <= second_position < len(password) and password[second_position] == letter

        # xor
        if first_valid != second_valid:
            valid_passwords += 1

    return valid_passwords


if __name__ == '__main__':
    print(validate1())
    print(validate2())
