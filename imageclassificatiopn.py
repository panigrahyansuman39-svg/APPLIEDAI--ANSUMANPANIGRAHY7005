from transformers import pipeline
from PIL import Image#PIL (Pillow) is a Python library used to open, edit, process, and save image files. 🖼️🐍

# Load image classification pipeline
classifier = pipeline(
    "image-classification",
    model="google/vit-base-patch16-224"
)

# Open image
image = Image.open(r"C:\\Users\\user\Downloads\Applied Ai\\PYTHON-COMPLETE-TUTORIAL\\Honey_Badger.jpg")

# Classify image
result = classifier(image)

# Print top predictions
for item in result:
    print(f"Label: {item['label']}")
    print(f"Score: {item['score']:.4f}")
    print("-" * 30)