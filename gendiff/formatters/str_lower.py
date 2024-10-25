def str_lower(word):
    if isinstance(word, bool):
        return str(word).lower()
    if word is None:
        return 'null'
    return word
