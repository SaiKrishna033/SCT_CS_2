import os
from PIL import Image

def encrypt_image(image_path, key):
    try:
        image = Image.open(image_path)
        pixels = list(image.getdata())

        # Encrypt the pixels by adding the key value (modulo 256 for wrapping)
        encrypted_pixels = [(pixel[0] + key) % 256, (pixel[1] + key) % 256, (pixel[2] + key) % 256 for pixel in pixels]

        # Create a new image with the encrypted pixels
        encrypted_image = Image.new(image.mode, image.size)
        encrypted_image.putdata(encrypted_pixels)

        return encrypted_image
    except Exception as e:
        print(f"Error loading image: {e}")
        return None

def save_image(image, save_path):
    try:
        image.save(save_path)
        print(f"Image saved to {save_path}")
    except Exception as e:
        print(f"Error saving image: {e}")

if __name__ == "__main__":
    # Get user input for paths and key
    image_path = input("Enter the path to the image: ")
    save_path = input("Enter the path to save the encrypted image: ")
    key = int(input("Enter the encryption key (an integer): "))

    # Encrypt the image
    encrypted_image = encrypt_image(image_path, key)

    if encrypted_image:
        # Save the encrypted image
        save_image(encrypted_image, save_path)
