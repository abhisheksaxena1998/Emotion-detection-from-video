import cv2
vidcap = cv2.VideoCapture('Dronefeed.mp4')
def getFrame(sec):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()
    if hasFrames:
        cv2.imwrite("test"+str(count)+".jpg", image)   
    return hasFrames
sec = 0
frameRate = 0.96774193548387
count=0
success = getFrame(sec)
while success:
    count = count + 1
    sec = sec + frameRate
    sec = round(sec, 2)
    success = getFrame(sec)











