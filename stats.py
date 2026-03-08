def get_num_words(text):
    # split contents into a list of words on whitespace(no argument)
    num_words = len(text.split())
    return num_words

def get_char_appearance(text):
    seen_counts = {}
    for char in text:
        # count upper and lower case chars together
        char = char.lower()
        # create new key if the char appears for first time
        if char not in seen_counts:
            seen_counts[char] = 0
        # if it has been already seen, count + 1
        seen_counts[char] += 1
    # give back whole dict when the content is over (all iterations done)
    return seen_counts

def sort_on(seen_counts):
    return seen_counts["num"]

def get_sorted_count(seen_counts):
    # create list to append dict with keys later
    sorted_chars = []
    # take each char (they are already keys)
    for char in seen_counts:
        # take the count for each char (key)
        count = seen_counts[char]
        # build a dict of the key pairs, add each dict to list
        sorted_chars.append({"char": char, "num": count})
    # after loop, using helper, rearrange the list by "num" key, but make it reverse (originally it's not)
    sorted_chars.sort(key=sort_on, reverse=True)
    # give back sorted list with 2 keys into dict
    return sorted_chars
