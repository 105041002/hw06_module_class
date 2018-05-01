# -*- coding: utf-8 -*-
from human import *


def main():
    x = American('Obama')
    # should be `Obama says Hello`
    x.say_hi()

    x = French('Napoléon')
    # should be `Napoléon says Bonjour`
    x.say_hi()

    x = Spanish('Picasso')
    # should be `Picasso says Hola`
    x.say_hi()

    x = Japanese('Aragaki Yui')
    # should be `Aragaki Yui says Konnichiwa`
    x.say_hi()

    x = Korean('Yoona')
    # should be `Yoona says Yeoboseyo`
    x.say_hi()

    x = Indian('Gandhi')
    # should be `Gandhi‎ says Namaste`
    x.say_hi()


if __name__ == '__main__':
    main()
