import re

WORD_PATTERN = re.compile("[^A-Za-z]+")


def camelcase(chars):
    words = WORD_PATTERN.split(chars)
    return "".join(w.lower() if i is 0 else w.title() for i, w in enumerate(words))


def normalize_keys(allowed_keys, payload):
    data = {}
    message_keys = payload.keys()
    valid_keys = [k for k in message_keys if k in allowed_keys]
    for k in valid_keys:
        data[camelcase(k)] = payload.get(k)
    return data
