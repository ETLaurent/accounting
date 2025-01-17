def bold(text):
    return ''.join('\033[1m' + c + '\033[0m' for c in text)


def dim(text):
    return ''.join('\033[2m' + c + '\033[0m' for c in text)


def italic(text):
    return ''.join('\033[3m' + c + '\033[0m' for c in text)


def strikethrough(text):
    return ''.join(c + '\u0336' for c in text)
