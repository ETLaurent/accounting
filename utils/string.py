def strikethrough(text):
    return ''.join(c + '\u0336' for c in text)


def italic(text):
    return ''.join('\033[3m' + c + '\033[0m' for c in text)
