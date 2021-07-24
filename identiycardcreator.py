# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 11:56:55 2020

@author: Aryan
"""

import cv2
from PIL import Image

def photo(choice,name,date,rollno,course,phone,collagename):
    video=cv2.VideoCapture(0)
    check,frame=video.read()
    pic=frame
    print(pic.shape)

    if choice==1:
        pic=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    elif choice==2:
        pic=frame
    else:
        print("wrong option by default photo will be black and white")
        pic=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
       
    pic=pic[0:640,50:430]
    pic=cv2.resize(pic,(150,180))
        
        
    
    cv2.imshow("PREVIEW",pic)
    cv2.waitKey(0)
    cv2.destroyAllWindows()   
    z=int(input("If you would like to save photo  press 1:-  \n  If you would like to retake the photo press 2:- "))
    if z==1:

        cv2.imwrite(name+date+".png",pic)    
    elif z==2:
       photo(choice, name, date,rollno,course,phone,collagename)
    else:
       print("wrong option saving the pic by default")
       cv2.imwrite(name+date+".png",pic)    
    
    card(pic,name,date,collagename,rollno,course,phone)
    
    
       
def card(pic,name,date,collagename,rollno,course,phone):
    
    font = cv2.FONT_HERSHEY_DUPLEX
    font2 = cv2.FONT_ITALIC
    
    img = cv2.imread("idcard.png")
    
    cv2.putText(img,collagename,(80,60), font2, 0.8,(255,0,0),2)
    
    cv2.putText(img,name,(300,200), font, 0.51,(0,0,0),1)
    cv2.putText(img,rollno,(300,220), font, 0.51,(0,0,0),1)
    cv2.putText(img,date,(300,240), font, 0.51,(0,0,0),1)
    cv2.putText(img,course,(300,260), font, 0.51,(0,0,0),1)
    cv2.putText(img,phone,(300,280), font, 0.51,(0,0,0),1)

  
    
    
    cv2.imwrite(name+rollno+".png",img)
    
    final(pic,img,name,rollno,date)

    
def final(pic,img,name,rollno,date):
    pic1=Image.open(name+date+".png")
    pic2=Image.open(name+rollno+".png")
    
    area=(40,100)
    pic2.paste(pic1,area)
    
    pic2.show()
    pic2.save(rollno+name+"final.png")
    
    


Name=str(input("Enter your name:-  "))
Date=str(input("Enter the date to be printed on the photo:-  "))
collagename=str(input("Enter your college name:-  "))
rollno=str(input("Enter your rollno:-  "))
course=str(input("Enter your course:-  "))
phone=str(input("Enter your phone no:-  "))
Choice=int(input(" If you would like the photo to be black and white press 1:- \n if you would like the photo to be coloured press 2:-   "))
print(Name)
print(Date)
print(collagename)
print(Choice)
print(rollno)
print(course)
print(phone)




photo(Choice,Name,Date,rollno,course,phone,collagename)
