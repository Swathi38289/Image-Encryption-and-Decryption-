import numpy as np
from PIL import Image
from scipy.stats import chisquare
from skimage.metrics import peak_signal_noise_ratio as psnr

def load_image(image_path):
    """Load an image from the specified path."""
    return Image.open(image_path)

def calculate_histogram(image):
    """Calculate the histogram of an image."""
    gray_image = image.convert('L')
    histogram, _ = np.histogram(np.array(gray_image).flatten(), bins=256, range=(0, 256))
    return histogram

def calculate_entropy(image):
    """Calculate the entropy of an image."""
    histogram = calculate_histogram(image)
    histogram = histogram[histogram > 0]  # Avoid log(0)
    probabilities = histogram / histogram.sum()
    entropy = -np.sum(probabilities * np.log2(probabilities))
    return entropy

def calculate_correlation(original, encrypted):
    """Calculate the correlation between two images."""
    original_array = np.array(original).flatten()
    encrypted_array = np.array(encrypted).flatten()
    correlation = np.corrcoef(original_array, encrypted_array)[0, 1]
    return correlation

def calculate_npcr(original, encrypted):
    """Calculate the NPCR between two images."""
    original_array = np.array(original)
    encrypted_array = np.array(encrypted)
    diff = original_array != encrypted_array
    npcr = np.sum(diff) / (original_array.size) * 100
    return npcr

def calculate_uaci(original, encrypted):
    """Calculate the UACI between two images."""
    original_array = np.array(original)
    encrypted_array = np.array(encrypted)
    uaci = np.mean(np.abs(original_array - encrypted_array)) / 255 * 100
    return uaci

def chi_square_test(original_hist, encrypted_hist):
    """Perform the Chi-Square test between two histograms."""
    chi2_stat, p_value = chisquare(encrypted_hist, original_hist)
    return chi2_stat, p_value

def calculate_psnr(original, encrypted):
    """Calculate the PSNR between two images."""
    return psnr(np.array(original), np.array(encrypted))

# Load the images
original_image_path = r'C:\Users\swath\.vscode\power.jpg'  # Replace with your original image path
encrypted_image_path = r'C:\Users\swath\.vscode\output\decrypted_image.png'  # Replace with your encrypted image path

original_image = load_image(original_image_path)
encrypted_image = load_image(encrypted_image_path)

# Calculate metrics
entropy_original = calculate_entropy(original_image)
entropy_encrypted = calculate_entropy(encrypted_image)
correlation = calculate_correlation(original_image, encrypted_image)
npcr = calculate_npcr(original_image, encrypted_image)
uaci = calculate_uaci(original_image, encrypted_image)
psnr_value = calculate_psnr(original_image, encrypted_image)

# Calculate histograms for Chi-Square test
original_hist = calculate_histogram(original_image)
encrypted_hist = calculate_histogram(encrypted_image)

# Perform Chi-Square test
chi2_stat, p_value = chi_square_test(original_hist, encrypted_hist)

# Print the results
print(f"Entropy of Original Image: {entropy_original:.4f}")
print(f"Entropy of Encrypted Image: {entropy_encrypted:.4f}")
print(f"Correlation: {correlation:.4f}")
print(f"NPCR: {npcr:.4f}%")
print(f"UACI: {uaci:.4f}%")
print(f"PSNR: {psnr_value:.4f} dB")
print(f"Chi-Square Statistic: {chi2_stat:.4f}")
print(f"P-Value: {p_value:.4f}")

# Interpretation of the p-value
alpha = 0.05  # Significance level
if p_value < alpha:
    print("The distributions are significantly different (reject H0).")
else:
    print("The distributions are not significantly different (fail to reject H0).")




