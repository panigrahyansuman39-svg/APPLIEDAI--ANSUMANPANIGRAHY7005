from transformers import pipeline
summary=pipeline("summarization",model="facebook/bart-large-cnn")
text="my self ansuman panigrahy i am currewntly pursuing internship at gp bbsr"
summ=summary(text)
print(summ)