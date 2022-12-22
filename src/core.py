"""This is a password generator that generates a random password of a given length and with some options."""

import secrets  # For generating random numbers
from string import ascii_lowercase, ascii_uppercase
from string import digits as digits_  # import string constants
from string import punctuation as symbols_


class Generator:

    def __init__(self,
                 length=32,
                 letters_l=True,
                 letters_u=True,
                 digits=True,
                 symbols=True):
        self.entry = ""
        self.length = length
        if letters_l:
            self.entry += ascii_lowercase
        if letters_u:
            self.entry += ascii_uppercase
        if digits:
            self.entry += digits_
        if symbols:
            self.entry += symbols_

    def generate_password(self):
        return "".join(secrets.choice(self.entry) for _ in range(self.length))


if __name__ == "__main__":
    g = Generator(length=16).generate_password()
    # pwd = g
    print(g)
