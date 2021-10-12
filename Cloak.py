import cv2 #opencv for image processing
import numpy as np

#creating a videocapture object
cap = cv2.VideoCapture(0) #WARNING, YOUR WEBCAM IS PROBABLY INDEX 0, YOU MAY HAVE TO CHANGE IT IF I FORGET

#TODO LEARN WTF THIS DOES
open_kernel = np.ones((3,3),np.uint8)
close_kernel = np.ones((5,5),np.uint8)
dilation_kernel = np.ones((5, 5), np.uint8)

def filter_mask(mask):
    close_mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, close_kernel)
    open_mask = cv2.morphologyEx(close_mask, cv2.MORPH_OPEN, open_kernel)
    dilation = cv2.dilate(open_mask, dilation_kernel, iterations= 1)
    return dilation

def tobyFilter(image):
    #ADD YOUR OWN STYLE HERE
    return image

def alexFilter(image):
    #ADD YOUR OWN STYLE HERE
    return image

def andreiFilter(image):
    #ADD YOUR OWN STYLE HERE
    return image

def jodyFilter(image):
    #ADD YOUR OWN STYLE HERE
    return image

#getting the background image
while cap.isOpened():
    haveBg, background = cap.read() #simply reading from the web cam
    
    background = tobyFilter(background) # REPLACE WITH ONE OF THE OTHER FUNCTIONS
    
    #colour range (green)
    lower_bound = np.array([50, 80, 50])     
    upper_bound = np.array([90, 255, 255])
    

    ret = 1
    while haveBg and ret: #we have a background
        ret, currFrame = cap.read()
        
        #create a mask of everything that has changed
        hsv = cv2.cvtColor(currFrame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, lower_bound, upper_bound)
        mask = filter_mask(mask)
        
        #create a mask of everything that has NOT changed
        antiMask = cv2.bitwise_not(mask)
        
        #mask the image
        cloak = cv2.bitwise_and(background, background, mask=mask)
        antiCloak = cv2.bitwise_and(currFrame, currFrame, mask=antiMask)
        
        #cloak
        
        #combine the
        combination = cv2.add(cloak, antiCloak)
        
        if ret:
            cv2.imshow("image", combination)
            if cv2.waitKey(5) == ord('q'):
                #save the background image
                cv2.imwrite("image.jpg", background)
                break
cap.release()
cv2.destroyAllWindows()