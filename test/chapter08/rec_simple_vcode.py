import tesserocr
from PIL import Image

image = Image.open('code2.png')
image = image.convert('L')
threshold = 110
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
image = image.point(table, '1')
result = tesserocr.image_to_text(image)
print(result)
