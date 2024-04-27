import pytest

import tiketnlphub.preprocessing.normalizer as normalizer
from tests.fixtures.preprocessing.normalizer import (
    normalize_to_ascii_chars_test_cases, 
    normalize_punctuations_test_cases,
    normalize_punctuations_with_additional_punctuations_test_cases,
    normalize_remunerations_test_cases,
    normalize_remunerations_with_additional_remunerations_test_cases,
    normalize_slashes_en_test_cases,
    normalize_slashes_id_test_cases,
    normalize_symbols_en_test_cases,
    normalize_symbols_id_test_cases,
    normalize_symbols_with_additional_symbols_test_cases,
    normalize_parentheses_test_cases,
    normalize_non_ascii_char_currencies_test_cases,
    normalize_contractions_default_test_cases,
    normalize_contractions_with_addition_test_cases,
    normalize_fullstops_test_cases,
    normalize_split_word_and_num_test_cases
)


def test_normalize_to_ascii_chars(normalize_to_ascii_chars_test_cases):
    for input_text, expected_output in normalize_to_ascii_chars_test_cases:
        result = normalizer.normalize_to_ascii_chars(input_text)
        assert expected_output == result


def test_normalize_punctuations(normalize_punctuations_test_cases):
    for input_text, expected_output in normalize_punctuations_test_cases:
        result = normalizer.normalize_punctuations(input_text)
        assert expected_output == result


def test_normalize_punctuations_with_additional_punctuations(normalize_punctuations_with_additional_punctuations_test_cases):
    for input_text, expected_output in normalize_punctuations_with_additional_punctuations_test_cases:
        result = normalizer.normalize_punctuations(input_text, additional_punctuations={"!": "."})
        assert expected_output == result


def test_normalize_remunerations(normalize_remunerations_test_cases):
    for input_text, expected_output in normalize_remunerations_test_cases:
        result = normalizer.normalize_remunerations(input_text)
        assert expected_output == result


def test_normalize_remunerations_with_additional_remunerations(normalize_remunerations_test_cases):
    for input_text, expected_output in normalize_remunerations_test_cases:
        result = normalizer.normalize_remunerations(input_text, additional_remunerations={"(?<=\s)ber ": "ber"})
        assert expected_output == result


def test_normalize_slashes_en(normalize_slashes_en_test_cases):
    for input_text, expected_output in normalize_slashes_en_test_cases:
        result = normalizer.normalize_slashes(input_text, lang="en")
        assert expected_output == result


def test_normalize_slashes_id(normalize_slashes_id_test_cases):
    for input_text, expected_output in normalize_slashes_id_test_cases:
        result = normalizer.normalize_slashes(input_text, lang="id")
        assert expected_output == result


def test_normalize_symbols_en(normalize_symbols_en_test_cases):
    for input_text, expected_output in normalize_symbols_en_test_cases:
        result = normalizer.normalize_symbols(input_text, lang="en")
        assert expected_output == result


def test_normalize_symbols_id(normalize_symbols_id_test_cases):
    for input_text, expected_output in normalize_symbols_id_test_cases:
        result = normalizer.normalize_symbols(input_text, lang="id")
        assert expected_output == result


def test_normalize_symbols_with_additional_symbols(normalize_symbols_with_additional_symbols_test_cases):
    for input_text, expected_output in normalize_symbols_with_additional_symbols_test_cases:
        result = normalizer.normalize_symbols(input_text, lang="en", additional_symbols={"Rp.": "IDR"})
        assert expected_output == result


def test_normalize_parentheses(normalize_parentheses_test_cases):
    for input_text, expected_output in normalize_parentheses_test_cases:
        result = normalizer.normalize_parentheses(input_text)
        assert expected_output == result


def test_normalize_non_ascii_char_currencies(normalize_non_ascii_char_currencies_test_cases):
    for input_text, expected_output in normalize_non_ascii_char_currencies_test_cases:
        result = normalizer.normalize_non_ascii_char_currencies(input_text)
        assert expected_output == result


def test_normalize_contractions_default(normalize_contractions_default_test_cases):
    for input_text, expected_output in normalize_contractions_default_test_cases:
        result = normalizer.normalize_contractions(input_text, additional_contractions=None)
        assert expected_output == result


def test_normalize_contractions_with_addition(normalize_contractions_with_addition_test_cases):
    additional_contractions = {"she'll've": "she will have", "he'd've": "he would have"}
    for input_text, expected_output in normalize_contractions_with_addition_test_cases:
        result = normalizer.normalize_contractions(input_text, additional_contractions=additional_contractions)
        assert expected_output == result


def test_normalize_fullstops(normalize_fullstops_test_cases):
    for input_text, expected_output in normalize_fullstops_test_cases:
        result = normalizer.normalize_fullstops(input_text)
        assert expected_output == result


def test_split_word_and_num(normalize_split_word_and_num_test_cases):
    for input_text, expected_output in normalize_split_word_and_num_test_cases:
        result = normalizer.split_word_and_num(input_text)
        assert expected_output == result







    

