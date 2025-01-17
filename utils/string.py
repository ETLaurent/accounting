import os
import sys


def supports_ansi():
    if not sys.stdout.isatty():
        return False
    term = os.getenv("TERM", "")
    return "xterm" in term or "ansi" in term or "screen" in term


def style(text, ansi_code):
    if supports_ansi():
        return ''.join(ansi_code + char + '\033[0m' for char in text)
    return text


def bold(text):
    return style(text, '\033[1m')


def dim(text):
    if supports_ansi():
        return style(text, '\033[2m')
    return ''.join(char + '\u0336' for char in text)


def italic(text):
    return style(text, '\033[3m')
