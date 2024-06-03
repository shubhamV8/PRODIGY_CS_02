import os
from PIL import Image
import requests
from io import BytesIO

def encrypt_image(image_path):
    image = Image.open(image_path)
    pixels = image.load()
    width, height = image.size

    # Loop through each pixel and swap red and blue values
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            pixels[x, y] = (b, g, r)

    encrypted_image_path = os.path.join(os.getcwd(), os.path.splitext(os.path.basename(image_path))[0] + '_encrypted.png')
    image.save(encrypted_image_path)
    print("Image encrypted successfully!")
    return encrypted_image_path

def decrypt_image(image_path):
    image = Image.open(image_path)
    pixels = image.load()
    width, height = image.size

    # Loop through each pixel and swap red and blue values back
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            pixels[x, y] = (b, g, r)

    decrypted_image_path = os.path.join(os.getcwd(), os.path.splitext(os.path.basename(image_path))[0] + '_decrypted.png')
    image.save(decrypted_image_path)
    print("Image decrypted successfully!")
    return decrypted_image_path

def encrypt_image_from_url(image_url):
    response = requests.get(image_url)
    image = Image.open(BytesIO(response.content))
    pixels = image.load()
    width, height = image.size

    #Loop through each pixel and swap red and blue values
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            pixels[x, y] = (b, g, r)

    print("Image encrypted successfully!")
    return image

def decrypt_image_from_url(image_url):
    response = requests.get(image_url)
    image = Image.open(BytesIO(response.content))
    pixels = image.load()
    width, height = image.size

    #Loop through each pixel and swap red and blue values back
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            pixels[x, y] = (b, g, r)

    print("Image decrypted successfully!")
    return image

def main():
    mode = input("Enter 1 for 'encrypt' or 2 for 'decrypt': ")

    if mode == "1":
        image_path = input("Enter the path of the image or URL: ")
        if image_path.startswith("http://") or image_path.startswith("https://"):
            encrypted_image = encrypt_image_from_url(image_path)
            encrypted_image_path = os.path.join(os.getcwd(), os.path.splitext(os.path.basename(image_path.split('/')[-1]))[0] + '_encrypted.png')
            encrypted_image.save(encrypted_image_path)
            encrypted_image.show()  # Display encrypted image
        else:
            encrypt_image(image_path)
    elif mode == "2":
        image_path = input("Enter the path of the image: ")
        decrypt_image(image_path)
    else:
        print("Invalid mode! Please enter '1' (Encrypt) or '2' (Decrypt).")

if __name__ == "__main__":
    main()
