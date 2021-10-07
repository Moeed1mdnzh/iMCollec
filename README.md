# iMCollec
iMCollec is an image collecting tool for your datasets.Let's see how you can gather your own image dataset.

## Steps
### step-1
Clone the repo as usual <br/>
`git clone https://github.com/Moeed1mdnzh/iMCollec.git` 
### step-2
Minimum version for python to use this tool is 3.8. Install the required packages using the following command
`pip install -r requirements.txt` 
### step-3
In order to use the tool, You must pass a couple of arguments to the tool.
```python
python iMCollec.py -p PATH -n NAME -c CLASSES -s STEPS -g SPACE[OPTIONAL] -r RESOLUTION[OPTONAL] -f FORMAT[OPTIONAL]
```
By using the command
```python
python iMCollec.py --help
```
You will receive complete explanations associated with the arguments, But for now let's have a look on the explanations. <br/>
1. -p: Path to the folder in which the images are saved, Example: -p Desktop/myData/
2. -n: Base name of the images, Example: -n img
3. -c: Number of the classes
4. -s: Number of the images for each class
5. -g: Colorspace of the images, Must be 1 for gray or 3 for rgb
6. -r: Resolution of the images, Example: -r 128x128
7. -f: Format of the images, Must jpg or png

## Guidance
After running the tool, You will see any information related to the tool printed in the command prompt or terminal which makes
the tool easy to monitor and debug.You should now have some subfolders in the path you gave to the tool like the following 
```python
-> myData 
   ├───class_0 
   └───class_1 
```
In my case I have 2 subfolders since I inserted 2 as my number of classes.
### Collection-Process
Eventually, you now have your webcam turned on and should face the following image <br/>
![Example 1](https://github.com/Moeed1mdnzh/iMCollec/blob/master/examples/example_1.jpg) 
<br/> The things that you're looking at right now is a lot for your mind to digest, so let's break it down. <br/>There are total 4 buttons in this tool which are 
shown in the previous image by 4 colors green for capturing, yellow for saving, blue for undoing and pink for quiting. <br/>The top text says *Capturing: class_0/img_0_0.jpg*,
 What do you think is meant by that? Well, *Capturing* means that the program is waiting for you to press C to capture the image, So remember that it won't save the 
 image, It is only captured for now.Once you press C you realize that the text changes like the following example
![Example 2](https://github.com/Moeed1mdnzh/iMCollec/blob/master/examples/example_2.jpg) 
<br/> Again the program is now waiting for you to press S to save the captured image but Let's say that you pressed C by mistake, You can undo it by pressing U to get the below image and you can again press C to capture another image.
![Example 3](https://github.com/Moeed1mdnzh/iMCollec/blob/master/examples/example_3.jpg) 
<br/> <br/>
But what about the text in front of *Capturing*? What is that? *class_0* is the subfolder for the first class which the program created automatically and 
*img_0_0.jpg* is the name of the image.So how is the name generated? Take a look at the below table <br/>
| **img**  | **First 0** | **Second 0** | **.jpg** |
| ------------- | ------------- | ------------- | ------------- |
| Base Name   | Class Id  | Image Id | Image Format |

