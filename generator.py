from abc import ABC, abstractmethod
import string
import random

import names


class PasswordGenerator(ABC):
    @abstractmethod
    def generate_password(self):
        pass

class PinPassword(PasswordGenerator):
    def __init__(self, length):
        self.length = length
    def generate_password(self):
        return ''.join([random.choice(string.digits) for _ in range(self.length)])



class RandomPasswordGenerator(PasswordGenerator):
    def __init__(self, allowed_digits : bool = False, allowed_symbols : bool = False , length : int = 8):
        self.allowed_digits = allowed_digits
        self.allowed_symbols = allowed_symbols
        self.length = length
        self.characters = self.generate_characters()

    def generate_characters(self):
        characters = string.ascii_letters
        if self.allowed_digits:
            characters += string.digits
        if self.allowed_symbols:
            characters += string.punctuation
        return characters

    def generate_password(self):
        passcode = ''.join(random.choices(self.characters, k=self.length))
        return passcode



class MemorablePasswordGenerator(PasswordGenerator):
    def __init__(self, seperator='-', length: int = 8, uppercase: bool = True, names: list = None):
        self.seperator = seperator
        self.length = length
        self.uppercase = uppercase
        self.names = names

    def generate_password(self):
        if self.names is None:
            self.names = [names.get_first_name() for _ in range(self.length)]

        password = self.seperator.join(random.choices(self.names, k=self.length))
        if self.uppercase:
            password = password.upper()


        return password

