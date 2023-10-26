def print_upper_words1(words):
    """Takes an list of words and converts them to uppercase."""

    for word in words:
        print(word.upper())

print(print_upper_words1(['hello', 'dog', 'cat', 'car']))


def print_upper_words2(words):
    """Takes a list of words and checks to see if they start
    with 'e', then converts those ones to uppercase."""
    
    for word in words:
        if word.startswith('e'):
            print(word.upper())

print(print_upper_words2(['elephant', 'house', 'car', 'ear']))



def print_upper_words3(words, must_start_with):
    """Takes a list of words and an object with letters.
    If the words start with those letters, they will be
    printed."""

    for word in words:
   
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())




print(print_upper_words3(["hello", "hey", "goodbye", "yo", "yes"],
                         must_start_with={"h", "y"}))

print(print_upper_words3(["apple", "orange", "banana", "apricot", "blueberry"],
                         must_start_with={"a", "b"}))
