from PIL import Image

IMAGE_SIZE=(430, 430)
# duration - duration of each frame of the multiframe gif, in milliseconds. Pass a single integer for a constant duration, or a list or tuple to set the duration for each frame separately.
# http://pillow.readthedocs.io/en/latest/handbook/image-file-formats.html?highlight=gif#saving
FRAME_DURATION=500 # ms

im = Image.open('1.jpg')
im2 = Image.open('2.jpg')

out = im.resize(IMAGE_SIZE)
out2 = im2.resize(IMAGE_SIZE)

out.save('out.gif', save_all=True, append_images=[out2], loop=0, duration=500)
