from collections import Counter
import string

def count_words(text):
    # Remove punctuation and convert to lowercase
    text = text.translate(str.maketrans("", "", string.punctuation)).lower()
    
    # Split the text into words
    words = text.split()

    # Count the occurrences of each word
    word_counts = Counter(words)

    return word_counts

def word_count_tool():
    print("Word Count Tool")
    input_text = input("Enter text: ")

    # Get word counts
    word_counts = count_words(input_text)

    # Display total word count
    total_words = sum(word_counts.values())
    print(f"\nTotal Words: {total_words}\n")

    # Display word frequencies
    print("Word Frequencies:")
    for word, count in word_counts.items():
        print(f"{word}: {count}")

if __name__ == "__main__":
    word_count_tool()
