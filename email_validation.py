# -*- coding: utf-8 -*-
"""email_validation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TJmayIfw8pusModq0gMZZf6gpq2QUnqF
"""

print('''
             _ _     _       _                              _ _
 __   ____ _| (_) __| | __ _| |_ ___    ___ _ __ ___   __ _(_) |
 \ \ / / _` | | |/ _` |/ _` | __/ _ \  / _ \ '_ ` _ \ / _` | | |
  \ V / (_| | | | (_| | (_| | ||  __/ |  __/ | | | | | (_| | | |
   \_/ \__,_|_|_|\__,_|\__,_|\__\___|  \___|_| |_| |_|\__,_|_|_|
''')

from email_validator import validate_email, EmailNotValidError

email = input('Enter email here: ')

try:
    v = validate_email(email)
    print(f"{email} is valid.")
except EmailNotValidError as e:
    print(str(e))