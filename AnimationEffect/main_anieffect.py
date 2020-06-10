import cv2
import numpy as np
import math
from parser import in_video
from modules.handneck_module import handneck_effect
from modules.heart1_module import heart1_effect
from modules.heart2_module import heart2_effect
from modules.spark_module import spark_effect
from modules.fire_module import fire_effect
from modules.wing_module import wing_effect

in_video_path = '../../Naver_video_02.mp4'
out_video_path = '../../test_0611_4.mp4'

cap = cv2.VideoCapture(in_video_path)
back_cap = cv2.VideoCapture(in_video_path)

width = int(cap.get(3))
height = int(cap.get(4))
fps = int(cap.get(cv2.CAP_PROP_FPS))

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(out_video_path, fourcc, fps, (width, height))

# video effect start
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
    if i > 1800 :
        break

    # effect modules
    if i == 1000:
        i, frame, back_frame = handneck_effect(cap,frame, back_cap,back_frame, out, in_video, i, 100)

    if i == 1300:
        i, frame, back_frame = handneck_effect(cap,frame, back_cap,back_frame, out, in_video, i, 300)

    if i == 200:
        i, frame, back_frame = heart1_effect(cap,frame, back_cap,back_frame, out, in_video, i)

    if i == 600:
        i, frame, back_frame = heart2_effect(cap,frame, back_cap,back_frame, out, in_video, i)

    if i == 400:
        i, frame, back_frame = spark_effect(cap,frame, back_cap,back_frame, out, in_video, i)

    if i == 800:
        i, frame, back_frame = fire_effect(cap,frame, back_cap,back_frame, out, in_video, i)

    if i == 1150:
        i, frame, back_frame = wing_effect(cap,frame, back_cap,back_frame, out, in_video, i)
    # write output frame
    out.write(frame)

    i += 1

cap.release()
out.release()
cv2.destroyAllWindows()

print("Done!")