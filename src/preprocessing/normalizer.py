import re
import contractions
import unicodedata

from src.preprocessing.re_pattern import RegexString, RegexReplacement


def normalize_to_ascii_chars(text: str) -> str:
    """
    Normalize the input string to standard ASCII characters. 
    
    The normalization method follows these steps:
    1. Normalizes the Unicode input string using the NFKD (Normalization Form Compatibility Decomposition) normalization form. It decomposes characters into their base characters and compatibility characters.
    2. After normalization step, the input string is encoded to ASCII and remove any non-ASCII characters. It will ignore any characters that cannot be represented in ASCII.
    3. Decode those ASCII characters back to a Unicode string using the UTF-8 encoding. It will also ignore any decoding errors.

    Implementation notes:
    - Be mindful as this also removes emojis. If you want to remove only emojis, refer to tiketnlphub.preprocessing.cleaner.remove_emojis_emoticons instead.
    - Accents (German, French, Spanish, etc.) will be normalized to the usual a-z English characters. Avoid using this if you want to keep them.
    - Foreign currencies are also included as non-ASCII characters. Refer to tiketnlphub.preprocessing.normalizer.normalize_non_ascii_char_currencies instead if you want to keep them.

    Example
    -------
    >>> from tiketnlphub.preprocessing.normalizer import normalize_to_ascii_chars
    >>> text = normalize_to_ascii_chars("正本さんのおかげで素晴らしい滞在ができました. Thank you!")
    >>> text
    . Thank you!

    Parameters
    ----------
    text: str
        The text from which the text to be normalized

    Returns
    -------
    text: str
        The normalized ASCII input text.
    """
    return (
        unicodedata.normalize("NFKD", text)
        .encode("ascii", "ignore")
        .decode("utf-8", "ignore")
    )


def normalize_punctuations(text: str, additional_punctuations: dict = None) -> str:
    """
    Normalize punctuations by replacing unusual punctuations with a more common one.

    Additional punctuations can be also added proportionally. To see the existing list of the punctuation-replacement pair, refer to tiketnlphub.preprocessing.re_pattern.RegexReplacement.SPECIAL_PUNCT
    
    Example
    -------
    >>> from tiketnlphub.preprocessing.normalizer import normalize_punctuations
    >>> text = normalize_punctuations("I don’t have any words for this hotel. Worst hotel ever")
    >>> text
    I don't have any words for this hotel. Worst hotel ever

    Parameters
    ----------
    text: str
        The text from which the punctuations to be normalized

    Returns
    -------
    text: str
        The normalized punctuations input text.
    """
    for special_char, replacement in RegexReplacement.SPECIAL_PUNCT.items():
        text = text.replace(special_char, replacement)
    if additional_punctuations:
        for special_char, replacement in additional_punctuations.items():
            text = text.replace(special_char, replacement) 
        
    return text


def normalize_remunerations(text: str, additional_remunerations: dict = None) -> str:
    """
    Normalize remuneration in the input string.

    Remuneration commonly appears in Indonesian based reviews. The se- and -nya affixes will be normalized based on the correct spelling.

    Example
    -------
    >>> from tiketnlphub.preprocessing.normalizer import normalize_remuneration
    >>> text = normalize_remuneration("Ibu pulang ke rumah se cepat nya")
    >>> text
    Ibu pulang ke rumah secepatnya.

    Additional remunerations can be also added proportionally. To see the existing list of the remuneration-replacement pair, refer to tiketnlphub.preprocessing.re_pattern.RegexReplacement.REMUNERATIONS

    Parameters
    ----------
    text: str
        The text from which the remuneration to be normalized

    Returns
    -------
    text: str
        The normalized remuneration input text.
    """
    for pattern, value in RegexReplacement.REMUNERATIONS.items():
        text = re.sub(pattern, value, text, flags=re.IGNORECASE)
    if additional_remunerations:
        for pattern, value in additional_remunerations.items():
            text = re.sub(pattern, value, text, flags=re.IGNORECASE)
        
    return text


def normalize_slashes(text: str, lang="en") -> str:
    """
    Normalize the use of slashes in the input string.

    Slashes can be interpreted differently according to the context. In the reviews, it can be:
    - "or": Swimming pool/private pool
    - "per": Rp. 500,000/night

    Example
    -------
    >>> from tiketnlphub.preprocessing.normalizer import normalize_slashes
    >>> text = normalize_slashes("Got a promo for Rp. 252,000/night nett")
    >>> text
    Got a promo for Rp. 252,000 per night nett

    Parameters
    ----------
    text: str
        The text from which the slashes to be normalized

    Returns
    -------
    text: str
        The normalized slashes input text.
    """
    for pattern, value in RegexReplacement.SLASHES["general"].items():
        text = re.sub(pattern, value, text)
    for pattern, value in RegexReplacement.SLASHES[lang].items():
        text = re.sub(pattern, value, text, flags=re.IGNORECASE)
        
    return text


def normalize_symbols(text: str, lang="en", additional_symbols: dict = None) -> str:
    """
    Normalize the use of symbols in the input string.

    Symbols that represent quantity comparison are replaced with the suitable words, including foreign currencies.
    Additional symbols can be also added proportionally. To see the existing list of the symbol-replacement pair, refer to tiketnlphub.preprocessing.re_pattern.RegexReplacement.SYMBOLS

    Example
    -------
    >>> from tiketnlphub.preprocessing.normalizer import normalize_slashes
    >>> text = normalize_slashes("Got a promo for $252")
    >>> text
    Got a promo for USD252

    Parameters
    ----------
    text: str
        The text from which the symbols to be normalized

    Returns
    -------
    text: str
        The normalized symbols input text.
    """
    for pattern, value in RegexReplacement.SYMBOLS["general"].items():
        text = re.sub(pattern, value, text)
    for pattern, value in RegexReplacement.SYMBOLS[lang].items():
        text = re.sub(pattern, value, text)
    if additional_symbols:
        for pattern, value in additional_symbols.items():
            text = re.sub(pattern, value, text)
        
    return text


def normalize_parentheses(text: str) -> str:
    """
    Normalize the correct use of parenthesess by removing spaces in between in the input string.

    Example
    -------
    >>> from tiketnlphub.preprocessing.normalizer import normalize_parentheses
    >>> text = normalize_parentheses("No ( space before open parenthesis ) .")
    >>> text
    No (space before open parenthesis).

    Parameters
    ----------
    text: str
        The text from which the parentheses to be normalized

    Returns
    -------
    text: str
        The normalized parenthesess input text.
    """
    for pattern, value in RegexReplacement.PARENTHESES.items():
        text = re.sub(pattern, value, text)
        
    return text


def normalize_non_ascii_char_currencies(text: str) -> str:
    """
    Preserves foreign currencies that are considered as non-ASCII characters.

    If you want to remove them instead, refer to tiketnlphub.preprocessing.normalizer.normalize_to_ascii_chars.

    Example
    -------
    >>> from tiketnlphub.preprocessing.normalizer import normalize_non_ascii_char_currencies
    >>> text = normalize_non_ascii_char_currencies("I don't have any words. Paid €200 for this hotel.")
    >>> text
    I don't have any words. Paid €200 for this hotel.

    Parameters
    ----------
    text: str
        The text from which the punctuations to be normalized

    Returns
    -------
    text: str
        The normalized punctuations input text.
    """
    raw = text
    text = (
        unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("utf-8", "ignore")
    )

    word_list = text.split()
    raw_list = raw.split()

    new_word_list = []
    for w, r in zip(word_list, raw_list):
        if len(w) != len(r):
            new_word_list.append(r)
        else:
            new_word_list.append(w)
    text = " ".join(new_word_list)
    
    return text


def normalize_contractions(text: str, additional_contractions: dict=None) -> str:
    """
    Normalize contractions in the input string.

    A contraction is a word made by shortening and combining two words. Words like can't (can + not), don't (do + not), and I've (I + have) are contractions.
    You can add additional contractions if it does not listed yet by providing the `additional_contractions` parameter.

    Example
    -------
    >>> from tiketnlphub.preprocessing.normalizer import normalize_contractions
    >>> text = normalize_contractions("I don't have any words for this hotel. Worst hotel ever")
    >>> text
    I do not have any words for this hotel. Worst hotel ever

    >>> from tiketnlphub.preprocessing.normalizer import normalize_contractions
    >>> text = normalize_contractions("I'd've canceled my booking last week. Worst hotel ever", additional_contractions={"i'd've": "i would have"})
    >>> text
    I would have canceled my booking last week. Worst hotel ever

    Parameters
    ----------
    text: str
        The text from which the contractions to be normalized

    Returns
    -------
    text: str
        The normalized contractions input text.
    """
    if additional_contractions:
        for k, v in additional_contractions.items():
            contractions.add(k, v)
            
    return contractions.fix(text)


def normalize_fullstops(text: str) -> str:
    """
    Normalize the fullstops in the input string.

    - Remove space before a fullstop
    - Add fullstop at the end of the input string (if doesn't exist).

    Example
    -------
    >>> from tiketnlphub.preprocessing.normalizer import normalize_fullstops
    >>> text = normalize_fullstops("I don't have any words for this hotel ... Worst hotel ever")
    >>> text
    I don't have any words for this hotel... Worst hotel ever.

    Parameters
    ----------
    text: str
        The text from which the fullstops to be normalized

    Returns
    -------
    text: str
        The normalized input text.
    """
    # remove space before fullstop
    text = re.sub(r"\s+\.", ".", text)

    # add fullstop the end
    if not text.endswith("."):
        text += "."

    return text


def split_word_and_num(text: str) -> str:
    """
    Split/separate between words followed by numbers without any space and vice versa.

    Some exclusion for words representing ranks (e.g. 1st, 2nd, 3rd, 31th, etc.) are not separated.

    Example
    -------
    >>> from tiketnlphub.preprocessing.normalizer import split_word_and_num
    >>> text = split_word_and_num("I booked this hotel at 74dollars.")
    >>> text
    I booked this hotel at 74 dollars.

    Parameters
    ----------
    text: str
        The text from which the words and numbers to be separated

    Returns
    -------
    text: str
        The separated words and numbers input text.
    """
    word_num_match = re.findall(RegexString.WORD_NUMBER, text)
    num_word_match = re.findall(RegexString.NUMBER_WORD, text)

    if len(word_num_match) > 0:
        for word in word_num_match:
            if word[0] + word[1] in text:
                text = text.replace(word[0] + word[1], " ".join(word))

    elif len(num_word_match) > 0:
        for word in num_word_match:
            if (
                word[1].upper().endswith("ST")
                or word[1].upper().endswith("ND")
                or word[1].upper().endswith("RD")
                or word[1].upper().endswith("TH")
            ):
                continue
            if word[0] + word[1] in text:
                text = text.replace(word[0] + word[1], " ".join(word))

    return text