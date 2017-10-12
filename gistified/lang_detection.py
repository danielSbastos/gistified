from pygments.lexers import get_lexer_for_filename

import re


def which_lang(title):
    try:
        lang_lexer = str(get_lexer_for_filename(title))
        lang = re.search('lexers.(.*)Lexer', lang_lexer).group(1)
    except:
        lang = "undefined"

    return lang
