from PIL import Image
import numpy as np

img = Image.open('C:\\Users\\kannc\\sample_img.png')
width, height = img.size
filter_size = 3
img2 = Image.new('RGB', (width, height))
img_pixels = np.array([[img.getpixel((x,y)) for x in range(width)] for y in range(height)])

#
def draw_partial_img(img2, start_x, start_y, partial_size_x, partial_size_y, pixel_color):
  for y in range(start_y, start_y + partial_size_y):
    for x in range(start_x, start_x + partial_size_x):
      img2.putpixel((x, y), pixel_color)

for y in range(0, height, filter_size):
  for x in range(0, width, filter_size):
    # ぼかし加工同様に画像の一部分を切り出す
    partial_img = img_pixels[y:y + filter_size, x:x + filter_size]
    # 色の配列になるように変換する
    color_array = partial_img.reshape(partial_img.shape[0] * partial_img.shape[1], 3)
    # 各ピクセルごとのr + g + bが最大値を取る物の番号を取得する
    # ようするに切り出した画像の中で一番濃い色の番号
    max_index = np.argmax(color_array.sum(axis=1))
    max_r, max_g, max_b = color_array[max_index]
    # (x,y)を起点に縦横フィルターサイズで単色(上記の色)の画像をimg2へセットする
    draw_partial_img(img2, x, y, partial_img.shape[1], partial_img.shape[0], (max_r, max_g, max_b))

img2.show()
