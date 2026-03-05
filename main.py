def get_book_text(filepath):
    with open(filepath) as file:
    # open the file at given path
        return file.read()
        # read it and give back the entire contents as one long string
    

def count_words(text):
    # split contents into a list of words on whitespace(no argument), then count them
    num_words = len(text.split())
    return num_words
    

def main():
    # store the location of our file in a variable
    path = "books/frankenstein.txt"
    # call our function, use the path, and save the result in 'text'
    text = get_book_text(path)
    # call count_words on the content and store the returned word count
    num_words = count_words(text)
    print(f"Found {num_words} total words")

    # print(text) - output the contents to the console

main()