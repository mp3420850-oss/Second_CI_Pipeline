
import string

def is_pangram(sentence):
    letters = set(sentence.lower())
    return set(string.ascii_lowercase).issubset(letters)


if __name__ == "__main__":
    sentence = input("Enter a sentence: ")
    if is_pangram(sentence):
        print("Pangram")
    else:
        print("Not Pangram")
