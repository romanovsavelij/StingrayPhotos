last_key = 1000


def get_unique_key() -> int:
    global last_key
    last_key += 1
    return last_key
