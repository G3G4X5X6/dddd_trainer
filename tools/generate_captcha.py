# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 19:35:16 2022

@author: Administrator
"""

import random
from captcha.image import ImageCaptcha


CHARS_SET = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789"


def get_random_chars(len=4):
    chars = []
    for i in range(0, len):
        chars.append(random.choice(CHARS_SET))
    return "".join(chars)


def generate_captcha(path):

    image = ImageCaptcha()

    chars = get_random_chars()
    image.write(chars, path + chars + "_" +
                str(random.getrandbits(128)) + '.png')


if __name__ == "__main__":
    data_dir = "C:/Users/Administrator/Documents/GitHub/dddd_trainer/data/images_set/"
    # generate_captcha(data_dir)

    # TODO use threading
    count = 0
    while count < 10000:
        generate_captcha(data_dir)
        count += 1
