from PIL import Image
img = Image.open('snake.jpg')
change_img = img.resize((900, 600))
change_img.save('snake.png')
print(change_img)