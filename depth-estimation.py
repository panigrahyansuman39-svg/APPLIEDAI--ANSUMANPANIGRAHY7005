from transformers import pipeline
from PIL import Image#PIL (Pillow) is a Python library used to open, edit, process, and save image files. 🖼️🐍
print("Loading model...")

pipe = pipeline(
    "depth-estimation",
    model="LiheYoung/depth-anything-small-hf"
)
print("Opening image...")

image = Image.open(
    r"C:\Users\user\Downloads\Applied Ai\PYTHON-COMPLETE-TUTORIAL\Screenshot 2026-06-06 092557.png"
)

print("Running depth estimation...")

result = pipe(image)

print("Saving depth map...")

result["depth"].save("depth_map.png")

print("Done! Depth map saved as depth_map.png")