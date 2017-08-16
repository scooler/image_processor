from PIL import Image

im = Image.open('1.jpg')
im2 = Image.open('2.jpg')
# duration - duration of each frame of the multiframe gif, in milliseconds. Pass a single integer for a constant duration, or a list or tuple to set the duration for each frame separately.
# http://pillow.readthedocs.io/en/latest/handbook/image-file-formats.html?highlight=gif#saving
im.save('out.gif', save_all=True, append_images=[im2], loop=0, duration=500)
