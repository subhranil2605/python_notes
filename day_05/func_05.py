def text_embedding(text: str):

    def _clean_text(text):
        return text.strip()

    final_text = _clean_text(text)
    return final_text

print(text_embedding("    Rutuja    "))