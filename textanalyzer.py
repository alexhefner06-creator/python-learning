print("=== TEXT ANALYZER ===")
sentence = input("Enter a sentence: ")
print("--- Analysis Results ---")
total_chars_with_spaces = len(sentence)
total_chars_without_spaces = len(sentence.replace(" ", ""))
words = sentence.split()
num_words = len(words)
vowels = "aeiou"
vowel_count = 0
for char in sentence.lower():
    if char in vowels:
        vowel_count += 1
uppercase_version = sentence.upper()
lowercase_version = sentence.lower()
reversed_sentence = sentence[::-1]
starts_with_capital = sentence[0].isupper() if sentence else False
ends_with_punctuation = sentence.endswith((".", "!", "?"))
print(f"Total characters (with spaces): {total_chars_with_spaces}")
print(f"Total characters (without spaces): {total_chars_without_spaces}")
print(f"Number of words: {num_words}")
print(f"Number of vowels: {vowel_count}")
print(f"Uppercase version: {uppercase_version}")
print(f"Lowercase version: {lowercase_version}")
print(f"Reversed: {reversed_sentence}")
print(f"Starts with capital: {'Yes' if starts_with_capital else 'No'}")
print(f"Ends with punctuation: {'Yes' if ends_with_punctuation else 'No'}")