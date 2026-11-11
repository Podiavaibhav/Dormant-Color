import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from collections import Counter

# Step 1: Load the image
image_path = '/Users/vaibhav/Desktop/0_9H74uSINU-qGHWz5.jpg'
image = cv2.imread(image_path)

if image is None:
    raise FileNotFoundError(f"Could not load image: {image_path}")

# Step 2: Convert BGR to RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Step 3: Reshape image into RGB pixel data
pixels = image_rgb.reshape((-1, 3))
print(f"Pixel data shape: {pixels.shape}")

# Step 4: Apply K-Means clustering
num_colors = 5
kmeans = KMeans(n_clusters=num_colors, random_state=42)
kmeans.fit(pixels)

# Step 5: Extract cluster centers
colors = kmeans.cluster_centers_.astype(int)

# Step 6: Count pixels belonging to each cluster
counts = Counter(kmeans.labels_)
sorted_counts = counts.most_common()

# Step 7: Display ranked dominant colors
total_pixels = len(pixels)

print("\nDominant colors ranked by pixel count:\n")

for rank, (cluster_idx, count) in enumerate(sorted_counts, start=1):
    color = colors[cluster_idx]
    percentage = (count / total_pixels) * 100
    hex_color = '#{:02X}{:02X}{:02X}'.format(*color)

    print(
        f"{rank}. RGB: {tuple(color)} | "
        f"HEX: {hex_color} | "
        f"Pixels: {count:,} | "
        f"Percentage: {percentage:.2f}%"
    )

# Step 8: Display original image and dominant color palette
fig, (ax_image, ax_palette) = plt.subplots(
    2, 1,
    figsize=(10, 8),
    gridspec_kw={'height_ratios': [5, 1]}
)

ax_image.imshow(image_rgb)
ax_image.set_title("Original Image")
ax_image.axis('off')

start = 0

for cluster_idx, count in sorted_counts:
    color = colors[cluster_idx]
    percentage = count / total_pixels

    rgb_color = tuple(float(channel) / 255 for channel in color)

    ax_palette.barh(
        0,
        percentage,
        left=start,
        height=0.8,
        color=rgb_color
    )

    start += percentage

ax_palette.set_xlim(0, 1)
ax_palette.set_ylim(-0.6, 0.6)
ax_palette.set_title("Dominant Color Palette")
ax_palette.axis('off')

plt.tight_layout()
plt.savefig("results/dominant_color_extraction.png", dpi=200, bbox_inches="tight")
plt.show()
