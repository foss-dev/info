import random


def generate(data, length=8):
    chars = {
        "lower": "abcdefghijklmnopqrstuvwxyz",
        "upper": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "numeric": "01234567890",
        "other": "!@#$%^&*()?{}/_-",
        "all": "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890!@#$%^&*()?{}/_-"
    }

    char_set = ""

    if bool(int(data["all"])):
        char_set = chars["all"]
    else:
        for i, (k, v) in enumerate(data.items()):
            if bool(int(v)):
                char_set += chars[str(k)]

    s = ''.join([random.choice(char_set) for _ in range(length)])

    return s
