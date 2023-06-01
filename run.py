from PIL import Image

image_path = 'Windows_Terminal_logo.svg.png'

img = Image.open(image_path)
# изменяем размер
new_image = img.resize((50000, 50000))
new_image.save('rip.png')
