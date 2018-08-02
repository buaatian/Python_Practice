from PIL import Image, ImageDraw, ImageFont
front = ImageFont.truetype("arial.ttf", 15)
im = Image.open("image.jpg")
draw = ImageDraw.Draw(im)
draw.text((10, 10), "4", font=front, fill=(0, 0, 0))
im.save("change.jpg")
