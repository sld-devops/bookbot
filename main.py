def get_book_text(filepath):
    with open(filepath) as s:
    # Use 'with' to open the file at that path; 's' represents the open file
        return s.read()
        # Read the file's contents into a string and return it
    
def main():
    path = "books/frankenstein.txt"
    # Store the location of our file in a variable
    text = get_book_text(path)
     # Call our function, passing the path, and save the result in 'text'
    print(text)
    # Output the text to the console
    
main()