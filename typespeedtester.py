import random
import time

def randomtext(length):
    charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return ''.join(random.choice(charset) for _ in range(length))

def cwpm(start_time, end_time, typed_characters):
    minutes = (end_time - start_time) / 60.0
    words = typed_characters / 5.0  # Assuming an average word length of 5 characters
    return int(words / minutes)

def main():
    random.seed(time.time())

    print("Welcome to Typing Speed Tester!")

    text_length = 100  # You can adjust the length of the text
    random_text = randomtext(text_length)

    print(f"Type the following:\n{random_text}")

    start_time = time.time()

    user_input = input("Your typing: ")

    end_time = time.time()

    # Count the number of characters in the typed text
    typed_characters = sum(1 for char in user_input if 'A' <= char <= 'z')

    wpm = cwpm(start_time, end_time, typed_characters)
    print(f"Typing speed: {wpm} WPM")

if __name__ == "__main__":
    main()
