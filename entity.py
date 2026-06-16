from transformers import pipeline
ansu = pipeline("ner", model="dslim/bert-base-NER")
text="ansuman lives in odisha and he is a student"
result=ansu(text)
print(result)