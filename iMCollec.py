import os
import cv2
import argparse
import numpy as np
from logger import Logger
from collector import Collect

ap = argparse.ArgumentParser()
ap.add_argument("-p", "--path", required=True, type=str,
                help="Path to the directory where images are saved")
ap.add_argument("-n", "--name", default="img", type=str,
                help="Base name of the images")
ap.add_argument("-c", "--classes", required=True,
                type=int, help="Number of classes")
ap.add_argument("-s", "--steps", required=True, type=int,
                help="Number of images of each class")
ap.add_argument("-g", "--space", default=3, type=int,
                help="Color space of the images, Should be wether 1 or 3")
ap.add_argument("-r", "--resolution", default="NULL", type=str,
                help="Resolution of images, For instance: '128x128'")
ap.add_argument("-f", "--format", default="jpg", type=str,
                help="Format of the images, Must be wether jpg or png")
args = vars(ap.parse_args())
logs = Logger()


def preprocess_args(args):
    if not os.path.exists((x:= args["path"])):
        logs.invalid_path(x)

    if (x:= args["classes"]) < 1:
        logs.invalid_class(x)

    if (x:= args["steps"]) < 1:
        logs.invalid_step(x)

    if (x:= args["space"]) not in (1, 3):
        logs.invalid_space(x)

    if args["resolution"] == "NULL":
        args["resolution"] = "640x480"
    args["resolution"] = tuple(map(int, args["resolution"].split("x")))

    if (x:= args["format"]) not in ("jpg", "png"):
        logs.invalid_format(x)
    return args


args = preprocess_args(args)
collector = Collect(args["path"], args["name"], args["classes"], args["steps"],
                    args["space"], args["resolution"], args["format"])

try:
    collector.collect()
except Exception as e:
    logs.unknown(e)
