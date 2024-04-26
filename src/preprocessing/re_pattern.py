import re


class RegexString:

    DIGITS = r"\d+"
    
    HASTAGS = r"#(\w+)"

    MENTIONS = r"@(\w+)"

    PHONE_NUMBERS = r"\+[0-9\s]{6,}"

    BULLETS = r"(([\-\>\*]+)|(\([\-\+]\)))"

    NUMBERING_BULLETS = r"([0-9]{1,2}[\.\:])(?=\s?[a-z])"

    SYMBOLS = r"[_–—\=\*\|¬#@\\\\]"

    TIME_FORMAT = r"(\d{1,}\:\d{1,}\s?)"
    
    UNITS = r"(malam)|(hari)|(mlm)|(night)|(day)"
    
    REPEAT_PUNCTS = r"[\?\.\!]+(?=[\?\.\!])"
    
    REPEAT_CHARS = r"(\D)\1{2,}"
    
    REPEAT_WORDS = r"\b(\w+)\b(?:\s+\1\b)+"

    REPEAT_CAPS = r"([A-Z]{2,})"

    WORD_NUMBER = r"([a-zA-Z]+)([0-9]+)"

    NUMBER_WORD = r"([0-9]+)([a-zA-Z]+)"

    PUNCT_WORD = r"([.!?;,]+)(\w)"

    UPPER_SELECTED_WORD = r"(^|[.?!])\s*([a-zA-Z])"

    URLS = r"""(https?:\/\/)(\s)*(www\.)?(\s)*((\w|\s)+\.)*([\w\-\s]+\/)*([\w\-]+)((\?)?[\w\s]*=\s*[\w\%&]*)*|www\S+"""

    EMOTICONS = [
            ":)",
            ":]",
            "=)",
            ":-)",
            ":(",
            ":[",
            "=(",
            ":-(",
            ":')",
            ":'(",
            ":p",
            ":P",
            "=P",
            ":-p",
            ":-P",
            ":D",
            "=D",
            ":-D",
            ";-D",
            ";D",
            ">6",
            "(. ͈ᴗ. ͈)",
            "T_T",
            "T___T",
            "T^T",
            "^__^",
            "^^",
            "^ ^",
            ":o",
            ":O",
            ":-o",
            ":-O",
            ";)",
            ";-)",
            "8-)",
            "B-)",
            "^_^",
            "-_-",
            ">:o",
            ">:O",
            ":v",
            ":3",
            "8|",
            "B|",
            "8-|",
            "B-|",
            ">:(",
            ":/",
            ":\\",
            ":-/",
            ":-\\",
            ":'(",
            "O:)",
            ":*",
            ":-*",
            "<3",
            "(y)",
            "(Y)",
        ]


class RegexReplacement:

    BULLETS = {
        f"^{RegexString.BULLETS}": "",
        f"(?<=\s){RegexString.BULLETS}": ". ",
        f"(?<=\.){RegexString.BULLETS}": " ",
        f"{RegexString.BULLETS}(?=\s)": ". ",
    }
    
    NUMBERING_BULLETS = [
        f"((^)|(?<=\s)){RegexString.NUMBERING_BULLETS}",
        f"(?<=[a-z]\s){RegexString.NUMBERING_BULLETS}",
        f"(?<=[a-z][\.\:]\s){RegexString.NUMBERING_BULLETS}",
        f"(?<=[a-z][\.\:]){RegexString.NUMBERING_BULLETS}",
    ]
    
    SPECIAL_PUNCT = {
            "‘": "'",
            "’": "'",
            "´": "'",
            "`": "'",
            "·": ".",
            "※": ".",
            "•": ".",
            "。": ".",
            "~": ".",
            "“": '"',
            "”": '"',
            "[": "(",
            "]": ")",
            "…": "...",
            "²": "2",
            "-->": ",",
            "->": ",",
            ">": ",",
            "\r\n": "\n",
            "⁰": "°",
            "\u200b": " ",
    }
    
    SLASHES = {
        "general": {
            f"(?<=\d)\/(?=({RegexString.UNITS}))": " per ",
            "(?<=\d)\/(?=\d)": " per ",
        },
        "id": {
            f"(?<=\d(rb))\/(?=({RegexString.UNITS}))": " per ",
            f"\/": " atau ",
        },
        "en": {
            f"(?<=\d(USD|IDR))\/(?=({RegexString.UNITS}))": " per ",
            f"$(?<=\d)\/(?=({RegexString.UNITS}))": " per ",
            f"\/": " or ",
        }
    }
    
    SYMBOLS = {
        "general": {
            "€": " EUR ",
            "¥": " YEN ",
            "£": " PS ",
            ";": ",",
            "\n": ". ",
        },
        "id": {
            "\+\+": " lebih ",
            "(\+\-)|±|(\-\+)|(\(?\+\/\-\))": " sekitar ",
            "<": " kurang dari ",
            ">": " lebih dari ",
            "½": " setengah ",
            "⅘": " 4 dari 5 ",
            "⅕": " 1 dari 5 ",
            "(?<=\S{2})[&\+](?=\S{2})": " dan ",
            "[&\+](?=\s)": " dan",
            "(?<=\s)[&\+]": "dan ",
        },
        "en": {
            "\+\+": " more ",
            "(\+\-)|±|(\-\+)|(\(?\+\/\-\))": " around ",
            "<": " less than ",
            ">": " more than ",
            "½": " half ",
            "⅘": " 4 out of 5 ",
            "⅕": " 1 out of 5 ",
            "(?<=\S{2})[&\+](?=\S{2})": " and ",
            "[&\+](?=\s)": " and",
            "(?<=\s)[&\+]": "and ",
        }
    }
    
    PARENTHESES = {
        "^\. ": "",
        " (?=[\.\,\?\!\-\)\:\%])": "",
        "(?<=[\(\$]) ": "",
        "(?<!\W)\(": " (",
        "\)(?!\W)": ") ",
        "\(\)": " ",
        "(?<=[\:\,\!\?\.])[\.,]": "",
    }

    REMUNERATIONS = {
        "(?<=\s)se ": "se", 
        " nya(?![a-z\-])": "nya"
    }
