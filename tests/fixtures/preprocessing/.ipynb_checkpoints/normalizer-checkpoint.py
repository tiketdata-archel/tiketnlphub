import pytest


@pytest.fixture
def normalize_to_ascii_chars_test_cases():
    return [
        ("This is a normal text", "This is a normal text"),
        ("¡Hola, mundo!", "Hola, mundo!"),  # Spanish characters converted to ASCII
        ("Привет, мир!", ", !"),  # Cyrillic characters removed
        ("你好", ""),  # Chinese characters removed
        ("مرحبا", ""),  # Arabic characters removed
        ("नमस्तेदुनिया", ""),  # Devanagari characters removed
        ("こんにちは世界", ""),  # Japanese characters removed
        ("สวัสดีโลก", ""),  # Thai characters removed
        ("مرحبا, Hello, สวัสดี, 你好!", ", Hello, , !"),  # Multiple scripts mixed
        ("12345", "12345"),  # Numbers remain unchanged
        ("$€£¥", "$"),  # Currency symbols: only '$' remain unchanged
        ("αβγδε", ""),  # Greek characters removed
        ("⁰¹²³⁴⁵⁶⁷⁸⁹", "0123456789"),  # Superscript digits converted to ASCII digits
        ("This is a test 😊", "This is a test "),  # Emoticon removed
        ("❤️", ""),  # Heart emoji removed
    ]


@pytest.fixture
def normalize_punctuations_test_cases():
    return [
        ("This is a normal text", "This is a normal text"),
        ("Hello ‘ world ’ !", "Hello ' world ' !"),  # Single quotes replaced
        ("What ’ s up ? ", "What ' s up ? "),  # Single quotes replaced
        ("Let´s go!", "Let's go!"),  # Single quotes replaced
        ("This ` is ` a ` test `", "This ' is ' a ' test '"),  # Backticks replaced
        ("The price is € 10 · 50", "The price is € 10 . 50"),  # Dots replaced
        ("Please choose: 1 ※ 2 ※ 3 ※", "Please choose: 1 . 2 . 3 ."),  # Dots replaced
        ("Bullet points: • First point. • Second point.", "Bullet points: . First point. . Second point."),  # Dots replaced
        ("End of sentence。Middle of sentence。", "End of sentence.Middle of sentence."),  # Dots replaced
        ("Approximately ~ 50% of the time", "Approximately . 50% of the time"),  # Dot replaced
        ("Quotes: “Quoted text”", 'Quotes: "Quoted text"'),  # Double quotes replaced
        ("Data [1, 2, 3] is enclosed in brackets", "Data (1, 2, 3) is enclosed in brackets"),  # Brackets replaced
        ("Let me think about it…", "Let me think about it..."),  # Ellipsis replaced
        ("Temperature: 20⁰C", "Temperature: 20°C"),  # Degree symbol replaced
        ("Website: example.com\r\nContact: info@example.com", "Website: example.com\nContact: info@example.com"),  # Newline replaced
        ("Water boils at 100°C", "Water boils at 100°C"),  # Degree symbol preserved
        ("Order --> 1, 2, 3", "Order , 1, 2, 3"),  # Comma replaced
        ("Redirect -> home page", "Redirect , home page"),  # Comma replaced
        ("Larger -> smaller", "Larger , smaller"),  # Comma replaced
        ("This sentence has zero width spaces\u200b", "This sentence has zero width spaces "),  # Zero width space replaced
    ]


@pytest.fixture
def normalize_punctuations_with_additional_punctuations_test_cases():
    return [
        ("This is a normal text", "This is a normal text"),
        ("Hello world!", "Hello world."),
    ]


@pytest.fixture
def normalize_remunerations_test_cases():
    return [
        ("This is a normal text", "This is a normal text"),
        ("Stanley makan se porsi nasi", "Stanley makan seporsi nasi"),
        ("Ibu sedang membawa barang belanjaan nya", "Ibu sedang membawa barang belanjaannya"),
        ("Ibu pulang ke rumah se cepat nya", "Ibu pulang ke rumah secepatnya"),
    ]


@pytest.fixture
def normalize_remunerations_with_additional_remunerations_test_cases():
    return [
        ("This is a normal text", "This is a normal text"),
        ("Stanley sedang ber tengkar dengan kucing", "Stanley sedang bertengkar dengan kucing")
    ]


@pytest.fixture
def normalize_slashes_id_test_cases():
    return [
        ("This is a normal text", "This is a normal text"),
        ("100rb/malam", "100rb per malam"),  # Replace slash between for 'malam' unit
        ("500/hari", "500 per hari"),  # Replace slash between for 'hari' unit
        ("a/b", "a atau b") # Replace slash with "atau" if not between 2 digits or digits-units pair
    ]


@pytest.fixture
def normalize_slashes_en_test_cases():
    return [
        ("This is a normal text", "This is a normal text"),
        ("100USD/night", "100USD per night"),  # Replace slash between for 'night' unit
        ("100IDR/night", "100IDR per night"),  # Replace slash between for 'night' unit
        ("$100/night", "$100 per night"),  # Replace slash between for 'night' unit
        ("500/day", "500 per day"),  # Replace slash between for 'hari' unit
        ("a/b", "a or b") # Replace slash with "atau" if not between 2 digits or digits-units pair
    ]


@pytest.fixture
def normalize_symbols_id_test_cases():
    return [
        ("This is a normal text", "This is a normal text"),
        ("100€", "100 EUR "),  # Euro symbol replaced
        ("50¥", "50 YEN "),  # Yen symbol replaced
        ("£25", " PS 25"),  # Pound symbol replaced
        ("100++", "100 lebih "),  # Double plus sign replaced
        ("+-50", " sekitar 50"),  # Plus-minus sign replaced
        ("sabun+shampo", "sabun dan shampo"),  # Plus sign replaced
        ("sabun&shampo", "sabun dan shampo"),  # Ampersand replaced
        ("90<100", "90 kurang dari 100"),  # Less than symbol replaced
        ("100>90", "100 lebih dari 90"),  # Less than symbol replaced
        ("1½", "1 setengah "),  # Fraction replaced
        ("⅘", " 4 dari 5 "),  # Fraction replaced
        ("⅕", " 1 dari 5 "),  # Fraction replaced
        ("I; J", "I, J"),  # Semicolon replaced with comma
        ("K\nL", "K. L"),  # Newline replaced with period and space
    ]


@pytest.fixture
def normalize_symbols_en_test_cases():
    return [
        ("This is a normal text", "This is a normal text"),
        ("100€", "100 EUR "),  # Euro symbol replaced
        ("50¥", "50 YEN "),  # Yen symbol replaced
        ("£25", " PS 25"),  # Pound symbol replaced
        ("100++", "100 more "),  # Double plus sign replaced
        ("+-50", " around 50"),  # Plus-minus sign replaced
        ("sabun+shampo", "sabun and shampo"),  # Plus sign replaced
        ("sabun&shampo", "sabun and shampo"),  # Ampersand replaced
        ("90<100", "90 less than 100"),  # Less than symbol replaced
        ("100>90", "100 more than 90"),  # Less than symbol replaced
        ("1½", "1 half "),  # Fraction replaced
        ("⅘", " 4 out of 5 "),  # Fraction replaced
        ("⅕", " 1 out of 5 "),  # Fraction replaced
        ("I; J", "I, J"),  # Semicolon replaced with comma
        ("K\nL", "K. L"),  # Newline replaced with period and space
    ]


@pytest.fixture
def normalize_symbols_with_additional_symbols_test_cases():
    return [
        ("This is a normal text", "This is a normal text"),
        ("Rp. 100", "IDR 100"), 
    ]


@pytest.fixture
def normalize_parentheses_test_cases():
    return [
        ("This is a normal text", "This is a normal text"),
        ("Hello ( world ) !", "Hello (world)!"),  # Remove space inside parentheses
        ("This is a (test) .", "This is a (test)."),  # Remove space before period after parentheses
        ("No ( space before open parenthesis ) .", "No (space before open parenthesis)."),  # Remove space before open parenthesis
        ("( No space after open parenthesis) .", " (No space after open parenthesis)."),  # Remove space after open parenthesis
        ("(No space before close parenthesis ).", " (No space before close parenthesis)."),  # Remove space before close parenthesis
        ("Remove empty parenthesis ( ) .", "Remove empty parenthesis  ."),  # Remove empty parenthesis
        ("No space before period (This is a sentence inside parenthesis. )", "No space before period (This is a sentence inside parenthesis.) "),  # Remove space after period inside parentheses
    ]


@pytest.fixture
def normalize_non_ascii_char_currencies_test_cases():
    return [
        ("This is a normal text", "This is a normal text"),
        ("Price: $10", "Price: $10"), # USD symbol preserved
        ("Price: €10", "Price: €10"),  # Euro symbol preserved
        ("Cost: £20", "Cost: £20"),  # Pound symbol preserved
        ("Product: ¥5000", "Product: ¥5000"),  # Yen symbol preserved
        ("Amount: ₹100", "Amount: ₹100"),  # Rupee symbol preserved
        ("Total: ₹5000", "Total: ₹5000"),  # Rupee symbol preserved
        ("Price: €20 and ₹500", "Price: €20 and ₹500"),  # Euro and Rupee symbols preserved
        ("Cost: £10 and ¥1000", "Cost: £10 and ¥1000"),  # Pound and Yen symbols preserved
        ("Budget: £2000 and €3000", "Budget: £2000 and €3000"),  # Pound and Euro symbols preserved
    ]


@pytest.fixture
def normalize_contractions_default_test_cases():
    return [
        ("This is a normal text", "This is a normal text"),
        ("I'm", "I am"),  # Replace "I'm" with "I am"
        ("You're", "You are"),  # Replace "You're" with "You are"
        ("He's", "He is"),  # Replace "He's" with "He is"
        ("We're", "We are"),  # Replace "We're" with "We are"
        ("That's", "That is"),  # Replace "That's" with "That is"
        ("Can't", "Cannot"),  # Replace "Can't" with "Can not"
        ("Won't", "Will not"),  # Replace "Won't" with "Will not"
        ("Ain't", "Are not"),  # Replace "Ain't" with "Am not"
        ("You'll", "You will"),  # Replace "You'll" with "You will"
        ("I've", "I have"),  # Replace "I've" with "I have"
        ("He'll", "He will"),  # Replace "He'll" with "He will"
        ("Would've", "Would have"),  # Replace "Would've" with "Would have"
        ("Shell", "She Will") # Also works without the apostrophe sign
    ]


@pytest.fixture
def normalize_contractions_with_addition_test_cases():
    return [
        ("This is a normal text", "This is a normal text"),
        ("She'll've", "She will have"),  # Replace "She'll've" with "She will have"
        ("He'd've", "He would have"),  # Replace "He'd've" with "She would have"
    ]


@pytest.fixture
def normalize_fullstops_test_cases():
    return [
        ("This is a normal text without fullstop", "This is a normal text without fullstop."), # Added fullstop at the end of sentence
        ("Another sentence .", "Another sentence."),  # Remove space before fullstop
        ("This has multiple fullstops . .", "This has multiple fullstops.."),  # Remove spaces in between
    ]


@pytest.fixture
def normalize_split_word_and_num_test_cases():
    return [
        ("This is a normal text", "This is a normal text"),
        ("The price is 15dollars", "The price is 15 dollars"),  # Split needed
        ("The price is $15", "The price is $15"),  # No split needed
        ("The price is Rp15", "The price is Rp 15"),  # No split needed
        ("This is the 1st floor", "This is the 1st floor"),  # No split needed
    ]

















