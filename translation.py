from transformers import pipeline

translator = pipeline(
    "translation",
    model="Helsinki-NLP/opus-mt-en-ur"
)

def translate_text(text):
    result = translator(text)
    return result[0]["translation_text"]