from PIL import Image


def encrypt_decrypt(image_path, operation, key, mode="encrypt"):
  
  SUPPORTED_FORMATS = (".jpg", ".jpeg", ".png")
  if not image_path.lower().endswith(SUPPORTED_FORMATS):
    raise ValueError(f"Unsupported image format: {image_path}")

  img = Image.open(image_path) 
  width, height = img.size

  new_img = img.convert("RGB")  
  pixels = img.load()
  new_pixels = new_img.load()

  for i in range(height):
    for j in range(width):
      r, g, b = pixels[j, i]  
      new_r, new_g, new_b = operation(r, g, b, key, mode)  
      new_pixels[j, i] = (new_r, new_g, new_b) 

  new_img.save(f"{image_path[:-4]}_{mode}.{img.format}")  

def swap_pixels(r, g, b, key, mode):
  
  if mode == "encrypt":
    return g, r, b
  else:
    return r, g, b

def add_key(r, g, b, key, mode):
    
    if mode == "encrypt":
        return r + key, g + key, b + key
    else:
       
        return r - key, g - key, b - key
def xor_pixels(r, g, b, key, mode):
  
  if mode == "encrypt":
    return r ^ key, g ^ key, b ^ key
  else:
    return r ^ key, g ^ key, b ^ key

def get_user_input():
  
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
    operation_options = {"swap": swap_pixels, "add": add_key, "xor": xor_pixels}
    operation = operation_options[input("Choose operation (swap, add, xor): ").lower()]
    encrypt_decrypt(image_path, operation, key, mode)
    print(f"Image {mode}ed successfully!")
  except ValueError as e:
    print(e)

if __name__ == "__main__":
  main()
