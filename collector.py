import os
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
		return cv2.waitKey(25)

	def off(self):
		cv2.destroyAllWindows()
		self.cam.release()
		self.logger.turn_off()

class Preprocessor:
	def __init__(self, permission: bool, res: tuple):
		self.permission = permission
		self.res = res 

	def to_gray(self, frame):
		if self.permission != 3:
			frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		return frame

	def resize(self, frame):
		return cv2.resize(frame, self.res)

class Collect:
	def __init__(self, path: str, base_name: str, classes: int, steps: int,
				space: bool, res: tuple, _format: str):
		self.path = path
		self.base_name = base_name
		self.classes = classes
		self.steps = steps
		self.space = space
		self.res = res
		self.format = _format
		self.cam = Webcam()
		self.prep = Preprocessor(space, res)
		self.captured = None
		self.msg = "Capturing"
		self.color_mode = (30, 180, 30)
		self.cam.on()

	def check_event(self, event):
		if event == ord("c"):
			return "C"

		elif event == ord("s"):
			return "S"

		elif event == ord("u"):
			return "U"

		elif event == ord("q"):
			self.cam.off()

	def get_fname(self):
		pass

	def create(self):
		for _class in range(self.classes):
			des_path = self.path + "class" + str(_class)
			os.system(f"mkdir {des_path}")
			self.cam.logger.folder_log(des_path)

	def perform(self, frame, task):
		if task == "C":
			self.captured = frame
			self.msg = "Saving:"
			self.color_mode = (80, 215, 215)

		elif task == "S":
			save(self.base_name, self.captured)
			self.msg = "Capturing"
			self.color_mode = (30, 180, 30)

		elif task == "U":
			self.captured = None
			self.msg = "Undoing"
			self.color_mode = (215, 80, 80)

	def collect(self):
		self.create()
		while True:
			frame = self.cam.get_frame()
			clone = frame.copy()
			clone = self.cam.logger.display_buttons(clone)
			event = self.cam.show(clone)
			task = self.check_event(event)
			frame = self.prep.resize(frame)
			frame = self.prep.to_gray(frame)

def save(base_name, image: np.ndarray):
	cv2.imwrite(file, image)

