import cv2
import time
import numpy as np


class Logger:
    base = "[INFO]: "

    def webcam_access(self, access: bool):
        if access:
            print(f"{self.base}Could not access your webcam properly")
            print(f"{self.base}Make sure you have a webcam set on your machine")
            self.exit()
        else:
            print(f"{self.base}Webcam is now on")

    def invalid_path(self, path: str):
        print(f"{self.base}No such a directory named as {path} exists")
        self.exit()

    def invalid_class(self, classes: int):
        print(f"{self.base}Invalid number of classes -> {classes}")
        self.exit()

    def invalid_step(self, step: int):
        print(f"{self.base}Invalid number of steps -> {step}")
        self.exit()

    def invalid_space(self, space: int):
        print(f"{self.base}Invalid number for space -> {space}")
        self.exit()

    def invalid_format(self, _format: str):
        print(f"{self.base}Invalid format -> {_format}")

    def display_fname(self, frame: np.ndarray, event: str,
                      name: str, color_mode: tuple):
        cv2.rectangle(frame, (5, 0), (400, 50), (10, 10, 10), -1, cv2.LINE_AA)
        cv2.putText(frame, f"{event}: {name}", (10, 30),
                    cv2.FONT_HERSHEY_COMPLEX, 0.7, color_mode, 2)
        return frame

    def display_buttons(self, frame):
        cv2.rectangle(frame, (5, 50), (230, 240),
                      (10, 10, 10), -1, cv2.LINE_AA)
        cv2.putText(frame, "C -> Capture", (10, 80),
                    cv2.FONT_HERSHEY_TRIPLEX, 0.9, (30, 180, 30), 2)
        cv2.putText(frame, "S -> Save", (10, 130),
                    cv2.FONT_HERSHEY_TRIPLEX, 0.9, (80, 215, 215), 2)
        cv2.putText(frame, "U -> Undo", (10, 180),
                    cv2.FONT_HERSHEY_TRIPLEX, 0.9, (215, 80, 80), 2)
        cv2.putText(frame, "Q -> Quit", (10, 230),
                    cv2.FONT_HERSHEY_TRIPLEX, 0.9, (215, 80, 215), 2)
        return frame

    def folder_log(self, folder_name: str):
        print(f"{self.base}Created {folder_name} ...")

    def monitor(self, file_name: str):
        print(f"{self.base}Saved {file_name} successfully")

    def end(self, n_images: int):
        print(f"{self.base}Collected {n_images} images totally")
        time.sleep(2)

    def turn_off(self):
        print(f"{self.base}Webcam is now off")
        self.exit()

    def unknown(self, error: Exception):
        print(f"{self.base}An unknown issue occured -> {error} ")
        self.exit()

    def exit(self):
        print(f"{self.base}Program was executed successfully")
        time.sleep(5)
        quit()
