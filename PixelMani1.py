from PIL import Image

def encrypt_image(image_path):
    image = Image.open(image_path)
    pixels = image.load()
    width, height = image.size

    # Loop through each pixel
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]

            # Swap red and blue values
            pixels[x, y] = (b, g, r)

    encrypted_image_path = f"{image_path.split('.')[0]}_encrypted.png"
    image.save(encrypted_image_path)
    print("Image encrypted successfully!")
    return encrypted_image_path

def decrypt_image(image_path):
    image = Image.open(image_path)
    pixels = image.load()
    width, height = image.size

    # Loop through each pixel
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]

            # Swap red and blue values back
            pixels[x, y] = (b, g, r)

    decrypted_image_path = f"{image_path.split('_encrypted')[0]}_decrypted.png"
    image.save(decrypted_image_path)
    print("Image decrypted successfully!")
    return decrypted_image_path

def main():
    image_path = input("Enter the path of the image: ")
    mode = input("Enter 1 for 'encrypt' or 2 for 'decrypt': ")
    if mode == "1":
        encrypt_image(image_path)
    elif mode == "2":
        decrypt_image(image_path)
    else:
        print("Invalid mode! Please enter '1' (Encrypt) or '2' (Decrypt).")

if __name__ == "__main__":
    main()
