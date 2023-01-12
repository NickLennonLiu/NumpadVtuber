import os
import cv2
from tqdm import tqdm

"""
Change your transparent background image to certain mask
(green by default)
"""

def change_color(to):

	for image in tqdm(os.listdir("./raw")):
		img = cv2.imread(os.path.join("./raw", image), -1)
		sp = img.shape
		width = sp[0]
		height = sp[1]
		for y in range(height):
			for x in range(width):
				color_d = img[x, y]
				if color_d[3] == 0:
					img[x, y] = to
		cv2.imwrite(os.path.join("./images", image), img)

if __name__ == "__main__":
	change_color([0,255,0,255])