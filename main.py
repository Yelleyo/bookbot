def main(file_path):
    word_count = count_words(file_path)
    char_count = dict()
    char_count = count_characters(file_path)
    print(f'--- Begin report of {file_path} ---\n {word_count} words found in the document \n')
    for key, value in char_count.items():
        print(f"The '{key}' character was found {value} times")
    print('--- End report ---')


def get_file(file_path):
    with open(file_path) as f:
        file_content = f.read()
        return file_content

def print_file(file_path):
    file_content = get_file(file_path)
    print(file_content)

def count_words(file_path):
    file_content = get_file(file_path)
    words = file_content.split()
    words_count = len(words)
    return words_count

def count_characters(file_path):
    file_content = get_file(file_path)
    file_content = file_content.lower()
    char_count = dict()
    for char in file_content:
        if char.isalnum():
            char_count[char] = char_count.get(char, 0) + 1
    return char_count

# print_file()
# count_words("books/frankenstein.txt")
# count_characters()
main("books/frankenstein.txt")