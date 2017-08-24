from PIL import Image, ImageColor, ImageOps
import colorsys

IMAGE_SIZE = (430, 430)
OVERLAY_SIZE = (430, 90)
# duration - duration of each frame of the multiframe gif, in milliseconds. Pass a single integer for a constant duration, or a list or tuple to set the duration for each frame separately.
# http://pillow.readthedocs.io/en/latest/handbook/image-file-formats.html?highlight=gif#saving
FRAME_DURATION = 500 # ms

#d6922d, #d86c27, #1b84c0
FRAME_COLORS = [(214, 146, 45), (216, 108, 39), (27, 132, 192)]
# FRAME_COLORS = ['#d6922d88', '#d86c2788', '#1b84c088']
COLOR_OVERLAY_ALPHA = 0.5
BOTTOM_SPACING = 20


overlay = Image.open('group-430.png')
overlay = overlay.resize(IMAGE_SIZE) # SVG original is 600x126, so after scaling 126 * 430 / 600 = 90


def saturate(img, ratio):
  # img = Image.open(filename)
  ld = img.load()
  width, height = img.size
  for y in range(height):
    for x in range(width):
      r,g,b = ld[x,y]
      h,s,v = colorsys.rgb_to_hsv(r/255., g/255., b/255.)
      # h = (h + -90.0/360.0) % 1.0
      # s = s**0.65
      s = s * ratio
      r,g,b = colorsys.hsv_to_rgb(h, s, v)
      ld[x,y] = (int(r * 255.9999), int(g * 255.9999), int(b * 255.9999))
  return img

def read_img(path):
  img = Image.open(path)
  img2 = img.resize(IMAGE_SIZE).convert('RGB')
  return saturate(img2, 0.6) # saturation down by 40%

def add_overlay(img, overlay):
  img.paste(overlay, mask=overlay)
  return img

def fun(x, max):
  return -abs(x - 127.5)/127.5 + max # it's a linear function with max at (127.5, 1) and "mins" at (0, 0) and (255, 0)

def blend_img(img, color):
  color_img3 = Image.new('RGB', IMAGE_SIZE, color=color)
  ld = img.convert('L').load()
  color_ld = color_img3.load()
  width, height = img.size
  r, g, b = color
  h, s, v = colorsys.rgb_to_hsv(r, g, b)
  # print(h, s, v)
  for y in range(height):
    for x in range(width):
      # print("[x,y] = ",x, y)
      brightness = ld[x, y]
      # print(brightness)
      img_r, img_g, img_b = colorsys.hsv_to_rgb(h, fun(brightness, s), brightness)
      # print(img_r, img_g, img_b)
      # ld[x, y] = (int(img_r * 255.9999), int(img_g * 255.9999), int(img_b * 255.9999))
      img_r = int(img_r)
      img_g = int(img_g)
      img_b = int(img_b)
      # print(img_r, img_g, img_b)
      color_ld[x, y] = (img_r, img_g, img_b)
  # color_img3.show()
  return Image.blend(img, color_img3, COLOR_OVERLAY_ALPHA)
  # return Image.blend(Image.composite(img, color_img3, img.convert('L')), color_img3, COLOR_OVERLAY_ALPHA)

frame1 = add_overlay(blend_img(read_img('11.png'), FRAME_COLORS[0]), overlay)
frame2 = add_overlay(blend_img(read_img('22.png'), FRAME_COLORS[1]), overlay)
frame3 = add_overlay(blend_img(read_img('55.png'), FRAME_COLORS[2]), overlay)
frame1.save('out1.png')
frame2.save('out2.png')
frame3.save('out3.png')

import imageio
images = []
for filename in ['out1.png', 'out2.png', 'out3.png']:
    images.append(imageio.imread(filename))
imageio.mimsave('out-io.gif', images, duration=0.5)


