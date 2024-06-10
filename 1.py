from PIL import Image

# Откройте изображение
img = Image.open('images/ship.bmp')

# Создайте маску прозрачности
mask = Image.new('L', img.size, 0)  # Создайте маску с нулевым альфа-каналом

# Установите прозрачность для пикселей, которые нужно сделать прозрачными
for x in range(img.size):
    for y in range(img.size):
        r, g, b = img.getpixel((x, y))[:3]
        if (r, g, b) == (255, 255, 255):  # Белый цвет
            # Установите альфа-канал в 0 для прозрачности
            mask.putpixel((x, y), 0)
        else:
            # Установите альфа-канал в 255 для непрозрачности
            mask.putpixel((x, y), 255)

# Создайте новое изображение с альфа-каналом
new_img = Image.new('RGBA', img.size)
