from PIL import Image
import numpy as np
import cv2

def update_orientation(image):
	exif_orientation_tag = 0x0112
	if hasattr(image, '_getexif'):
		exif = image._getexif()
		if (exif != None and exif_orientation_tag in exif):
			orientation = exif.get(exif_orientation_tag, 1)
			orientation -= 1
			if orientation >= 4:
				image = image.transpose(Image.TRANSPOSE)
			if orientation == 2 or orientation == 3 or orientation == 6 or orientation == 7:
				image = image.transpose(Image.FLIP_TOP_BOTTOM)
			if orientation == 1 or orientation == 2 or orientation == 5 or orientation == 6:
				image = image.transpose(Image.FLIP_LEFT_RIGHT)
	return image

def convert_to_opencv(image):
	r,g,b = np.array(image).T
	opencv_image = np.array([b,g,r]).transpose()
	return opencv_image

def resize_down_to_1600_max_dim(image):
	h, w = image.shape[:2]
	if (h < 1600 and w < 1600):
		return image
	new_size = (1600 * w // h, 1600) if (h > w) else (1600, 1600 * h // w)
	return cv2.resize(image, new_size, interpolation = cv2.INTER_LINEAR)

def crop_center(img,cropx,cropy):
	h, w = img.shape[:2]
	startx = w//2-(cropx//2)
	starty = h//2-(cropy//2)
	return img[starty:starty+cropy, startx:startx+cropx]

def resize_to_256_square(image):
	h, w = image.shape[:2]
	return cv2.resize(image, (256, 256), interpolation = cv2.INTER_LINEAR)

def prepareimage(image):
	image = resize_down_to_1600_max_dim(convert_to_opencv(update_orientation(image)))
	h, w = image.shape[:2]
	min_dim = min(w,h)

def prepareimage(image):
	image = update_orientation(image)
	image = convert_to_opencv(image)
	image = resize_down_to_1600_max_dim(image)
	h, w = image.shape[:2]
	min_dim = min(w,h)
	max_square_image = crop_center(image, min_dim, min_dim)
	augmented_image = resize_to_256_square(max_square_image)
	network_input_size = 227
	return crop_center(augmented_image, network_input_size, network_input_size)