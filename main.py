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


# En esta funcion primero me fijo que los caracteres sean alfabeticos. Si lo son, los agrego en un diccionario con su letra y cantidad.
# Despues los ordeno de mayor a menor y los imprimo de acuerdo al formato. La funcion lambda es la encargada de detectar esos valores y como esta en el key del sort, se basa en eso para el ordenamiento.


def print_report(char_dict, path, words_count):
    char_list = []
    print(f"--- Begin report {path} ---")
    print(f"{words_count} words found in the document")
    for char in char_dict:
        if char.isalpha():
            char_list.append({"char":char, "count":char_dict[char]})
    
    char_list.sort(key=lambda x: x["count"], reverse=True)
    for item in char_list:
        print(f"The \'{item["char"]}\' character was found {item["count"]} times")

    print("--- End report ---")
        
        
main()