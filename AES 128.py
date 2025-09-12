from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os

def encrypt_image(image_path, key, output_path):
    cipher = AES.new(key, AES.MODE_CBC)
    iv = cipher.iv
    with open(image_path, 'rb') as img_file:
        image_data = img_file.read()

    encrypted_data = cipher.encrypt(pad(image_data, AES.block_size))
    
    # Save the encrypted image to the specified output path
    with open(output_path, 'wb') as enc_file:
        enc_file.write(iv + encrypted_data)

    return output_path

def decrypt_image(encrypted_image_path, key, output_path):
    with open(encrypted_image_path, 'rb') as enc_file:
        iv = enc_file.read(16)  # Read the IV
        encrypted_data = enc_file.read()

    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)

    # Save the decrypted image to the specified output path
    with open(output_path, 'wb') as out_file:
        out_file.write(decrypted_data)
    
    return output_path

# Usage
key = b'Sixteen byte key'  # 16 bytes key
image_path = r"C:\Users\swath\OneDrive\Documents\Downloads\power.jpg"  # Use raw string for the path

# Define output paths
encrypted_image_path = "./output/encrypted_image.aes"
decrypted_image_path = "./output/decrypted_image.png"

# Ensure the output directory exists
os.makedirs(os.path.dirname(encrypted_image_path), exist_ok=True)

# Encrypt the image
encrypt_image(image_path, key, encrypted_image_path)

# Decrypt the image
decrypt_image(encrypted_image_path, key, decrypted_image_path)

print(f'Encrypted image saved to: {encrypted_image_path}')
print(f'Decrypted image saved to: {decrypted_image_path}’)
