#!/usr/bin/env python

import os

from PIL import ImageSequence


RGB = 'RGB'


def get_frames(image):
    """Get image frames from the GIF file."""
    try:
        if image.mode != RGB:
            image = image.convert(RGB)
        frames = (frame.copy() for frame in ImageSequence.Iterator(image))
        return frames
    except OSError:
        # images to be opened might by corrupted or truncated
        return None


def write_images(frames, src_filename, dst_dirpath):
    """Split the GIF image and write as the distinct image files."""
    for index, frame in enumerate(frames):
        dst_filename = src_filename.split('.')[0] + '_{0}.jpg'.format(index)
        dst_filepath = os.path.join(dst_dirpath, dst_filename)
        frame.save(dst_filepath)
