import cv2
import numpy as np
import matplotlib.pyplot as plt

def compute_histogram(image):
    """Compute the histogram of an image."""
    hist = cv2.calcHist([image], [0], None, [256], [0, 256])
    return hist

def plot_histograms(original_hist, decrypted_hist):
    """Plot the histograms for comparison."""
    plt.figure(figsize=(12, 6))
    
    plt.subplot(1, 2, 1)
    plt.title("Original Image Histogram")
    plt.plot(original_hist, color='blue')
    plt.xlim([0, 256])
    
    plt.subplot(1, 2, 2)
    plt.title("Decrypted Image Histogram")
    plt.plot(decrypted_hist, color='green')
    plt.xlim([0, 256])
    
    plt.tight_layout()
    plt.show()

# Load the images
original_image_path = r'C:\Users\swath\.vscode\power.jpg'  # Replace with your original image path
decrypted_image_path = r'C:\Users\swath\.vscode\output\decrypted_image.png'  # Replace with your decrypted image path

original_image = cv2.imread(original_image_path, cv2.IMREAD_GRAYSCALE)  # Load as grayscale
decrypted_image = cv2.imread(decrypted_image_path, cv2.IMREAD_GRAYSCALE)

# Compute histograms
original_hist = compute_histogram(original_image)
decrypted_hist = compute_histogram(decrypted_image)

# Normalize histograms
original_hist = original_hist / original_hist.sum()
decrypted_hist = decrypted_hist / decrypted_hist.sum()

# Plot histograms
plot_histograms(original_hist, decrypted_hist)

