from transformers import pipeline
ansu=pipeline("document-question-answering",model="google/flan-t5-base")
result=ansu("Question: what is the capital of india? Answer:")
print(result)