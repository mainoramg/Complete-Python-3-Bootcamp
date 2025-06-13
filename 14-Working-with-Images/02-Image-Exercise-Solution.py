from PIL import Image

word_matrix = Image.open("word_matrix.png")
mask = Image.open("mask.png")

matrix_size = word_matrix.size
mask = mask.resize(matrix_size)
mask.putalpha(128)

word_matrix.paste(im=mask, box=(0,0), mask=mask)
word_matrix.show()
