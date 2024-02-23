from googletrans import Translator

def translate_text(text, target_language):
    translator = Translator()
    translated_text = translator.translate(text, dest=target_language)
    return translated_text.text

if __name__ == "__main__":
    while True:
        input_text = input("Enter the text to translate (or 'quit' to exit): ")

        if input_text.lower() == "quit":
            break

        target_language = input("Enter the target language (e.g., 'es' for Spanish, 'fr' for French): ")

        translated_text = translate_text(input_text, target_language)
        print(f"Translation: {translated_text}")
