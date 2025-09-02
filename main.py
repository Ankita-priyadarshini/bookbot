import sys
from stats import get_num_words, get_book_text, char_count, sort_char_counts

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")

    total_words = get_num_words(text)
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")

    counts = char_count(text)
    sorted_counts = sort_char_counts(counts)

    print("--------- Character Count -------")
    for entry in sorted_counts:
        print(f"{entry['char']}: {entry['num']}")

    print("============= END ===============")


if __name__ == "__main__":
    main()
