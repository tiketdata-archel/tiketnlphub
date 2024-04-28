from typing import List
import re
import string

import emoji
from bs4 import BeautifulSoup

from src.tiketnlphub.preprocessing.re_pattern import RegexString, RegexReplacement


def remove_digits(text: str) -> str:
    """
    Removes all digits from the input text.

    Example
    -------
    >>> from tiketnlphub.preprocessing.cleaner import remove_digits
    >>> text = remove_digits("I spent 2 nights here and it was really good")
    >>> text
    I spent  nights here and it was really good
    
    Parameters
    ----------
    text: str
        The text from which digits are to be removed.

    Returns
    -------
    text: str
        The input text with all digits removed.
    """
    return re.sub(RegexString.DIGITS, "", text)
    

def remove_emojis_emoticons(text: str, additional_emoticons: List[str] = None) -> str:
    """
    Removes all emojis and emoticons from the input text.
    
    An emoticon is a sequence of keyboard characters used to illustrate a facial expression (or to render some kind of picture or symbol). For example:
    :) for a smile
    :( for a frown
    XD for a laughing face
    O_O for surprise.
    
    An emoji is a small image used alongside or in place of text. Many depict facial expressions (such as 🙂 and 🙁), but there are many, many other kinds (such as 👍, 💙, and 🐈)

    Optional parameter `additional_emoticons` can be used to add new emoticons to be removed from the string. Please check if the provided emoticons already existed in the re_pattern.RegexString.EMOTICONS constant.

    Example
    -------
    >>> from tiketnlphub.preprocessing.cleaner import remove_emojis_emoticons
    >>> text = remove_emojis_emoticons("I spent 2 nights here and it was really good :)")
    >>> text
    I spent 2 nights here and it was really good

    >>> text = remove_emojis_emoticons("I spent 2 nights here and it was really good :) =D", additional_emoticons=["=D"])
    >>> text
    I spent 2 nights here and it was really good

    Parameters
    ----------
    text: str
        The text from which digits are to be removed.

    additional_emoticons: list
        Additional emoticons to remove that have not been listed in the re_pattern.RegexString.EMOTICONS constant. Default is `None`.

    Returns
    -------
    text: str
        The input text with all emoticons and emojis removed.
    """
    # emoticons
    emoticon_pattern = re.compile("|".join([re.escape(x) for x in RegexString.EMOTICONS]))
    text = emoticon_pattern.sub(r"", text)
    if additional_emoticons:
        emoticon_pattern = re.compile("|".join([re.escape(x) for x in additional_emoticons]))
        text = emoticon_pattern.sub(r"", text)
    # emojis
    text = re.sub(emoji.get_emoji_regexp(), r"", text)
    
    return text


def remove_hashtags(text: str) -> str:
    """
    Removes all X (a.k.a Twitter) style hashtags from the input text.

    Example
    -------
    >>> from tiketnlphub.preprocessing.cleaner import remove_hashtags
    >>> text = remove_hashtags("thank you #JWMariott its been a pleasure to stay in your hotel!")
    >>> text
    thank you  its been pleasure to stay in your hotel!
    
    Parameters
    ----------
    text: str
        The text from which hashtags are to be removed.

    Returns
    -------
    text: str
        The input text with all hashtags removed.
    """
    return re.sub(RegexString.HASTAGS, "", text)


def remove_mentions(text: str) -> str:
    """
    Removes all X (a.k.a Twitter) style mentions from the input text.

    Example
    -------
    >>> from tiketnlphub.preprocessing.cleaner import remove_mentions
    >>> text = remove_mentions("kudos to @martin for your hospitality in the last 3 nights. really appreciate it.")
    >>> text
    kudos to  for your hospitality in the last 3 nights. really appreciate it.
    
    Parameters
    ----------
    text: str
        The text from which mentions are to be removed.

    Returns
    -------
    text: str
        The input text with all mentions removed.
    """
    return re.sub(RegexString.MENTIONS, "", text)


def remove_urls(text: str) -> str:
    """
    Removes all web URLs from the input text.

    Example
    -------
    >>> from tiketnlphub.preprocessing.cleaner import remove_urls
    >>> text = remove_urls("there is a promo going on. you can visit their website at https://www.jwmariott.com/promotions")
    >>> text
    there is a promo going on. you can visit their website at 
    
    Parameters
    ----------
    text: str
        The text from which URLs are to be removed.

    Returns
    -------
    text: str
        The input text with all URLs removed.
    """
    return re.sub(RegexString.URLS, "", text, flags=re.IGNORECASE)


def remove_phone_numbers(text: str) -> str:
    """
    Removes all phone numbers from the input text. 
    
    Phone numbers are indicated by consecutive numbers that have 6 or more occurrences

    Example
    -------
    >>> from tiketnlphub.preprocessing.cleaner import remove_phone_numbers
    >>> text = remove_phone_numbers("one thing that I don't like, I need to call 59902034 if I need to replace bedsheets and call for a room service.")
    >>> text
    one thing that I don't like, I need to call  if I need to replace bedsheets and call for a room service.
    
    Parameters
    ----------
    text: str
        The text from which phone numbers are to be removed.

    Returns
    -------
    text: str
        The input text with all phone numbers removed.
    """
    return re.sub(RegexString.PHONE_NUMBERS, "", text, flags=re.IGNORECASE)


def remove_numbering_bullets(text: str) -> str:
    """
    Removes all numbering bullets from the input text. 
    
    Numbering bullets are usually indicated by numbers 1-9 followed with a review.
    Pros: 1. The hotel is .... 2. In additional, the room is ....

    Example
    -------
    >>> from tiketnlphub.preprocessing.cleaner import remove_numbering_bullets
    >>> text = remove_numbering_bullets("Pros: 1. close to the airport. 2. restaurant serves good food. Cons: 1. a little bit pricey. 2. old fashioned")
    >>> text
    Pros: close to the airport.  restaurant serves good food. Cons: a little bit pricey.  old fashioned
    
    Parameters
    ----------
    text: str
        The text from which numbering bullets are to be removed.

    Returns
    -------
    text: str
        The input text with all numbering bullets removed.
    """
    for bullet_style in RegexReplacement.NUMBERING_BULLETS:
        text = re.sub(bullet_style, "", text, flags=re.IGNORECASE)
        
    return text


def remove_bullets(text: str) -> str:
    """
    Removes all unordered bullets from the input text. 
    
    Unordered bullets are usually indicated by the following symbols: -, --, -->, (-), and (+).
    Pros: - The hotel is .... --> In additional, the room is ....
    Cons: (-) The pool is ....

    Example
    -------
    >>> from tiketnlphub.preprocessing.cleaner import remove_bullets
    >>> text = remove_bullets("Pros: - close to the airport - restaurant serves good food. Cons: - a little bit pricey - old fashioned")
    >>> text
    Pros: close to the airport .  restaurant serves good food. Cons: a little bit pricey .  old fashioned
    
    Parameters
    ----------
    text: str
        The text from which unordered bullets are to be removed.

    Returns
    -------
    text: str
        The input text with all unordered bullets removed.
    """
    for bullet, value in RegexReplacement.BULLETS.items():
        text = re.sub(bullet, value, text)
        
    return text


def remove_html_tags(text: str) -> str:
    """
    Removes all HTML tags from the input text.

    Example
    -------
    >>> from tiketnlphub.preprocessing.cleaner import remove_html_tags
    >>> text = remove_html_tags("<html><body><p>I spent 2 nights here and it was really good</html></body></p>")
    >>> text
    I spent 2 nights here and it was really good
    
    Parameters
    ----------
    text: str
        The text from which HTML tags are to be removed.

    Returns
    -------
    text: str
        The input text with all HTML tags removed.
    """
    return BeautifulSoup(text, "html.parser").get_text()


def remove_punctuations(text: str, punct_to_remove: str='all') -> str:
    """
    Removes punctuations from the input text. 
    
    By default, remove all punctuations. However, if you don't want to remove all punctuations, you can provide an optional string parameter `punct_to_remove` and pass the desired punctuation(s)).
    If you want to replace them instead, see `tiketnlphub.preprocessing.normalizer.normalize_symbols`.

    Example
    -------
    >>> from tiketnlphub.preprocessing.cleaner import remove_punctuations
    >>> text = remove_punctuations("I booked this hotel cheaper at $50 last weekend.")
    >>> text
    I booked this hotel cheaper at 50 last weekend

    >>> from tiketnlphub.preprocessing.cleaner import remove_punctuations
    >>> text = remove_punctuations("I booked this hotel cheaper at $50 last weekend!", punct_to_remove='.,!?')
    >>> text
    I booked this hotel cheaper at $50 last weekend

    Parameters
    ----------
    text: str
        The text from which punctuations are to be removed/replaced.

    punct_to_remove: str
        Define own punctuations to remove. Default is `all`, remove all in `string.punctuations` punctuation list.

    Returns
    -------
    text: str
        The input text with all punctuations removed/replaced.
    """
    if punct_to_remove == 'all':
        translator = str.maketrans("", "", string.punctuation)
    else:
        translator = str.maketrans("", "", punct_to_remove)
        
    text = text.translate(translator)

    return text


def remove_white_spaces(text: str) -> str:
    """
    Removes excessive white/empty spaces from the input text.

    Example
    -------
    >>> from tiketnlphub.preprocessing.cleaner import remove_white_spaces
    >>> text = remove_white_spaces("   I  booked this hotel cheaper at            $50   last weekend.   ")
    >>> text
    I booked this hotel cheaper at 50 last weekend.

    Parameters
    ----------
    text: str
        The text from which white spaces are to be removed.

    Returns
    -------
    text: str
        The input text with all white spaces removed.
    """
    return " ".join(word.strip() for word in text.split())


def remove_repeated_chars(text: str) -> str:
    """
    Removes repeated characters from the input text. Repeated characters are the consecutive placement of the same character with more than 2 times.
    
    Be mindful that some English words ARE NOT considered repeated characters if it occurs 2 times only. Words like book, foot, goose, beep, etc. ARE NOT considered as repeated chars.

    Example
    -------
    >>> from tiketnlphub.preprocessing.cleaner import remove_repeated_chars
    >>> text = remove_repeated_chars("This hotel is soooooooo cheap. Booked this at only $50 last weekend.")
    >>> text
    This hotel is so cheap. Booked this at only $50 last weekend.

    Parameters
    ----------
    text: str
        The text from which the repeated characters are to be removed.

    Returns
    -------
    text: str
        The input text with all repeated characters removed.
    """
    return re.sub(RegexString.REPEAT_CHARS, r"\1", text)


def remove_repeated_words(text: str) -> str:
    """
    Removes repeated words from the input text. 
    
    Repeated words are the consecutive placement of the same word with more than 1 time.

    Example
    -------
    >>> from tiketnlphub.preprocessing.cleaner import remove_repeated_words
    >>> text = remove_repeated_words("This hotel is very very very very cheap. Booked this at only $50 last weekend.")
    >>> text
    This hotel is very cheap. Booked this at only $50 last weekend.

    Parameters
    ----------
    text: str
        The text from which repeated words are to be removed.

    Returns
    -------
    text: str
        The input text with all repeated words removed.
    """
    return re.sub(RegexString.REPEAT_WORDS, r"\1", text)


def remove_repeated_puncts(text: str) -> str:
    """
    Removes repeated punctuations from the input text. 
    
    Repeated punctuations are the consecutive placement of the same punctuation with more than 1 time.
    If multiple repeated punctuations exist in the same string, it will be replaced by the last punctuation found at the end of the string.

    Example
    -------
    >>> from tiketnlphub.preprocessing.cleaner import remove_repeated_puncts
    >>> text = remove_repeated_puncts("This hotel is very cheap!!!!!!. Booked this at only $50 last weekend.")
    >>> text
    This hotel is very cheap! Booked this at only $50 last weekend.

    >>> from tiketnlphub.preprocessing.cleaner import remove_repeated_puncts
    >>> text = remove_repeated_puncts("This hotel is very cheap.......???????????!!!!!!!. Booked this at only $50 last weekend.")
    >>> text
    This hotel is very cheap! Booked this at only $50 last weekend.

    Parameters
    ----------
    text: str
        The text from which repeated punctuations are to be removed.

    Returns
    -------
    text: str
        The input text with all repeated punctuations removed.
    """
    return re.sub(RegexString.REPEAT_PUNCTS, "", text)
    

def split_punct_and_word(text: str) -> str:
    """
    Splits consecutive occurences between a punctuation followed by a word. 
    
    Included punctuations: ".,!?;"

    Example
    -------
    >>> from tiketnlphub.preprocessing.cleaner import split_punct_and_word
    >>> text = split_punct_and_word("Hello!How are you?I am fine,thank you;and you?")
    >>> text
    Hello! How are you? I am fine, thank you; and you?

    Parameters
    ----------
    text: str
        The text from which punctuation and words are to be split.

    Returns
    -------
    text: str
        The input text with all punctuations and words split.
    """
    return re.sub(RegexString.PUNCT_WORD, r"\1 \2", text)


def upper_selected_word(text: str) -> str:
    """
    Capitalize input text and convert all letters to uppercase after certain punctuations (.?!).

    Example
    -------
    >>> from tiketnlphub.preprocessing.cleaner import upper_selected_word
    >>> text = upper_selected_word("stayed at this hotel yesterday. not even once I wake up from my sleep! really enjoyed my stay.")
    >>> text
    Stayed at this hotel yesterday. Not even once I wake up from my sleep! Really enjoyed my stay.

    Parameters
    ----------
    text: str
        The text from which to capitalize and give uppercase for words after certain punctuations.

    Returns
    -------
    text: str
        The input text with all words capitalized and uppercased after certain punctuations.
    """
    return re.sub(RegexString.UPPER_SELECTED_WORD, lambda p: p.group(0).upper(), text.capitalize())


def upper_i_word(text: str) -> str:
    """
    Uppercase for each 'i' word in the text.

    Example
    -------
    >>> from tiketnlphub.preprocessing.cleaner import upper_i_word
    >>> text = upper_i_word("i stayed at this hotel yesterday. not even once i wake up from my sleep! really enjoyed my stay.")
    >>> text
    I stayed at this hotel yesterday. Not even once I wake up from my sleep! Really enjoyed my stay.

    Parameters
    ----------
    text: str
        The text from which the 'i' words are to be uppercased

    Returns
    -------
    text: str
        The input text with all 'i' words uppercased.
    """
    return ' '.join(word.replace('i', 'I') if word.lower() == 'i' else word for word in text.split())


def lower_letter_sequence_caps(text: str) -> str:
    """
    Convert caps (uppercased) a sequence of letter to lowercase.

    Example
    -------
    >>> from tiketnlphub.preprocessing.cleaner import lower_letter_sequence_caps
    >>> text = lower_letter_sequence_caps("i STAYED at THIs hotel yesterday.")
    >>> text
    i stayeed at this hotel yesterday.

    Parameters
    ----------
    text: str
        The text from which the uppercased letter sequence to be lowercased

    Returns
    -------
    text: str
        The input text with all uppercased letter sequence words lowercased.
    """
    return re.sub(RegexString.REPEAT_CAPS, lambda x: x.group(0).lower(), text)


def handle_time_format(text: str) -> str:
    """
    Changed the time format from using ':' to '.' instead.

    Example
    -------
    >>> from tiketnlphub.preprocessing.cleaner import handle_time_format
    >>> text = handle_time_format("Arrived at this hotel at 6:00 am yesterday night.")
    >>> text
    Arrived at this hotel at 6.00 am yesterday night.

    Parameters
    ----------
    text: str
        The text from which the time format to be handled

    Returns
    -------
    text: str
        The input text with time format handled.
    """
    def replace_time(match):
        return match.group(0).replace(":", ".")

    return re.sub(RegexString.TIME_FORMAT, replace_time, text)

