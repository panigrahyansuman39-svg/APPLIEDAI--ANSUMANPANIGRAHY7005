from transformers import pipeline
from PIL import Image

# Load feature extraction pipeline
extractor = pipeline(
    "image-feature-extraction",
    model="google/vit-base-patch16-224"
)

# Load image
image = Image.open(
    r"C:\\Users\\user\\Downloads\\Applied Ai\\PYTHON-COMPLETE-TUTORIAL\\Honey_Badger.jpg"
)

# Extract features
features = extractor(image)

print("Images:", len(features))
print("Tokens:", len(features[0]))
print("Features per token:", len(features[0][0]))