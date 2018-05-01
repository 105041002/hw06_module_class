# -*- coding: utf-8 -*-


class Human:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print(self.name, 'says', self.hi)


class American(Human):
    hi = 'Hello'


class French(Human):
    hi = 'Bonjour'


class Spanish(Human):
    hi = 'Hola'


class Japanese(Human):
    hi = 'Konnichiwa'


class Korean(Human):
    hi = 'Yeoboseyo'


class Indian(Human):
    hi = 'Namaste'
