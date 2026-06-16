from transformers import pipeline
generator=pipeline("text-generation",model='gpt2')
result=generator(
    "whats the capital of india",
    max_length=10
)
print(result)