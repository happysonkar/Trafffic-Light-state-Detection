# Trafffic Light state Detection
 Detecting the color of traffic Light

* Install opencv

```
pip install opencv-python
```
It should be noted that OpenCV requires: ``numpy`` 

``numpy`` 

pip install numpy



● First I have loaded the images and converted them to HSV
images which are used to detect different colours from them.
● Then I gathered the BGR color codes ranges of RED, GREEN
and YELLOW color.
● And Created the masks for each color which only contain
RED,GREEN and YELLOW color
● Then I have used a technique called Hough Circles which are
used to detect the circle in images.
● This technique we have applied to that mask that we have
created earlier and then detected circles are stored in array.
● Then IF conditions are applied for detecting and drawing contour
of circles around traffic light color and adding text to the images.
● Showing the output images and saving the output Images .
