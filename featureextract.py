from transformers import pipeline
import numpy as np

extractor = pipeline(
    "feature-extraction",
    model="distilbert-base-uncased"
)
text = """
I love Python programming because it is easy to learn,
powerful for data analysis, machine learning, web development,
automation, and artificial intelligence applications.
"""
result = extractor(text)

arr = np.array(result)

print("Shape:", arr.shape)