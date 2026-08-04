import streamlit as st

from sentiment import analyze_sentiment
from text_generation import generate_text
from question_answering import answer_question
from summarization import summarize_text
from ner import extract_entities
from translation import translate_text

st.set_page_config(
    page_title="NLP Transformer System",
    page_icon="🤖"
)

st.title("🤖 NLP Transformer System")
st.write("Transformer-based NLP Application")

task = st.sidebar.selectbox(
    "Select Task",
    [
        "Sentiment Analysis",
        "Text Generation",
        "Question Answering",
        "Text Summarization",
        "Named Entity Recognition",
        "Language Translation"
    ]
)

# ----------------------------------
# Sentiment Analysis
# ----------------------------------

if task == "Sentiment Analysis":

    st.header("😊 Sentiment Analysis")

    text = st.text_area(
        "Enter Text"
    )

    if st.button("Analyze Sentiment"):

        if text.strip() == "":
            st.warning("Please enter some text.")
        else:

            result = analyze_sentiment(text)

            st.success(
                f"Sentiment: {result['label']}"
            )

            st.write(
                f"Confidence: {result['score']:.4f}"
            )

# ----------------------------------
# Text Generation
# ----------------------------------

elif task == "Text Generation":

    st.header("✍️ Text Generation")

    prompt = st.text_area(
        "Enter Prompt"
    )

    if st.button("Generate Text"):

        if prompt.strip() == "":
            st.warning("Please enter a prompt.")
        else:

            generated_text = generate_text(prompt)

            st.subheader("Generated Text")

            st.write(generated_text)

# ----------------------------------
# Question Answering
# ----------------------------------

elif task == "Question Answering":

    st.header("❓ Question Answering")

    context = st.text_area(
        "Enter Context"
    )

    question = st.text_input(
        "Enter Question"
    )

    if st.button("Get Answer"):

        if context.strip() == "" or question.strip() == "":
            st.warning("Please enter both context and question.")
        else:

            answer = answer_question(
                question,
                context
            )

            st.subheader("Answer")

            st.success(answer)

# ----------------------------------
# Text Summarization
# ----------------------------------

elif task == "Text Summarization":

    st.header("📝 Text Summarization")

    text = st.text_area(
        "Enter Long Text"
    )

    if st.button("Generate Summary"):

        if text.strip() == "":
            st.warning("Please enter some text.")
        else:

            summary = summarize_text(text)

            st.subheader("Summary")

            st.success(summary)

# ----------------------------------
# Named Entity Recognition
# ----------------------------------

elif task == "Named Entity Recognition":

    st.header("🏷️ Named Entity Recognition (NER)")

    text = st.text_area(
        "Enter Text"
    )

    if st.button("Extract Entities"):

        if text.strip() == "":
            st.warning("Please enter some text.")
        else:

            entities = extract_entities(text)

            st.subheader("Detected Entities")

            if len(entities) == 0:
                st.info("No entities found.")
            else:

                for entity in entities:

                    st.write(
                        f"**{entity['word']}** → {entity['entity_group']}"
                    )

# ----------------------------------
# Language Translation
# ----------------------------------

elif task == "Language Translation":

    st.header("🌐 Language Translation")

    text = st.text_area(
        "Enter English Text"
    )

    if st.button("Translate Text"):

        if text.strip() == "":
            st.warning("Please enter some text.")
        else:

            translated_text = translate_text(text)

            st.subheader("Translated Text")

            st.success(translated_text)