def get_book_text(path_to_file):
    """
    Reads the content of a book file and returns it as a string.
    
    :param path_to_file: The path to the book file.
    :return: The content of the book file as a string.
    """

    with open(path_to_file) as f:
        file_contents = f.read()

    return file_contents

def number_of_words(text):
    """
    Counts the number of words in a given text.
    
    :param text: The text to count words in.
    :return: The number of words in the text.
    """
    return len(text.split())    

def main():
    """
    Main function to execute the script.
    """
    path_to_file = '/Users/eitanhalfon/bookbot/books/frankenstein.txt'
    book_text = get_book_text(path_to_file)
    print(book_text)
    print(f"{number_of_words(book_text)} words found in the document")

if __name__ == "__main__":
    main()
# main.py