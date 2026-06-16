from transformers import pipeline

ner = pipeline(
    "ner",
    model="dslim/bert-base-NER",
    aggregation_strategy="simple"
)

text="ansuman lives in odisha and he is a student"

result = ner(text)

for entity in result:
    print(entity)