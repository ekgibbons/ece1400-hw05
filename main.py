import sys

import imageprocessing


if len(sys.argv) < 2:
    print("Usage:")
    print("    $ python %s <input_photo_file_name>" %
          sys.argv[0])
    sys.exit(0)

image_file = sys.argv[1]

try:
    im = imageprocessing.Image(image_file)
except RuntimeError as e:
    print("ERROR: %s" % e)
    sys.exit(2)

im.sharpening(0.5)
im.display_im()

im.write_im("sharp_wildcat.jpg")

im.smoothing()
im.display_im()

im.write_im("smooth_wildcat.jpg")

print(im)
