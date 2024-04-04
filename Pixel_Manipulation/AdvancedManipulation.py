from PIL import Image
import random


def encrypt_decrypt(image_path, operation, key, mode="encrypt"):
    """Encrypts or decrypts an image using pixel manipulation.

    Args:
        image_path: Path to the image file (user input).
        operation: Function to apply to each pixel (e.g., swap_pixels, add_key).
        key: Value used for the operation (user input).
        mode: "encrypt" or "decrypt" (user input).
    """
    SUPPORTED_FORMATS = (".jpg", ".jpeg", ".png")
    if not image_path.lower().endswith(SUPPORTED_FORMATS):
        raise ValueError(f"Unsupported image format: {image_path}")

    img = Image.open(image_path)  # Open image
    width, height = img.size

    new_img = img.convert("RGB")  # Convert to RGB for consistent processing
    pixels = img.load()
    new_pixels = new_img.load()

    for i in range(height):
        for j in range(width):
            r, g, b = pixels[j, i]  # Get pixel values
            new_r, new_g, new_b = operation(r, g, b, key, mode)
            new_pixels[j, i] = (new_r, new_g, new_b)  # Set new pixel values

    new_img.save(f"{image_path[:-4]}_{mode}.{img.format}")  # Save with original format


def swap_pixels(r, g, b, key, mode):
    """Swaps pixel values based on mode (encrypt or decrypt)."""
    if mode == "encrypt":
        return g, r, b
    else:
        return r, g, b


def add_key(r, g, b, key, mode):
    """Adds or subtracts the key value to each pixel based on mode."""
    if mode == "encrypt":
        return r + key, g + key, b + key
    else:
        return r - key, g - key, b - key


def xor_pixels(r, g, b, key, mode):
    """Performs bitwise XOR operation with the key on each pixel value based on mode."""
    if mode == "encrypt":
        return r ^ key, g ^ key, b ^ key
    else:
        return r ^ key, g ^ key, b ^ key


def random_shuffle(r, g, b, key, mode):
    """Shuffles pixel values (red, green, blue) randomly."""
    if mode == "encrypt":
        random.shuffle([r, g, b])
        return r, g, b
    else:
        # Decrypt by reversing the shuffle
        random.shuffle([r, g, b])
        return r, g, b


def get_user_input():
    """Gets user input for image path, operation, key, and mode."""
    while True:
        image_path = input("Enter image path: ")
        try:
            key = int(input("Enter key value: "))
            break
        except ValueError:
            print("Invalid key value. Please enter an integer.")
    mode = input("Choose 'encrypt' or 'decrypt': ").lower()
    return image_path, key, mode


def main():
    try:
        image_path, key, mode = get_user_input()
        operation_options = {
            "swap": swap_pixels,
            "add": add_key,
            "xor": xor_pixels,
            "shuffle": random_shuffle,
        }
        operation = operation_options[input("Choose operation (swap, add, xor, shuffle): ").lower()]
        encrypt_decrypt(image_path, operation, key, mode)
        print(f"Image {mode}ed successfully!")
    except ValueError as e:
        print(e)
    except KeyError:
        print("Invalid operation entered.")


if __name__ == "__main__":
    main()
