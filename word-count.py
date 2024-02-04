from collections import Counter
import string


def count_words(path, most_frequent):
    file_path = path
    with open(file_path) as file:
        text = file.read()

    word_counts = Counter(text.lower().translate(str.maketrans('', '', string.punctuation)).split()).most_common(most_frequent)

    print('')
    print(f"Top {most_frequent} most frequent words:")
    for i, (word, count) in enumerate(word_counts, start=1):
        print(f"{i}. {word}: {count} occurrences")
    print()


i_path = input('Enter the path to the text file: ')
i_N = int(input('Enter the number of top words to display: '))
count_words(i_path, i_N)
