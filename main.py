from stats import get_num_words, get_characters_count, sort_dictionary
import sys

def get_book_text(file_path):
    with open(file_path) as file:
        return file.read()


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    file_contents = get_book_text(book_path)
    num_words = get_num_words(file_contents)
    chars_dict = get_characters_count(file_contents)
    sort_dict = sort_dictionary(chars_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dict in sort_dict:
        print(f"{dict['char']}: {dict['count']}")

main()
