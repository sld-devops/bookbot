def get_num_words(text):
    num_words = len(text.split())
    return num_words


def get_num_words(text):
    # split contents into a list of words on whitespace(no argument)
    num_words = len(text.split())
    return num_words

def get_char_appearance(text):
    seen_counts = {}
    for char in text:
        char = char.lower()
        if char not in seen_counts:
            seen_counts[char] = 0
        seen_counts[char] += 1
    return seen_counts
