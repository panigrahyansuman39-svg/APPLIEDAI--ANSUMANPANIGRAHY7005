from google import genai
client=genai.Client(api_key="AQ.Ab8RN6ISHG2DJObSVN1NozBjYWfLLroQD9Fh8-YBXQNx0uuSYw")
while True:
    question=input("you:")
    if question.lower()=="exit":
        print("Goodbye")
        break
    response=client.models.generate_content(
        model="gemini-2.5-flash",
        contents=question
    )
    print("Gemini:",response.text)