import cv2
import numpy as np
import math
from parser import in_video

in_video_path = '../../Naver_video_02.mp4'
#out_video_path = '../Result_Naver_video_01.mp4'
out_video_path = '../../test_0525_2.mp4'
cap = cv2.VideoCapture(in_video_path)
back_cap = cv2.VideoCapture(in_video_path)##
width = int(cap.get(3))
height = int(cap.get(4))
fps = int(cap.get(cv2.CAP_PROP_FPS))

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(out_video_path, fourcc, fps, (width, height))

colors = [
    (0,0,255), #red
    (0,255,0), #green
    (255,0,0), #blue
    (0,255,255), #yellow
    (255,0,255), #pink
    (255,255,0) #skyblue
]

print("Wait...")

# hand point stack
left_hand = []
right_hand = []
for i in range(in_video.hum_cnt):
    left_hand.append([i+1])
    right_hand.append([i+1])

def ani_effect(x,y,fr,effect):
    rows, cols, channels = effect.shape
    roi = fr[x:rows+x, y:cols+y]

    effect_gray = cv2.cvtColor(effect, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(effect_gray, 10 ,255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)

    fr_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
    effect_fg = cv2.bitwise_and(effect, effect, mask=mask)

    dst = cv2.add(fr_bg, effect_fg)
    fr[x:rows+x, y:cols+y] = dst

    return fr

i = 0
while(cap.isOpened()):
    ret, frame = cap.read()
    back_ret, back_frame = back_cap.read() # original frame / It's for opacity

    if ret == False:
        print("Oops... ")
        break

    #Skip the unrecognized frame
    if in_video.frames[i] == 'empty_frame':
        i += 1
        continue

    # Short Test
    if i > 500 :
        break
    
    # draw prepared img
    n = 48
    start = 100
    if start <= i < start+n :
        stars = cv2.imread('./Effects/Star_new/stars'+str(i-start).zfill(4)+'.jpg')
        frame = ani_effect(10, 10, frame, stars)

    # write output frame
    out.write(frame)

    i += 1

cap.release()
out.release()
cv2.destroyAllWindows()

print("Done!")