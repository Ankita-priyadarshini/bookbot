def get_book_text(url):
    file_content = ""
    with open(url) as f:
        file_content = f.read()
    return file_content

def get_num_words(content):
    list_of_words = content.split()
    return len(list_of_words)

def char_count(text) -> dict[str, int]:
    counts = {}
    for ch in text.lower():
        if ch in counts:
            counts[ch] += 1
        else:
            counts[ch] = 1
    return counts

def sort_char_counts(counts) -> list[dict[str, int]]:
    char_list = []
    for ch, num in counts.items():
        if ch.isalpha():
            char_list.append({"char": ch, "num": num})

    char_list.sort(key=lambda x: x["num"], reverse=True)
    return char_list