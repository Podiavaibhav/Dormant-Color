# Dominant Color Extraction using K-Means Clustering

A beginner computer vision project that uses **K-Means clustering**, an unsupervised machine learning algorithm, to identify and visualize the dominant colours in an image.

The project processes image pixels, groups similar colours into clusters, and generates a visual colour palette based on the frequency of each cluster.

## Overview

Images contain thousands or millions of individual pixels, each represented by RGB colour values. This project applies K-Means clustering to group pixels with similar colour characteristics and identify the most prominent colours in the image.

## How It Works

1. **Image Loading:** Reads an input image using OpenCV.
2. **Preprocessing:** Converts the image from BGR to RGB format and reshapes it into a two-dimensional array of pixel values.
3. **K-Means Clustering:** Groups pixels into a predefined number of colour clusters.
4. **Colour Extraction:** Retrieves the cluster centroids as representative colours.
5. **Frequency Analysis:** Counts the number of pixels assigned to each cluster and ranks the clusters by frequency.
6. **Palette Visualization:** Generates a colour palette using Matplotlib, with each colour's width proportional to its representation in the image.

## Technologies Used

- Python
- OpenCV
- NumPy
- Scikit-learn
- Matplotlib

## Installation

Clone the repository:

```bash
git clone https://github.com/Podiavaibhav/Dormant-Color.git
cd Dormant-Color
```

Install the required libraries:

```bash
pip install opencv-python numpy matplotlib scikit-learn
```

## Usage

1. Open `Color_extraction.py`.
2. Update the `image_path` variable with the location of your input image.
3. Set `num_colors` to specify the number of colour clusters.
4. Run the script:

```bash
python Color_extraction.py
```

The program displays the original image, prints the extracted colours and their pixel frequencies, and generates a visual colour palette.

## Algorithm

The project uses K-Means clustering to minimize the within-cluster sum of squared distances between pixel colour values and their assigned cluster centroids.

Each cluster centroid represents a dominant colour, while the number of assigned pixels determines its relative frequency in the image.

## Limitations

- The current implementation uses RGB Euclidean distance, which does not perfectly represent human colour perception.
- Processing every pixel can be computationally expensive for high-resolution images.
- The number of colour clusters must be specified before execution.
- The current implementation uses a locally configured image path.

## Learning Outcomes

- Understanding unsupervised machine learning through K-Means clustering.
- Working with image data and RGB pixel representations.
- Applying OpenCV for image processing.
- Analysing cluster distributions and visualizing extracted features.

---

**Project Type:** Beginner Computer Vision / Machine Learning  
**Status:** Initial implementation / Learning project
