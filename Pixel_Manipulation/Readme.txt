This code defines functions for encrypting and decrypting images. Here's a breakdown:

Imports:

from PIL import Image: This line imports the Image class from the Pillow library (often referred to as PIL for backwards compatibility). This class allows you to work with images in Python.
Functions:

encrypt_decrypt:

Takes four arguments: image_path (string, path to the image), operation (function for manipulating pixels), key (integer, key for encryption/decryption), and mode (string, "encrypt" or "decrypt").
Checks if the image format is supported (JPEG, PNG).
Opens the image using Image.open and gets its width and height.
Converts the image to RGB mode if needed for the operation.
Creates a new image object (new_img) and gets a way to access its pixels (new_pixels).
Loops through each pixel of the image:
Gets the red (R), green (G), and blue (B) values of the current pixel.
Calls the provided operation function with the pixel values, key, and mode. This function performs the encryption or decryption logic.
Sets the corresponding pixel in the new image with the modified values.
Saves the new image with a filename indicating the operation mode (encrypt or decrypt) appended before the original extension.
swap_pixels:

Takes five arguments: R, G, B values of a pixel, key, and mode.
Swaps the R and G values if the mode is "encrypt" (vice versa for decryption).
Returns the new R, G, B values.
add_key:

Takes the same arguments as swap_pixels.
Adds the key value to each color channel (R, G, B) if the mode is "encrypt" (subtracts for decryption).
Returns the new R, G, B values.
xor_pixels:

Similar to add_key but uses the bitwise XOR operation (^) with the key on each color channel.
Returns the new R, G, B values.
get_user_input:

Prompts the user for the image path, key (ensuring it's an integer), and encryption/decryption mode.
Returns the user-provided values.
main:

Calls get_user_input to get image details, operation choice, and key.
Creates a dictionary operation_options that maps operation names ("swap", "add", "xor") to their corresponding functions.
Based on user input, retrieves the chosen operation function from the dictionary.
Calls encrypt_decrypt with the gathered information.
Prints a success message or any encountered errors (ValueError).
Overall process:

User provides the image path, key, and operation mode.
The chosen operation function is used to modify each pixel's color values based on the key and mode ("encrypt" or "decrypt").
A new image is created with the modified pixel values.
The new image is saved with a filename indicating the applied operation.
Note: This is a basic example. More robust implementations might include features like error handling for invalid image data or providing a way to choose the output format for the new image.