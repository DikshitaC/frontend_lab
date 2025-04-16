from collections import Counter

def most_frequent_words(filename):
    with open(filename, 'r') as file:
        text = file.read().split()
    word_counts = Counter(text)
    for word, count in word_counts.most_common(10):
        print(f"{word}: {count}")

most_frequent_words('textfile.txt')
