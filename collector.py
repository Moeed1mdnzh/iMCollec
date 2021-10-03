import cv2
import numpy as np
from logger import Logger

class Webcam:
	def __init__(self):
		self.logger = Logger()
		self.cam = None 

	def on(self):
		self.cam = cv2.VideoCapture(3)

	def get_frame(self):
		frame = self.cam.read()[1]
		access = 0
		if frame is not None:
			access = 1
		self.logger.webcam_access(0)
		return frame

	def show(self, frame):
		cv2.imshow("Frame", frame)
		cv2.waitKey(25)

	def off(self):
		cv2.destroyAllWindows()
		self.cam.release()

class Collect:
	def __init__(self, base_name : str, classes : int, step : int,
				gray : bool, res : tuple):
		self.cam = Webcam()
		self.base_name = base_name
		self.classes = classes 
		self.step = step 
		self.gray = gray  
		self.res = res

	def to_gray(self, permission):
		pass

	def resize(self, res):
		pass 

	def collect(self):
		while True:
			self.cam.on()
			frame = self.cam.get_frame()
			self.cam.show(frame)

		

def save(image : np.ndarray):
	pass

def main():
	c = Collect("img", 2, 25, 0, "128x128")
	c.collect()

if __name__ == "__main__":
	main()
