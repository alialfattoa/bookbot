def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def num_words(text):
    text_list = text.split()
    return len(text_list)
    

def count_charachters(text_file):
    char_list=[]
    char_count=[]
    final_char_count={}
    words_list=text_file.split()
    for elem in words_list:
        for char in elem:
            char = char.lower()
            char_list.append(char)

    for chars in char_list:
        if chars in final_char_count:
            final_char_count[chars] += 1
        else:
            final_char_count[chars] = 1
    return final_char_count

def list_sort(chars_dictionary):
    chars_dictionary.sort(reverse=True, key=sort_on)
    print(chars_dictionary)
    pass

def print_report(filepath, text, word_count, final_char_count):
    print("============ BOOKBOT ============")

    print(f"Analyzing book found at {filepath}...")

    print("--------- Word Count -------")
    print(f"Found {word_count} total words")

    print("--------- Character Count -------")
    for char, count in final_char_count.items():
        print(f"{char}: {count}")
        
    print("============= END ===============")
    pass



