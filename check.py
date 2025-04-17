from words import abusive_words

def detch_abuse(text):
    return " ".join(
        '*' * len(word) if word.lower() in abusive_words else word
        for word in text.split()
    )

def chat():
    while True:
        user_text = input("User: ")
        if user_text.lower() in ['exit', 'quit']:
            print("Exiting chat.")
            break
        print("Echo:", detch_abuse(user_text), "\n")

chat()
