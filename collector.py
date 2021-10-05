import cv2
import numpy as np
from logger import Logger

class Webcam:
	def __init__(self):
		self.logger = Logger()
		self.cam = None 

	def on(self):
		self.cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
		frame = self.cam.read()[1] 	
		access = 0
		if frame is not None:
			access = 1
		self.logger.webcam_access(0)

	def get_frame(self):
		frame = self.cam.read()[1]
		return frame

	def show(self, frame: np.ndarray):
		cv2.imshow("Frame", frame)
		if cv2.waitKey(25) == ord("q"):
			self.logger.exit()

	def off(self):
		cv2.destroyAllWindows()
		self.cam.release()

class Collect:
	def __init__(self, base_name: str, classes: int, steps: int,
				space: bool, res: tuple):
		self.cam = Webcam()
		self.base_name = base_name
		self.classes = classes 
		self.steps = steps
		self.space = space
		self.res = res

	def to_gray(self, frame: np.ndarray, permission: bool=3):
		if permission != 3:
			frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
		return frame

	def resize(self, frame: np.ndarray , res: tuple):
		return cv2.resize(frame, res)

	def collect(self):
		self.cam.on()
		while True:
			frame = self.cam.get_frame()
			clone = frame.copy()
			frame = self.resize(frame, self.res)
			frame = self.to_gray(frame, permission=self.space)
			
			self.cam.show(frame)

def save(image: np.ndarray):
	pass

def main():
	c = Collect("img", 2, 25, 0, "128x128")
	c.collect()

if __name__ == "__main__":
	main()
