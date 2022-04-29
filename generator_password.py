# -*- coding: utf-8 -*-
# !/usr/bin/env python3

# -------------------------------------------
# Username Validation
# Programmer:   https://www.linkedin.com/in/ddzambranoa/
# Created:      April 25, 2022
# Copyright:    Free
# License:      Free
# -------------------------------------------

import random
import secrets
import string


def generator():
    while True:
        try:
            length = int(input("Please Enter Password Length: "))
            if length >= 4:
                random_source = string.ascii_letters + string.digits + string.punctuation
                password = random.choice(string.ascii_lowercase)
                password += random.choice(string.ascii_uppercase)
                password += random.choice(string.digits)
                password += random.choice(string.punctuation)
                password += ''.join((secrets.choice(random_source) for _ in range(length - 4)))
                password_list = list(password)
                random.SystemRandom().shuffle(password_list)
                password = ''.join(password_list)
                print(password)
                break
            else:
                print("Password must contain at least 4 characters")
        except ValueError:
            print("Something went wrong")


if __name__ == "__main__":
    generator()
