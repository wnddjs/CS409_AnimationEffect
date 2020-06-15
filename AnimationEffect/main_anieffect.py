import cv2
import numpy as np
import math
import moviepy.editor as mpe
from parser import in_video
from modules.handneck_module import handneck_effect
from modules.heart1_module import heart1_effect
from modules.heart2_module import heart2_effect, heart2_effects
from modules.spark_module import spark_effect
from modules.fire_module import fire_effect
from modules.wing_module import wing_effect
from modules.ribbon_module import ribbon_effect
from modules.mirrorball import mirrorball_effect
from modules.back_streak import back_streak_effect
from modules.back_glowing import back_glowing_effect
from modules.back_light import back_light_effect
from modules.back_turnnel import back_turnnel_effect
from modules.back_light2 import back_light2_effect
from modules.back_light3 import back_light3_effect
from modules.back_light4 import back_light4_effect
from modules.color_outline import outline_effect
from modules.color_outline_black import black_outline_effect

in_video_path = '../../Naver_video_02.mp4'
out_video_path = '../../proto_01.mp4'

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
    # if i > 2400 :
    #     break

    # effect modules
    if i == 30:
        i, frame, back_frame = back_streak_effect(cap,frame, back_cap,back_frame, out, in_video, i)

    if i == 200:
        i, frame, back_frame = ribbon_effect(cap,frame, back_cap,back_frame, out, in_video, i)

    if i == 400:
        i, frame, back_frame = heart1_effect(cap,frame, back_cap,back_frame, out, in_video, i)
    
    if i == 500:
        i, frame, back_frame = back_turnnel_effect(cap,frame, back_cap,back_frame, out, in_video, i)

    if i == 610:
        i, frame, back_frame = back_light3_effect(cap,frame, back_cap,back_frame, out, in_video, i)
    
    if i == 800:
        i, frame, back_frame = heart2_effects(cap,frame, back_cap,back_frame, out, in_video, i)

    if i == 900:
        i, frame, back_frame = fire_effect(cap,frame, back_cap,back_frame, out, in_video, i, 80)

    if i == 1000:
        i, frame, back_frame = handneck_effect(cap,frame, back_cap,back_frame, out, in_video, i, 100)
  
    if i == 1150:
        i, frame, back_frame = wing_effect(cap,frame, back_cap,back_frame, out, in_video, i)
    
    if i == 1300:
        i, frame, back_frame = outline_effect(cap,frame, back_cap,back_frame, out, in_video, i)
    
    if i == 1450:
        i, frame, back_frame = back_glowing_effect(cap,frame, back_cap,back_frame, out, in_video, i)
    
    if i == 1750:
        i, frame, back_frame = back_light2_effect(cap,frame, back_cap,back_frame, out, in_video, i)

    if i == 2180:
        i, frame, back_frame = black_outline_effect(cap,frame, back_cap,back_frame, out, in_video, i)
    # write output frame
    out.write(frame)

    i += 1

cap.release()
out.release()
cv2.destroyAllWindows()

print("Done!")

# add audio
my_clip = mpe.VideoFileClip('../../proto_01.mp4')
audio_background = mpe.VideoFileClip('../../Naver_video_02.mp4')
my_clip.audio = audio_background.audio
my_clip.write_videofile('../../proto_02.mp4',
  codec='libx264', 
  audio_codec='aac', 
  temp_audiofile='temp-audio.m4a', 
  remove_temp=True)

my_clip.close()
audio_background.close()