import pytest


@pytest.fixture
def remove_digits_test_cases():
    return [
        ("This is a normal text", "This is a normal text"),
        ("There are 10 apples", "There are  apples"),  # Remove digits
        ("My phone number is 1234567890", "My phone number is "),  # Remove digits
        ("The price is $15.99", "The price is $."),  # Remove digits
        ("The year is 2022", "The year is "),  # Remove digits
        ("It's 5 o'clock", "It's  o'clock"),  # Remove digits
        ("The room number is 12B", "The room number is B"),  # Remove digits
        ("My age is 30 years old", "My age is  years old"),  # Remove digits
        ("The weight is 5.7 kg", "The weight is . kg"),  # Remove digits
        ("The temperature is -10°C", "The temperature is -°C"),  # Remove digits
        ("The score is 8/10", "The score is /"),  # Remove digits
        ("I have $100 in my wallet", "I have $ in my wallet"),  # Remove digits
    ]
    

@pytest.fixture
def remove_emojis_emoticons_test_cases():
    return [
        ("This is a normal text", "This is a normal text"),
        ("This is a review =).", "This is a review ."),
        ("This hotel is very bad :( the room is smelly and unbearable ^^", "This hotel is very bad  the room is smelly and unbearable "),
        ("This is a test 😊", "This is a test "),
        ("❤️", ""),
    ]


@pytest.fixture
def remove_emojis_emoticons_with_additional_emoticons_test_cases():
    return [
        ("This is a normal text", "This is a normal text"),
        ("This is a review =).", "This is a review ."),
        ("This hotel is very bad :( the room is smelly and unbearable ^^", "This hotel is very bad  the room is smelly and unbearable "),
        ("This is a test 😊", "This is a test "),
        ("❤️", ""),
        ("This is a review =D.", "This is a review ."),
    ]


@pytest.fixture
def remove_hastags_test_cases():
    return [
        ("This is a normal text", "This is a normal text"),
        ("This review has a hashtag #hashtag1", "This review has a hashtag "),
        ("This review has more than one hashtags #hashtag1 #hashtag2 #hashtag3", "This review has more than one hashtags   "),
    ]


@pytest.fixture
def remove_mentions_test_cases():
    return [
        ("This is a normal text", "This is a normal text"),
        ("Thanks to @Stanley who took care of us for 3 days @YogaHotel", "Thanks to  who took care of us for 3 days "),
    ]


@pytest.fixture
def remove_urls_test_cases():
    return [
        ("This is a normal text", "This is a normal text"),
        ("Check out my website at https://example.com", "Check out my website at "),
        ("Visit www.example.com for more info", "Visit  for more info"),
        ("You can also find us at example.com", "You can also find us at "),
        ("This is a link: http://www.example.com/page.html", "This is a link: "),
        ("URLs with special characters: http://www.example.com/#about-us", "URLs with special characters: "),
        ("Multiple URLs included: https://example.com and www.another-example.com", "Multiple URLs included:  and ")
    ]


@pytest.fixture
def remove_phone_numbers_test_cases():
    return [
        ("This is a normal text", "This is a normal text"),
        ("Contact me at +1234567890", "Contact me at "),
        ("Phone numbers: +1 234567890, +12 34567890", "Phone numbers: , "),
        ("Invalid number: +12345", "Invalid number: +12345"),
        ("Numbers with spaces: +12 34 5678 90", "Numbers with spaces: "),
        ("+1234567890", ""),
        ("+1 23 45 67 89 00", ""),
        ("Prices and general numbers should not be removed: Rp. 6000, $3, 50 dollars, 10 people", "Prices and general numbers should not be removed: Rp. 6000, $3, 50 dollars, 10 people")
    ]


@pytest.fixture
def remove_numbering_bullets_test_cases():
    return [
        ("This is a normal text", "This is a normal text"),
        ("1. First item\n2. Second item\n3. Third item", " First item\n Second item\n Third item"), 
        ("Pros: 1. review goes here. 2. review goes here. Cons: 1. review goes here. 2. review goes here.", "Pros:  review goes here.  review goes here. Cons:  review goes here.  review goes here."),
    ]


@pytest.fixture
def remove_bullets_test_cases():
    return [
        ("This is a normal text", "This is a normal text"),
        ("- First item - Second item - Third item", " First item .  Second item .  Third item"), 
        ("- Item 1 -- Item 2 -> Item 3", " Item 1 .  Item 2 .  Item 3"),
        ("(+) Option A (-) Option B (+) Option C", " Option A .  Option B .  Option C"),
        ("Pros: *review goes here. *review goes here. Cons: *review goes here. *review goes here.", "Pros: . review goes here. . review goes here. Cons: . review goes here. . review goes here."),
    ]


@pytest.fixture
def remove_html_tags_test_cases():
    return [
        ("This is a normal text", "This is a normal text"),
        ("<p>This is a <strong>test</strong> with <em>HTML</em> tags.</p>", "This is a test with HTML tags."),  # Basic HTML tags
        ("<div><h1>Title</h1><p>Paragraph</p></div>", "TitleParagraph"),  # Nested HTML tags
        ("<a href='https://example.com'>Link</a>", "Link"),  # Anchor tag with attribute
        ("<p>No HTML tags here!</p>", "No HTML tags here!"),  # No HTML tags
        ("<div><p>This is <a href='#'>link</a></p><p>within <span>div</span></p></div>", "This is linkwithin div"),  # Nested tags with multiple elements
        ("<p>Some text with <br>line break</p>", "Some text with line break"),  # Line break tag
    ]


@pytest.fixture
def remove_punctuations_default_test_cases():
    return [
        ("This is a normal text", "This is a normal text"),
        ("!@#$%^&*()_+-=[]{}|;':,./<>?", ""),  # All punctuations
        ("Unicode punctuations: ¡¿", "Unicode punctuations ¡¿"),  # Unicode punctuations
    ]


@pytest.fixture
def remove_punctuations_with_rules_test_cases():
    return [
        ("This is a normal text", "This is a normal text"),
        ("This is first review; followed by second review", "This is first review, followed by second review"), 
        ("This is first review.This is second review.", "This is first review This is second review "),  
        ('"This is a review"', "This is a review"), 
    ]


@pytest.fixture
def remove_white_spaces_test_cases():
    return [
        ("This is a normal text", "This is a normal text"),
        ("              This is a review with white spaces at the beginning", "This is a review with white spaces at the beginning"), 
        ("This is a review with white spaces at the end             ", "This is a review with white spaces at the end"),  
        (               "This is a review with white spaces at both ends           ", "This is a review with white spaces at both ends"), 
    ]


@pytest.fixture
def remove_repeated_chars_test_cases():
    return [
        ("This is a normal text", "This is a normal text"),
        ("book cool roof loop", "book cool roof loop"), # English words that contain 2 repeated chars are excluded
        ("This hotel is soooooo expensive despite the bad services", "This hotel is so expensive despite the bad services"),
        ("I booked this hotel for around Rp. 1500000", "I booked this hotel for around Rp. 1500000"),  # Digits with repeated characters representing price for example, are fine
        ("!@@##$$%%^^&&", "!@@##$$%%^^&&"),  # No repeated characters 
    ]


@pytest.fixture
def remove_repeated_words_test_cases():
    return [
        ("This is a normal text", "This is a normal text"),
        ("This hotel is very very very very bad", "This hotel is very bad"),
        ("This hotel is veryveryveryvery bad", "This hotel is veryveryveryvery bad"),
    ]


@pytest.fixture
def remove_repeated_puncts_test_cases():
    return [
        ("This is a normal text", "This is a normal text"),
        ("This hotel is very bad!!!!!", "This hotel is very bad!"),
        ("Testing multiple punctuations!?!?!!!....", "Testing multiple punctuations.")
    ]


@pytest.fixture
def split_punct_and_word_test_cases():
    return [
        ("This is a normal text", "This is a normal text"),
        ("Hello!How are you?I am fine,thank you;and you?", "Hello! How are you? I am fine, thank you; and you?"),
        ("Be careful,comma numbers will be also split: $100.10 like this", "Be careful, comma numbers will be also split: $100. 10 like this"),  # No full stop followed by word
    ]


@pytest.fixture
def upper_selected_word_test_cases():
    return [
        ("This is a normal text", "This is a normal text"),
        ("this is a normal text without capitalization", "This is a normal text without capitalization"),
        ("this is a normal text without capitalization. followed by another text, and another text! end of sentence? no this is end of sentence.", "This is a normal text without capitalization. Followed by another text, and another text! End of sentence? No this is end of sentence."),
    ]


@pytest.fixture
def upper_i_word_test_cases():
    return [
        ("This is a normal text", "This is a normal text"),
        ("I created this review", "I created this review"),
        ("i created this review", "I created this review"),
        ("Pros: i. first review. ii. second review", "Pros: i. first review. ii. second review"),
    ]


@pytest.fixture
def lower_letter_sequence_caps_test_cases():
    return [
        ("This is a normal text", "This is a normal text"),
        ("THIS IS A NORMAL TEXT", "this is A normal text"), # The letter 'A' should stay in uppercase
        ("ThIS iS AnOtHeR TeST", "This iS AnOtHeR Test"),
        ("This is a test WITH SEQUENCE", "This is a test with sequence"),
        ("NoUpperCase", "NoUpperCase"),
        ("UPPER CASE lower case", "upper case lower case"), 
        ("ClassName", "ClassName"),
        ("AcronymAAA", "Acronymaaa"),
        ("AaBbCcDd", "AaBbCcDd"), 
    ]


@pytest.fixture
def handle_time_format_test_cases():
    return [
        ("This is a normal text", "This is a normal text"),
        ("Meeting at 9:30", "Meeting at 9.30"),  # Replace time format hh:mm with hh.mm
        ("Lunch at 12:00 PM", "Lunch at 12.00 PM"),  # Replace time format hh:mm with hh.mm
        ("Dinner at 18:45", "Dinner at 18.45"),  # Replace time format hh:mm with hh.mm
        ("Time ranges: 10:00-11:30 and 14:00-16:30", "Time ranges: 10.00-11.30 and 14.00-16.30"),  # Replace multiple time formats hh:mm with hh.mm
        ("No time format here", "No time format here"),  # No time format present
        ("Invalid time format 25:00", "Invalid time format 25.00"),  # Invalid time format, should not be replaced
        ("Time format without minutes 7:00", "Time format without minutes 7.00"),  # Replace time format hh:mm with hh.mm
        ("No minutes 10: and 20:", "No minutes 10: and 20:"),  # No minutes in the time format, should not be replaced
    ]




















