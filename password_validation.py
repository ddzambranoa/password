# -*- coding: utf-8 -*-
# !/usr/bin/env python3

# -------------------------------------------
# Username Validation
# Programmer:   https://www.linkedin.com/in/ddzambranoa/
# Created:      April 25, 2022
# Copyright:    Free
# License:      Free
# -------------------------------------------

def validation():
    while True:
        try:
            password = input("Enter Your Password: ")
            length = False
            upper = False
            lower = False
            space = False
            num = False
            alpha = password.isalnum()
            no_space = False
            valid = False
            verification = True
            for i in password:
                if i.isupper():
                    upper = True
                if i.islower():
                    lower = True
                if i.isspace():
                    space = True
                if i.isdigit():
                    num = True
            if len(password) >= 8:
                length = True
            else:
                print("Password must contain at least 8 characters")
                valid = False

            if not space:
                no_space = True
                valid = True
            else:
                print("Password must not contain spaces")

            if length and upper and lower and num and no_space and not alpha:
                valid = True
            else:
                verification = False

            if valid and not verification:
                print('Password must contain at least one number and includes both lower and uppercase letters and special characters')
            if valid and verification:
                print("Password is Valid")
                break
        except ValueError:
            print("Something went wrong")


if __name__ == "__main__":
    validation()
