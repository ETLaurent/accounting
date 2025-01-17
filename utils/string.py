import os
import sys


def supports_ansi():
    if not sys.stdout.isatty():
        return False
    term = os.getenv("TERM", "")
    return "xterm" in term or "ansi" in term or "screen" in term


def style(text, ansi_code):
    if supports_ansi():
        return ''.join(ansi_code + c + '\033[0m' for c in text)
    return text


def bold(text):
    return style(text, '\033[1m')


def dim(text):
    return style(text, '\033[2m')


def italic(text):
    return style(text, '\033[3m')
