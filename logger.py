import time

class Logger:
	base = "[INFO]: "
	def webcam_access(self, access : bool):
		if not access:
			print(f"{self.base}Could not access your webcam properly, Make sure you have a webcam set on your machine")
			self.exit()
		else:
			print(f"{self.base}Webcam is now on")

	def exit(self):
		print(f"{self.base}Program was executed successfully.")
		time.sleep(5)
		quit()
