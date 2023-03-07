def change_string(in_string: str, change_char: str, replace_char: str) -> str:
    words = in_string.split()
    new_words = []
    for word in words:
        new_words.append(word.replace(change_char,replace_char,1))
    return " ".join(new_words)

if __name__ == "__main__":
    my_string = "distilling instilling fulfilling"
    new_string = change_string(my_string, "i", "*")
    print(new_string)