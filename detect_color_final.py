# import required packages
import cv2
import numpy as np
import os

# Function for detecting color of traffic light
def detect_TrafficLight_color(image_file,image_count):
    img=cv2.imread("frames/"+image_file)         # Load the image 
    img_Hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV) # Convert to HSV image

    red_low_1 = np.array([0,100,100])
    red_upper1 = np.array([10,255,255])
    red_low2= np.array([160,100,100])
    red_upper2 = np.array([180,255,255])
    
    mask1=cv2.inRange(img_Hsv.copy(), red_low_1 ,red_upper1)
    mask2=cv2.inRange(img_Hsv.copy(),red_low2, red_upper2)   #create the mask to find red color
    maskr=cv2.add(mask1,mask2)
    red_circles=cv2.HoughCircles(maskr, cv2.HOUGH_GRADIENT,1,50,param1=50,param2=10,minRadius=0,maxRadius=30)


    green_low= np.array([40,50,50])
    green_upper = np.array([90,255,255])
    maskg=cv2.inRange(img_Hsv.copy(),green_low,green_upper)  #create a mask to find the green color
    green_circles=cv2.HoughCircles(maskg, cv2.HOUGH_GRADIENT,1,40,param1=50,param2=10,minRadius=0,maxRadius=30)

    yellow_low= np.array([15,150,150])
    yellow_upper = np.array([35,255,255])
    masky=cv2.inRange(img_Hsv.copy(),yellow_low,yellow_upper)   #create a mask to find the yellow color
    yellow_circles=cv2.HoughCircles(masky, cv2.HOUGH_GRADIENT,1,60,param1=50,param2=10,minRadius=0,maxRadius=30)
    
    if red_circles is None:
        red_circles=[]          #empty the list if it is not present

    if yellow_circles is None:
        yellow_circles=[]

    if green_circles is None:
        green_circles=[]


    # Condition to detecting red color 
    if len(red_circles) > 0:
        count=0
        detected_circles=np.uint16(np.around(red_circles))
        for x,y,r in detected_circles[0,:]:
            if count<3:
                cv2.circle(img, (x,y), r+5,(0,0,255),3)
                cv2.putText(img,"RED",(x-r,(y-2*r)),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,0,255),2)
                count+=1
    

    # Condition to detecting green color 
    if len(green_circles) > 0:
        count=0
        detected_circles=np.uint16(np.around(green_circles))
        for x,y,r in detected_circles[0,:]:
            if count<2:
                cv2.circle(img, (x,y), r+5, (0,255,0),3)
                cv2.putText(img,"Green",(x-r,(y-2*r)),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,255,0),2)
                count+=1


    # Condition to detecting yellow color
    if len(yellow_circles) > 0:
        detected_circles=np.uint16(np.around(yellow_circles))
        for x,y,r in detected_circles[0,:]:
            cv2.circle(img, (x,y), r+5,(0,255,255),3)
            cv2.putText(img,"Yellow",(x-r,(y-2*r)),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,255,255),2)


    cv2.imshow("OUT1",img)    # Showing the output images
    cv2.imwrite(str(image_count)+'.jpg', img)   # saving the output images
    cv2.waitKey(2000)
    cv2.destroyAllWindows()

for a,i in enumerate(os.listdir("frames")):
    # Calling the function to detect color
    detect_TrafficLight_color(i,a)      
    