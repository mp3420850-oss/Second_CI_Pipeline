
def count_words(sentence):
    return len(sentence.split())


if __name__ == "__main__":
    sentence = input("Enter a sentence: ")
    print("Number of words:", count_words(sentence))
