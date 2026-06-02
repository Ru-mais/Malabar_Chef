from rembg import remove
from PIL import Image

def process_image(input_path, output_path):
    print(f"Processing {input_path}...")
    input_img = Image.open(input_path)
    output_img = remove(input_img)
    output_img.save(output_path)
    print(f"Saved to {output_path}")

process_image("/Users/rumaispp/.gemini/antigravity/brain/adea0e50-f32b-4c0c-af0d-088b160ec21c/empty_plate_1779901745987.png", "public/images/plate.png")
process_image("/Users/rumaispp/.gemini/antigravity/brain/adea0e50-f32b-4c0c-af0d-088b160ec21c/kerala_porotta_1779901778189.png", "public/images/porotta.png")
process_image("/Users/rumaispp/.gemini/antigravity/brain/adea0e50-f32b-4c0c-af0d-088b160ec21c/beef_curry_1779901841206.png", "public/images/curry.png")
