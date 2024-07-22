from PIL import Image
import random
import os

def load_image(image_path):
    try:
        return Image.open(image_path)
    except Exception as e:
        print(f"Error loading image: {e}")
        return None

def save_image(image, output_path):
    try:
        image.save(output_path)
    except Exception as e:
        print(f"Error saving image: {e}")

def encrypt_image(image, key):
    pixels = list(image.getdata())
    width, height = image.size
    random.seed(key)

    # Swap pixel values
    for i in range(len(pixels)):
        swap_with = random.randint(0, len(pixels) - 1)
        pixels[i], pixels[swap_with] = pixels[swap_with], pixels[i]
    
    # Apply a basic mathematical operation
    encrypted_pixels = [( (pixel[0] + key) % 256, (pixel[1] + key) % 256, (pixel[2] + key) % 256 ) for pixel in pixels]
    
    encrypted_image = Image.new(image.mode, image.size)
    encrypted_image.putdata(encrypted_pixels)
    return encrypted_image

def decrypt_image(image, key):
    pixels = list(image.getdata())
    width, height = image.size
    random.seed(key)

    # Revert the mathematical operation
    decrypted_pixels = [( (pixel[0] - key) % 256, (pixel[1] - key) % 256, (pixel[2] - key) % 256 ) for pixel in pixels]

    # Revert the pixel swap
    swap_operations = []
    for i in range(len(pixels)):
        swap_with = random.randint(0, len(pixels) - 1)
        swap_operations.append((i, swap_with))
    for i, swap_with in reversed(swap_operations):
        decrypted_pixels[i], decrypted_pixels[swap_with] = decrypted_pixels[swap_with], decrypted_pixels[i]

    decrypted_image = Image.new(image.mode, image.size)
    decrypted_image.putdata(decrypted_pixels)
    return decrypted_image

def main():
    input_image_path = input("Enter the full path of the image to encrypt: ")
    output_image_path = input("Enter the full path to save the encrypted image: ")
    key = int(input("Enter the encryption key (integer): "))

    image = load_image(input_image_path)
    if image:
        encrypted_image = encrypt_image(image, key)
        save_image(encrypted_image, output_image_path)
        print(f"Encrypted image saved to {output_image_path}")

        decrypted_image_path = input("Enter the full path to save the decrypted image: ")
        decrypted_image = decrypt_image(encrypted_image, key)
        save_image(decrypted_image, decrypted_image_path)
        print(f"Decrypted image saved to {decrypted_image_path}")

if __name__ == "__main__":
    main()
