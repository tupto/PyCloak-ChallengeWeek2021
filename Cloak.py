import cv2 #opencv for image processing
import numpy as np

#creating a videocapture object
cap = cv2.VideoCapture(0) #WARNING, YOUR WEBCAM IS PROBABLY INDEX 0, YOU MAY HAVE TO CHANGE IT IF I FORGET



#getting the background image
while cap.isOpened():
    haveBg, background = cap.read() #simply reading from the web cam
    
    #colour range (green)
    lower_bound = np.array([50, 80, 50])     
    upper_bound = np.array([90, 255, 255])
    

    ret = 1
    while haveBg and ret: #we have a background
        ret, currFrame = cap.read()
        
        #create a mask of everything that has changed
        hsv = cv2.cvtColor(currFrame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, lower_bound, upper_bound)
        
        #create a mask of everything that has NOT changed
        antiMask = cv2.bitwise_not(mask)
        
        #mask the image
        cloak = cv2.bitwise_and(background, background, mask=mask)
        antiCloak = cv2.bitwise_and(currFrame, currFrame, mask=antiMask)
        
        #combine the
        combination = cv2.add(cloak, antiCloak)
        
        if ret:
            cv2.imshow("image", mask)
            if cv2.waitKey(5) == ord('q'):
                #save the background image
                cv2.imwrite("image.jpg", background)
                break
cap.release()
cv2.destroyAllWindows()