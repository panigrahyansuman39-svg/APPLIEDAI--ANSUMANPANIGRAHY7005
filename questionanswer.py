from transformers import pipeline

qa = pipeline("question-answering")

result = qa(
    question="What is the capital of India?",
    context="India is a country in South Asia. Its capital is New Delhi."
)

print(result["answer"])