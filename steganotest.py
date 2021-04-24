from stegano import lsb

"""Шифрование сообщения в файл изображения"""

secret = lsb.hide("image.png", "message")
secret.save("image_copy.png")

"""Расшифровка сообщения из файла изображения"""

# result = lsb.reveal("image_copy.png")
# print(result)
