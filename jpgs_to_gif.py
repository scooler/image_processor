from PIL import Image

IMAGE_SIZE = (430, 430)
OVERLAY_SIZE = (430, 90)
# duration - duration of each frame of the multiframe gif, in milliseconds. Pass a single integer for a constant duration, or a list or tuple to set the duration for each frame separately.
# http://pillow.readthedocs.io/en/latest/handbook/image-file-formats.html?highlight=gif#saving
FRAME_DURATION = 500 # ms

overlay = Image.open('group.png')
overlay = overlay.resize(OVERLAY_SIZE) # SVG original is 600x126, so after scaling 126 * 430 / 600 = 90


def prepare_frame(path, overlay):
  img = Image.open(path)
  out = img.resize(IMAGE_SIZE)
  out.paste(overlay, box=(0, out.height - OVERLAY_SIZE[1]), mask=overlay)
  return out

frame1 = prepare_frame('1.jpg', overlay)
frame2 = prepare_frame('2.jpg', overlay)

frame1.save('out.gif', save_all=True, append_images=[frame2], loop=0, duration=500)
