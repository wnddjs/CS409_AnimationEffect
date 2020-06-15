import cv2
import numpy as np
import math

def ani_effect(y,x,fr,effect):
    rows, cols, channels = effect.shape
    roi = fr[x:rows+x, y:cols+y]
    
    effect_gray = cv2.cvtColor(effect, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(effect_gray, 230 ,255, cv2.THRESH_BINARY_INV)
    mask_inv = cv2.bitwise_not(mask)

    fr_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
    effect_fg = cv2.bitwise_and(effect, effect, mask=mask)

    dst = cv2.add(fr_bg, effect_fg)
    fr[x:rows+x, y:cols+y] = dst

    return fr

def heart2_effect (cap, frame, back_cap, back_frame, out, in_video, who, i) :
    
    print("heart2...")

    n = 19 # number of frames
    start = i
    ani_start = []
    std_heights = []
    while(cap.isOpened()):

        #Skip the unrecognized frame
        if in_video.frames[i] == 'empty_frame':
            i += 1
            continue

        # Short Test
        if i == start + n  :
            break

        fr_humans = in_video.frames[i].humans
        
        # no exist point
        if who > len(fr_humans)-1:
            break

        # Draw a point for each person.
        
        anchors = fr_humans[who].pose_pos
        
        # set position and size
        if i == start:
            std_height = int(0.3*(anchors[13][1]-anchors[2][1])) #  knee - eye
            std_heights.append(std_height) 
            ani_start.append((anchors[1][0], anchors[1][1]))
                
        for j in range(len(ani_start)):
            if start <= i < start+n :
                eff = cv2.imread('./Effects/heart_2/animation_heart_02-'+str(i-start).zfill(4)+'.jpg')
                eff = cv2.resize(eff, dsize=(eff.shape[1]*std_heights[j]//eff.shape[0], std_heights[j]), interpolation=cv2.INTER_LINEAR)
                
                if (ani_start[j][0] < frame.shape[1] - eff.shape[1]) and (eff.shape[0]//2 < ani_start[j][1] < frame.shape[0] - eff.shape[0]*2):
                    frame = ani_effect(ani_start[j][0]-eff.shape[1]//2, ani_start[j][1]+eff.shape[0], frame, eff)
                
        # Give Opacity
        # frame = cv2.addWeighted(back_frame,0.1,frame,0.9,0)

        # write output frame
        out.write(frame)
        i += 1

        #
        ret, frame = cap.read()
        back_ret, back_frame = back_cap.read() # original frame / It's for opacity

        if ret == False:
            print("Oops... ")
            break

        

    return i, frame, back_frame


def heart2_effects (cap, frame, back_cap, back_frame, out, in_video, i) :
    for j in range(in_video.hum_cnt):
        i, frame, back_frame = heart2_effect(cap,frame, back_cap,back_frame, out, in_video, j, i)
    return i, frame, back_frame