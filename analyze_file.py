def count_words(path):
    with open(path, "r") as file:
        content = file.read()
        word_count = len(content.split())
        return word_count


def count_char(path):
    with open(path, "r") as file:
        content = file.read()
        char_count = len([*content])
        return char_count

def count_lines(path):
    with open(path, "r") as file:
        lines = (file.readline())
        return lines

path = ("C:\\Privater_Ordner\\Marlon_Bitiq\\Projects\\Python\\Challanges\\text_file.txt")
print("Word count: ")
print(count_words(path))

print("Character count: ")
print(count_char(path))

print("Character count: ")
print(count_lines(path))
