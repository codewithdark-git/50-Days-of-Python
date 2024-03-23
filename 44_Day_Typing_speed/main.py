import streamlit as st
import time
import random

def calculate_typing_speed(text, start_time, end_time):
    words_typed = len(text.split())
    time_taken = end_time - start_time
    words_per_minute = (words_typed / time_taken) * 60
    return words_per_minute

def display_sentence():
    sentences = [
        "The quick brown fox jumps over the lazy dog",
        "How much wood would a woodchuck chuck if a woodchuck could chuck wood",
        "The rain in Spain falls mainly on the plain",
        "To be or not to be, that is the question",
        "All that glitters is not gold"
    ]
    return random.choice(sentences)

def main():
    st.title("Typing Speed Test")

    st.write("Type the following sentence:")

    sentence = display_sentence()
    st.write(sentence)

    st.write("Press Enter when you are ready to start typing...")

    start_time = st.time_input("Start time")
    user_input = st.text_input("Type the sentence here:")
    end_time = st.time_input("End time")

    if user_input:
        speed = calculate_typing_speed(user_input, start_time, end_time)
        st.write(f"Your typing speed is approximately {speed:.2f} words per minute.")

        accuracy = (len(user_input) / len(sentence)) * 100
        st.write(f"Accuracy: {accuracy:.2f}%")

if __name__ == "__main__":
    main()
