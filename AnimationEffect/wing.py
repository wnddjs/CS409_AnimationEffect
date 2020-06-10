import cv2
import numpy as np
import math
from parser import in_video

in_video_path = '../../Naver_video_02.mp4'
#out_video_path = '../Result_Naver_video_01.mp4'
out_video_path = '../../test_wing.mp4'
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

def ani_effect(y,x,fr,effect):
    rows, cols, channels = effect.shape
    roi = fr[x:rows+x, y:cols+y]
    
    effect_gray = cv2.cvtColor(effect, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(effect_gray, 80 ,255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)

    fr_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
    effect_fg = cv2.bitwise_and(effect, effect, mask=mask)

    dst = cv2.add(fr_bg, effect_fg)
    fr[x:rows+x, y:cols+y] = dst

    return fr

ani_start = []
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
    if i > 1300 :
        break
    
    fr_humans = in_video.frames[i].humans

    for j in range(len(fr_humans)): 
        human_color = colors[fr_humans[j].id - 1]
    
        # anchor
        human_id = fr_humans[j].id - 1
        anchors = fr_humans[j].pose_pos
        
        left_shoulder = (anchors[5][0], anchors[5][1])
        right_shoulder = (anchors[6][0], anchors[6][1])

        # draw prepared img
        n = 82 # number of frames
        start = 1000
        if human_id == 2 :
            if start <= i < start+n :
                eff = cv2.imread('../../Effects/wing_left/animation_wing-'+str(i-start).zfill(4)+'.jpg')
                eff2 = cv2.imread('../../Effects/wing_right/animation_wing-'+str(i-start).zfill(4)+'.jpg')

                # resize
                sizing = 0.7
                eff = cv2.resize(eff, dsize=(0, 0), fx=sizing, fy=sizing, interpolation=cv2.INTER_AREA)
                eff2 = cv2.resize(eff2, dsize=(0, 0), fx=sizing, fy=sizing, interpolation=cv2.INTER_AREA)

                if (left_shoulder[0] < frame.shape[1] - eff.shape[1]) and (left_shoulder[1] < frame.shape[0] - eff.shape[0]):
                    frame = ani_effect(left_shoulder[0],left_shoulder[1]-eff.shape[0]//2, frame, eff)
                
                if (eff2.shape[1] < right_shoulder[0] < frame.shape[1]) and (right_shoulder[1] < frame.shape[0] - eff2.shape[0]):
                    frame = ani_effect(right_shoulder[0]-eff2.shape[1],right_shoulder[1]-eff2.shape[0]//2, frame, eff2)

            # frame = cv2.line(frame,left_shoulder,left_shoulder,human_color,9)
            # frame = cv2.line(frame,right_shoulder,right_shoulder,human_color,9)
                
    frame = cv2.addWeighted(back_frame,0.08,frame,0.92,0)

    # write output frame
    out.write(frame)

    i += 1

cap.release()
out.release()
cv2.destroyAllWindows()

print("Done!")