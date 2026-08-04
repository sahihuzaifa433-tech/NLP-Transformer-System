from transformers import pipeline

ner_pipeline = pipeline(
    "ner",
    aggregation_strategy="simple"
)

def extract_entities(text):

    results = ner_pipeline(text)

    return results