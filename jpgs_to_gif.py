from PIL import Image

IMAGE_SIZE = (430, 430)
OVERLAY_SIZE = (430, 90)
# duration - duration of each frame of the multiframe gif, in milliseconds. Pass a single integer for a constant duration, or a list or tuple to set the duration for each frame separately.
# http://pillow.readthedocs.io/en/latest/handbook/image-file-formats.html?highlight=gif#saving
FRAME_DURATION = 500 # ms

#d6922d, #d86c27, #1b84c0
FRAME_COLORS = [(214, 146, 45), (216, 108, 39), (27, 132, 192)]
COLOR_OVERLAY_ALPHA = 0.4
BOTTOM_SPACING = 20


overlay = Image.open('group.png')
overlay = overlay.resize(OVERLAY_SIZE) # SVG original is 600x126, so after scaling 126 * 430 / 600 = 90

def read_img(path):
  img = Image.open(path)
  return img.resize(IMAGE_SIZE)

def add_overlay(img, overlay):
  img.paste(overlay, box=(0, img.height - OVERLAY_SIZE[1] - BOTTOM_SPACING), mask=overlay)
  return img

def blend_img(img, color):
  color_img = Image.new('RGB', IMAGE_SIZE, color=color)
  return Image.blend(img, color_img, COLOR_OVERLAY_ALPHA)


frame1 = add_overlay(blend_img(read_img('1.jpg'), FRAME_COLORS[0]), overlay)
frame2 = add_overlay(blend_img(read_img('2.jpg'), FRAME_COLORS[1]), overlay)
frame3 = add_overlay(blend_img(read_img('3.jpg'), FRAME_COLORS[2]), overlay)

frame1.save('out.gif', save_all=True, append_images=[frame2, frame3], loop=0, duration=500)


