from PIL import Image

def remove_white_bg(input_path, output_path, tolerance=240):
    img = Image.open(input_path).convert("RGBA")
    data = img.getdata()
    new_data = []
    
    for item in data:
        # If the pixel is close to white, make it transparent
        if item[0] >= tolerance and item[1] >= tolerance and item[2] >= tolerance:
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append(item)
            
    img.putdata(new_data)
    img.save(output_path, "PNG")

remove_white_bg("public/images/plate.png", "public/images/plate.png")
remove_white_bg("public/images/porotta.png", "public/images/porotta.png")
remove_white_bg("public/images/curry.png", "public/images/curry.png")
print("Backgrounds removed!")
