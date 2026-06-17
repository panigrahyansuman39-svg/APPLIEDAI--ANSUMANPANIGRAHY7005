from transformers import pipeline

# Load Fill-Mask pipeline
fill_mask = pipeline(
    "fill-mask",
    model="bert-base-uncased"
)

# Sentence with a missing word
text = "Python is a [MASK] programming language."

# Predict the masked word
results = fill_mask(text)

# Print top predictions
for result in results:
    print(f"Prediction: {result['token_str']}")
    print(f"Score: {result['score']:.4f}")
    print(f"Sentence: {result['sequence']}")
    print("-" * 50)