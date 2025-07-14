import re
from googletrans import Translator, LANGUAGES

def remove_emoji(text):
    emoji_pattern = re.compile(
        "["
        "\U0001F600-\U0001F64F"  
        "\U0001F300-\U0001F5FF"  
        "\U0001F680-\U0001F6FF"  
        "\U0001F1E0-\U0001F1FF"  
        "\U00002702-\U000027B0"
        "\U000024C2-\U0001F251"
        "]+", flags=re.UNICODE
    )
    return emoji_pattern.sub(r'', text)

def get_language_code(language_name):
    for code, name in LANGUAGES.items():
        if name.lower() == language_name.lower():
            return code
    return None

def translate_text(text, target_language, emoji_pattern = False):
    translator = Translator()
    if emoji_pattern:
        cleaned_text = remove_emoji(text)
    else:
        cleaned_text = text
    code = get_language_code(target_language)
    if code:
        translated = translator.translate(cleaned_text, dest=code)
        return translated.text
    else:
        return "Language not supported."

if __name__ == "__main__":
    sample_text = "what is you name 🌍🚀😊"
    target_language = "french"
    translated_text = translate_text(sample_text, target_language)
    print(translated_text)  