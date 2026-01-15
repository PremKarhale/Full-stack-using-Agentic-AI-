def clean_text(text):
    cleaned_text=text.lower().strip()
    return cleaned_text

def is_long_prompt(text):
    if len(text)>20:
        return True
    return False

