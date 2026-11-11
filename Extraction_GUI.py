import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from collections import Counter
import tkinter as tk
from tkinter import filedialog, messagebox
import os


def select_image():
    file_path = filedialog.askopenfilename(
        title="Select Image",
        filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp")]
    )

    if not file_path:
        return

    try:
        # Load and process image
        image = cv2.imread(file_path)
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        pixels = image_rgb.reshape((-1, 3))

        plt.imshow(image_rgb)
        plt.title("Original Image")
        plt.axis('off')
        plt.show()

        # Run KMeans clustering
        num_colors = 5
        kmeans = KMeans(n_clusters=num_colors, random_state=42)
        kmeans.fit(pixels)
        colors = kmeans.cluster_centers_.astype(int)
        labels = kmeans.labels_

        # Count frequency of each color cluster
        counts = Counter(labels)
        sorted_counts = counts.most_common()

        # Show palette
        plot_color_palette(sorted_counts, colors)

    except Exception as e:
        messagebox.showerror("Error", str(e))



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


# Set up basic GUI window
root = tk.Tk()
root.title("Dominant Color Picker")
root.geometry("300x150")

label = tk.Label(root, text="Pick an image to extract dominant colors:")
label.pack(pady=10)

browse_button = tk.Button(root, text="Browse Image", command=select_image)
browse_button.pack()

root.mainloop()
