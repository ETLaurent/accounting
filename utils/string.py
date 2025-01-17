def style(text, ansi_code):
    return ''.join(ansi_code + c + '\033[0m' for c in text)


def bold(text):
    return style(text, '\033[1m')


def dim(text):
    return style(text, '\033[2m')


def italic(text):
    return style(text, '\033[3m')
