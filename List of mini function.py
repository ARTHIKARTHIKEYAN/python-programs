# Example: Using the min() function with a key function
words = ["apple", "banana", "orange", "kiwi", "strawberry"]

min_length_word = min(words, key=len)

print("Shortest word in the list:", min_length_word)
