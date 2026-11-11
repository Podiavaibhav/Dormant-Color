import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from collections import Counter
import os

# STEP 1: Load the image
image_path = '/Users/vaibhav/Desktop/0_9H74uSINU-qGHWz5.jpg'  # Change this to image path
if not os.path.exists(image_path):
    raise FileNotFoundError(f"Image file not found: {image_path}")

image = cv2.imread(image_path)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
pixels = image_rgb.reshape((-1, 3))

plt.imshow(image_rgb)
plt.title("Original Image")
plt.axis('off')
plt.show()


# STEP 2: Cluster the colors
num_colors = 5
kmeans = KMeans(n_clusters=num_colors, random_state=42)
kmeans.fit(pixels)
colors = kmeans.cluster_centers_.astype(int)
labels = kmeans.labels_

# STEP 3: Count how many pixels belong to each cluster
counts = Counter(labels)
sorted_counts = counts.most_common()

# STEP 4: Show the dominant colors
print("Dominant colors (most to least):")
for i, (cluster_idx, count) in enumerate(sorted_counts):
    rgb = colors[cluster_idx]
    print(f"{i + 1}. RGB: {rgb}, Pixels: {count}")


# STEP 5: Visualize color palette
def plot_color_palette(sorted_counts, colors):
    palette = []
    total = sum(count for _, count in sorted_counts)

    for cluster_idx, count in sorted_counts:
        rgb = colors[cluster_idx]
        percent = count / total
        palette.append((rgb, percent))

    plt.figure(figsize=(8, 2))
    start = 0
    for rgb, percent in palette:
        end = start + percent
        plt.fill_between([start, end], 0, 1, color=np.array(rgb) / 255)
        start = end

    plt.axis('off')
    plt.title("Dominant Color Palette")
    plt.show()


plot_color_palette(sorted_counts, colors)
