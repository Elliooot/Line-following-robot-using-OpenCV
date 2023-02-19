import cv2
import time
import numpy as np
import serial

ser = serial.Serial('/dev/ttyACM0',baudrate = 115200,timeout=1)
cap = cv2.VideoCapture(0)
cap.set(3,320)
cap.set(4,240)
xs=0
xe=int(cap.get(3))
ys=int(cap.get(4)/3)
ye=int(cap.get(4))
print(xs,xe,ys,ye)

while(1):
    ret,img=cap.read()
    if ret:
        hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        
        lower_black=np.array([0,0,0])
        upper_black=np.array([180,255,46])
        mask0=cv2.inRange(hsv,lower_black,upper_black)
        
        contours = cv2.findContours(mask0,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)      
        contours1 = sorted(contours[0],key=cv2.contourArea,reverse=True)
        
        if len(contours1)>0:
            x,y,w,h=cv2.boundingRect(contours1[0])
            cx=x+int(w/2)
            cy=y+int(h/2)+ys
            
            cv2.circle(img,(cx,cy),int(w/8),(0,255,0),2)
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            
            print("cx = ", cx)
            
            if cx>80 and cx<240: #go straight
                ser.write('W'.encode('ascii'))
            elif cx>240: #turn right
                ser.write('D'.encode('ascii'))
            elif cx<=80: #turn left
                ser.write('A'.encode('ascii'))
            ser.flush()
                          
        cv2.imshow('img',img)
        cv2.imshow('mask',mask0)
        
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break
    
    else:
        break
        
cap.release()
cv2.destroyAllWindows()
ser.close()
