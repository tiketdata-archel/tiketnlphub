import pytest

import tiketnlphub.preprocessing.cleaner as cleaner
from tests.fixtures.preprocessing.cleaner import (
    remove_digits_test_cases,
    remove_emojis_emoticons_test_cases,
    remove_emojis_emoticons_with_additional_emoticons_test_cases,
    remove_hastags_test_cases,
    remove_mentions_test_cases,
    remove_phone_numbers_test_cases,
    remove_numbering_bullets_test_cases,
    remove_bullets_test_cases,
    remove_html_tags_test_cases,
    remove_punctuations_default_test_cases,
    remove_punctuations_with_rules_test_cases,
    remove_white_spaces_test_cases,
    remove_repeated_chars_test_cases,
    remove_repeated_words_test_cases,
    remove_repeated_puncts_test_cases,
    split_punct_and_word_test_cases,
    upper_selected_word_test_cases,
    upper_i_word_test_cases,
    lower_letter_sequence_caps_test_cases,
    handle_time_format_test_cases,
)


def test_remove_digits(remove_digits_test_cases):
    for input_text, expected_output in remove_digits_test_cases:
        result = cleaner.remove_digits(input_text)
        assert expected_output == result
        

def test_remove_emojis_emoticons(remove_emojis_emoticons_test_cases):
    for input_text, expected_output in remove_emojis_emoticons_test_cases:
        result = cleaner.remove_emojis_emoticons(input_text, additional_emoticons=None)
        assert expected_output == result


def test_remove_emojis_emoticons_with_additional_emoticons(remove_emojis_emoticons_with_additional_emoticons_test_cases):
    for input_text, expected_output in remove_emojis_emoticons_with_additional_emoticons_test_cases:
        result = cleaner.remove_emojis_emoticons(input_text, additional_emoticons=["=D"])
        assert expected_output == result


def test_remove_hashtags(remove_hastags_test_cases):
    for input_text, expected_output in remove_hastags_test_cases:
        result = cleaner.remove_hashtags(input_text)
        assert expected_output == result


def test_remove_mentions(remove_mentions_test_cases):
    for input_text, expected_output in remove_mentions_test_cases:
        result = cleaner.remove_mentions(input_text)
        assert expected_output == result


def test_remove_phone_numbers(remove_phone_numbers_test_cases):
    for input_text, expected_output in remove_phone_numbers_test_cases:
        result = cleaner.remove_phone_numbers(input_text)
        assert expected_output == result


def test_remove_numbering_bullets(remove_numbering_bullets_test_cases):
    for input_text, expected_output in remove_numbering_bullets_test_cases:
        result = cleaner.remove_numbering_bullets(input_text)
        assert expected_output == result


def test_remove_bullets(remove_bullets_test_cases):
    for input_text, expected_output in remove_bullets_test_cases:
        result = cleaner.remove_bullets(input_text)
        assert expected_output == result


def test_remove_html_tags(remove_html_tags_test_cases):
    for input_text, expected_output in remove_html_tags_test_cases:
        result = cleaner.remove_html_tags(input_text)
        assert expected_output == result


def test_remove_punctuations_default(remove_punctuations_default_test_cases):
    for input_text, expected_output in remove_punctuations_default_test_cases:
        result = cleaner.remove_punctuations(input_text, rules=None)
        assert expected_output == result


def test_remove_punctuations_with_rules(remove_punctuations_with_rules_test_cases):
    rules = {r"\.": " ", r'"': "", r";": ","}
    for input_text, expected_output in remove_punctuations_with_rules_test_cases:
        result = cleaner.remove_punctuations(input_text, rules=rules)
        assert expected_output == result


def test_remove_white_spaces(remove_white_spaces_test_cases):
    for input_text, expected_output in remove_white_spaces_test_cases:
        result = cleaner.remove_white_spaces(input_text)
        assert expected_output == result


def test_remove_repeated_chars(remove_repeated_chars_test_cases):
    for input_text, expected_output in remove_repeated_chars_test_cases:
        result = cleaner.remove_repeated_chars(input_text)
        assert expected_output == result


def test_remove_repeated_words(remove_repeated_words_test_cases):
    for input_text, expected_output in remove_repeated_words_test_cases:
        result = cleaner.remove_repeated_words(input_text)
        assert expected_output == result


def test_remove_repeated_puncts(remove_repeated_puncts_test_cases):
    for input_text, expected_output in remove_repeated_puncts_test_cases:
        result = cleaner.remove_repeated_puncts(input_text)
        assert expected_output == result


def test_split_punct_and_word(split_punct_and_word_test_cases):
    for input_text, expected_output in split_punct_and_word_test_cases:
        result = cleaner.split_punct_and_word(input_text)
        assert expected_output == result


def test_upper_selected_word(upper_selected_word_test_cases):
    for input_text, expected_output in upper_selected_word_test_cases:
        result = cleaner.upper_selected_word(input_text)
        assert expected_output == result


def test_upper_i_word(upper_i_word_test_cases):
    for input_text, expected_output in upper_i_word_test_cases:
        result = cleaner.upper_i_word(input_text)
        assert expected_output == result


def test_lower_letter_sequence_caps(lower_letter_sequence_caps_test_cases):
    for input_text, expected_output in lower_letter_sequence_caps_test_cases:
        result = cleaner.lower_letter_sequence_caps(input_text)
        assert expected_output == result


def test_handle_time_format(handle_time_format_test_cases):
    for input_text, expected_output in handle_time_format_test_cases:
        result = cleaner.handle_time_format(input_text)
        assert expected_output == result

















