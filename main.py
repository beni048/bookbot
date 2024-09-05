def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print("--- Begin report of books/frankenstein.txt ---")
        num_words = count_words(file_contents)
        print(f"{num_words} words found in the document\n")
        char_counts = count_chars(file_contents)
        sorted_char_counts = dict(sorted(char_counts.items(), key=lambda item: item[1], reverse=True))
        for char, num in sorted_char_counts.items():
            print(f"The '{char}' character was found {num} times")
        print("--- End report ---")

def count_words(text):
    return len(text.split())

def count_chars(text):
    char_count = {}
    for char in text.lower():
        if char.isalpha():
            # If the character is already in the dictionary, increment its count
            if char in char_count:
                char_count[char] += 1
            # Otherwise, initialize the count for this character to 1
            else:
                char_count[char] = 1
    return char_count

def sort_on(dict):
    return dict["num"]


main()