from PIL import Image
import matplotlib.pyplot as plt

original = Image.open(
    r"C:\Users\user\Downloads\Applied Ai\PYTHON-COMPLETE-TUTORIAL\Screenshot 2026-06-06 092557.png"
)

depth = Image.open("depth_map.png")

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(original)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(depth, cmap="gray")
plt.title("Depth Map")
plt.axis("off")

plt.show()