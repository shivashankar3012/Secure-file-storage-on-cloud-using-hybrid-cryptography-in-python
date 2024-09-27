from tkinter import *
import cv2

def color():
    cap = cv2.VideoCapture(0)
    while(True):
        ret, frame = cap.read()
        cv2.imshow('frame',frame)
        key = cv2.waitKey(10)
        if key == 32:
            break
    cap.release()
    cv2.destroyAllWindows()
    
def gray():
    cap=cv2.VideoCapture(0)
    while(True):
        ret,frame=cap.read()
        gray =cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame',gray)
        key = cv2.waitKey(10)
        if key == 27:
            break
    cap.release()
    cv2.destroyAllWindows()
def hsv():
    cap=cv2.VideoCapture(0)
    while(True):
        ret,frame=cap.read()
        hsv_col=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        cv2.imshow('frame',hsv_col)
        key = cv2.waitKey(10)
        if key == 27:
            break
    cap.release()
    cv2.destroyAllWindows()
def canny():
    cap=cv2.VideoCapture(0)
    while(True):
        ret,frame=cap.read()
        edges= cv2.Canny(frame,100,200)
        cv2.imshow('frame',edges)
        key = cv2.waitKey(10)
        if key == 27:
            break
    cap.release()
    cv2.destroyAllWindows()
        
if __name__ == '__main__':

    
    root=Tk()
    
    root.geometry('600x350')
    
    root.title('opencv')
    
    w1=Button(root,text="click",command=color).grid(row=3,column=1,pady=15,padx=15)
    
    w1=Button(root,text="click2",command=gray).grid(row=4,column=1,pady=15,padx=15)
    
    w1=Button(root,text="click3",command=hsv).grid(row=5,column=1,pady=15,padx=15)
    
    w1=Button(root,text="click4",command=canny).grid(row=6,column=1,pady=15,padx=15)
    
    root.mainloop()

