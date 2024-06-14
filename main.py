def main():
    path = "books/frankenstein.txt"
    file_contents = get_book_text(path)
    words_count = get_words_count(file_contents)
    char_count = get_char_count(file_contents)
    print_report(char_count, path, words_count)
        
def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_words_count(text):
    words = text.split()
    return len(words)
    
def get_char_count(text):
    char_dict = {}
    for word in text:
        lowered = word.lower()
        if lowered in char_dict:
            char_dict[lowered] += 1
        else:
            char_dict[lowered] = 1
    return char_dict

def print_report(char_dict, path, words_count):
    print(f"--- Begin report {path} ---")
    print(f"{words_count} words found in the document")
    for key in char_dict:
        print(f"The \'{key}\' character was found {key[0]} times")
    print("--- End report ---")
        
        
main()