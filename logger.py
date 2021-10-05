import time

class Logger:
	base = "[INFO]: "
	def webcam_access(self, access: bool):
		if access:
			print(f"{self.base}Could not access your webcam properly, Make sure you have a webcam set on your machine")
			self.exit()
		else:
			print(f"{self.base}Webcam is now on")

	def invalid_class(self, classes: int):
		 print(f"{self.base}Invalid number of classes -> {classes}")
		 self.exit()

	def invalid_step(self, step: int):
		print(f"{self.base}Invalid number of steps -> {step}")
		self.exit()

	def invalid_space(self, space: int):
		print(f"{self.base}Invalid number for space -> {space}")
		self.exit()

	def exit(self):
		print(f"{self.base}Program was executed successfully")
		time.sleep(5)
		quit()
