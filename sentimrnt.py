from transformers import pipeline
classifier=pipeline("sentiment-analysis")
result=classifier("i dont like ml")
print(result)