import cv2 #opencv for image processing
import numpy as np

#creating a videocapture object
cap = cv2.VideoCapture(0) #this is my webcam



#getting the background image
while cap.isOpened():
    haveBg, background = cap.read() #simply reading from the web cam
    
    #colour range (green)
    hsv = cv2.cvtColor(background, cv2.COLOR_BGR2HSV)
    lower_bound = np.array([25, 25, 25])     
    upper_bound = np.array([255, 255, 255])
    
    mask = cv2.inRange(hsv, lower_bound, upper_bound)

    while haveBg: #we have a background
        ret, currFrame = cap.read()
        
        #get the difference between the current frame and the first frame
        cloak = cv2.absdiff(background, currFrame)
        
        #create a mask of everything that has changed
        mask = cv2.inRange(cloak, lower_bound, upper_bound)
        #create a mask of everything that has NOT changed
        antiMask = cv2.bitwise_not(mask)
        #mask the image
        antiCloak = cv2.bitwise_and(currFrame, currFrame, mask=antiMask)
        
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