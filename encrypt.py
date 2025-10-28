from PIL import Image

# --- Rail Fence Encryption ---
def rail_fence_encrypt(plaintext, rails):
    rail = ['' for _ in range(rails)]
    dir_down = False
    row = 0

    for ch in plaintext:
        rail[row] += ch
        if row == 0 or row == rails - 1:
            dir_down = not dir_down
        row += 1 if dir_down else -1

    return ''.join(rail)


# --- LSB Embedding ---
def embed_in_lsb(image_path, ciphertext, output_path):
    img = Image.open(image_path)
    img = img.convert("RGB")
    pixels = img.load()

    binary_msg = ''.join(format(ord(c), '08b') for c in ciphertext)
    binary_msg += '00000000'  # null terminator

    width, height = img.size
    idx = 0
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            rgb = [r, g, b]
            for i in range(3):
                if idx < len(binary_msg):
                    rgb[i] = (rgb[i] & ~1) | int(binary_msg[idx])
                    idx += 1
            pixels[x, y] = tuple(rgb)
            if idx >= len(binary_msg):
                break
        if idx >= len(binary_msg):
            break

    img.save(output_path)
    print(f"\n✅ Message embedded successfully into '{output_path}'")


# --- MAIN PROGRAM ---
if __name__ == "__main__":
    plaintext = input("Enter message to hide: ")
    rails = int(input("Enter number of rails for Rail Fence: "))
    image_path = input("Enter image file path : ")
    output_path = input("Enter output image file name : ")

    ciphertext = rail_fence_encrypt(plaintext, rails)
    print(f"\nEncrypted text: {ciphertext}")
    embed_in_lsb(image_path, ciphertext, output_path)
