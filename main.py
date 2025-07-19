import sys
from stats import char_counting, word_count, sort_dict

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    #check if the correct number of arguments was passed
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")

    # Get text from file
    text = get_book_text(book_path)
    num_words = word_count(text)

    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    #Getting the character count
    print("--------- Character Count -------")
    characters_count = char_counting(text)
    sorted_countdown = sort_dict(characters_count)

    for char, count in sorted_countdown:
        if char.isalpha():
            print(f"{char}: {count}")

    print("============= END ===============")


main()
