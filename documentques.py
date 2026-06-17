from transformers import pipeline
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

qa_pipeline = pipeline(
    "document-question-answering",
    model="impira/layoutlm-document-qa"
)

image = Image.open(
    r"C:\Users\user\Downloads\Applied Ai\PYTHON-COMPLETE-TUTORIAL\shoppingreceipt.jpg"
)

result = qa_pipeline(
    image=image,
    question="What is the total amount?"
)

print("Answer:")
print(result)