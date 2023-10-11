# Author: mihcuog@AILab
# Contatct: AI-Lab - Smart Things

import cv2
import numpy as np
from pyzbar.pyzbar import decode
import time

#img = cv2.imread('1.png')
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
fps = 0
frame_cnt = 0
frame_start_time = 0
font = cv2.FONT_HERSHEY_SIMPLEX

# decoded_data = "Bﾃｹi Minh Cﾆｰ盻拵g"
# decoded_text = decoded_data.encode('utf-8').decode('utf-8')
# print(decoded_text)

with open('myDataFile.text', encoding='utf-8') as f:
    myDataList = f.read().splitlines()
    count_people_length = len(myDataList)

while True:
    success, img = cap.read()
    for barcode in decode(img):
        # print(decode(img))
        # print(barcode)
        myData = barcode.data.decode('utf-8')
        print(myData)
        now = time.time()
        frame_time = now - frame_start_time
        fps = 1.0 / frame_time
        frame_start_time = now
        if myData in myDataList:
            # out_name = myDataList[0]
            myOutput = 'WELCOME!!! THE DOOR IS OPEN!'
            # text = ''
            myColor = (0,255,0)
            cv2.putText(img, "PERSON DETECT:  " + str(myData), (20, 130), font, 0.8, (0, 255, 0), 1, cv2.LINE_AA)    

        else:
            myOutput = 'SORRY!!! YOU ARE NOT IN DATA! '
            
            myColor = (0, 0, 255)

        pts = np.array([barcode.polygon],np.int32)
        pts = pts.reshape((-1,1,2))
        cv2.polylines(img,[pts],True,myColor,5)
        pts2 = barcode.rect
        # print(myData)

        
        cv2.putText(img,myOutput,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX,
                    0.9,myColor,2)
        # cv2.putText(img,myOutput,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX,
                    # 0.9,myColor,2)
        
    cv2.putText(img, "FPS:            " + str(fps.__round__(2)), (20, 70), font, 0.8, (0, 255, 0), 1, cv2.LINE_AA)    
    cv2.putText(img, "DATA:           " + str(count_people_length), (20, 100), font, 0.8, (0, 255, 0), 1, cv2.LINE_AA)    


    cv2.imshow('Result',img)
    # put notification
    
    key_shut = cv2.waitKey(1)
    if key_shut == ord('q'):
        break
cv2.destroyAllWindows()
cap.release()
