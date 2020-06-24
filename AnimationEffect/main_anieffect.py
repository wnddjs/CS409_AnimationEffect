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
from modules.back_stagelight import back_stagelight_effect
from modules.color_outline import outline_effect
from modules.color_outline_black import black_outline_effect
from modules.foot3_module import foot3_effect
from modules.foot2_module import foot2_effect
from modules.foot_module import foot_effect

in_video_path = '../../itzy_dala.mp4'
out_video_path = '../../Demo_01.mp4'

cap = cv2.VideoCapture(in_video_path)
back_cap = cv2.VideoCapture(in_video_path)

width = int(cap.get(3))
height = int(cap.get(4))
fps = cap.get(cv2.CAP_PROP_FPS)

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

    if i > len(in_video.frames)-1:
        break

    #Skip the unrecognized frame
    if in_video.frames[i] == 'empty_frame':
        out.write(frame)
        i += 1
        continue
    
    # Short Test
    # if i > 2899 :
    #     break

    # if i < 1500 :
    #     i += 1
    #     continue
    # effect modules
    if i == 50:
        i, frame, back_frame = back_streak_effect(cap,frame, back_cap,back_frame, out, in_video, i)

    if i == 260:
        i, frame, back_frame = spark_effect(cap,frame, back_cap,back_frame, out, in_video, i)

    if i == 300:
        i, frame, back_frame = ribbon_effect(cap,frame, back_cap,back_frame, out, in_video, i)

    if i == 400:
        i, frame, back_frame = heart1_effect(cap,frame, back_cap,back_frame, out, in_video, i)

    if i == 430:
        i, frame, back_frame = foot_effect(cap,frame, back_cap,back_frame, out, in_video, i)

    if i == 540:
        i, frame, back_frame = fire_effect(cap,frame, back_cap,back_frame, out, in_video, i, 100)

    if i == 660:
        i, frame, back_frame = back_light3_effect(cap,frame, back_cap,back_frame, out, in_video, i)
    
    if i == 945:
        i, frame, back_frame = heart2_effects(cap,frame, back_cap,back_frame, out, in_video, i)

    if i == 1070:
        i, frame, back_frame = handneck_effect(cap,frame, back_cap,back_frame, out, in_video, i, 90)
    
    if i == 1225:
        i, frame, back_frame = handneck_effect(cap,frame, back_cap,back_frame, out, in_video, i, 24)

    if i == 1250:
        i, frame, back_frame = outline_effect(cap,frame, back_cap,back_frame, out, in_video, i)
    
    if i == 1430:
        i, frame, back_frame = back_glowing_effect(cap,frame, back_cap,back_frame, out, in_video, i)
    
    if i == 1650:
        i, frame, back_frame = heart1_effect(cap,frame, back_cap,back_frame, out, in_video, i)

    if i == 1740:
        i, frame, back_frame = mirrorball_effect(cap,frame, back_cap,back_frame, out, in_video, i)

    if i == 1821:
        i, frame, back_frame = fire_effect(cap,frame, back_cap,back_frame, out, in_video, i, 70)

    if i == 1925:
        i, frame, back_frame = heart1_effect(cap,frame, back_cap,back_frame, out, in_video, i)
    
    if i == 1940:
        i, frame, back_frame = heart1_effect(cap,frame, back_cap,back_frame, out, in_video, i)

    # if i == 2250:
    #     i, frame, back_frame = fire_effect(cap,frame, back_cap,back_frame, out, in_video, i, 100)

    # if i == 2000:
    #     i, frame, back_frame = black_outline_effect(cap,frame, back_cap,back_frame, out, in_video, i)

    # if i == 2500:
    #     i, frame, back_frame = back_light2_effect(cap,frame, back_cap,back_frame, out, in_video, i)
   
    # if i == 2600:
    #     i, frame, back_frame = heart1_effect(cap,frame, back_cap,back_frame, out, in_video, i)
   
    if i == 2100:
        i, frame, back_frame = wing_effect(cap,frame, back_cap,back_frame, out, in_video, i)

    if i == 2171:
        i, frame, back_frame = back_light4_effect(cap,frame, back_cap,back_frame, out, in_video, i)

    if i == 2400:
        i, frame, back_frame = handneck_effect(cap,frame, back_cap,back_frame, out, in_video, i, 150)

    if i == 2600:
        i, frame, back_frame = back_turnnel_effect(cap,frame, back_cap,back_frame, out, in_video, i)

    if i == 2800:
        i, frame, back_frame = mirrorball_effect(cap,frame, back_cap,back_frame, out, in_video, i)

    if i == 2900:
        i, frame, back_frame = handneck_effect(cap,frame, back_cap,back_frame, out, in_video, i, 140)
    
    if i == 3050:
        i, frame, back_frame = back_light2_effect(cap,frame, back_cap,back_frame, out, in_video, i)

    if i == 3300:
        i, frame, back_frame = back_stagelight_effect(cap,frame, back_cap,back_frame, out, in_video, i)

    if i == 3540:
        i, frame, back_frame = black_outline_effect(cap,frame, back_cap,back_frame, out, in_video, i, 90)

    if i == 3670:
        i, frame, back_frame = foot_effect(cap,frame, back_cap,back_frame, out, in_video, i)
    
    if i == 3700:
        i, frame, back_frame = foot_effect(cap,frame, back_cap,back_frame, out, in_video, i)

    if i == 3900:
        i, frame, back_frame = heart2_effects(cap,frame, back_cap,back_frame, out, in_video, i)

    if i == 4100:
        i, frame, back_frame = black_outline_effect(cap,frame, back_cap,back_frame, out, in_video, i, 10)

    if i == 4120:
        i, frame, back_frame = black_outline_effect(cap,frame, back_cap,back_frame, out, in_video, i, 10)

    if i == 4140:
        i, frame, back_frame = black_outline_effect(cap,frame, back_cap,back_frame, out, in_video, i, 150)
    
    if i == 4300:
        i, frame, back_frame = handneck_effect(cap,frame, back_cap,back_frame, out, in_video, i, 150)

    if i == 4451:
        i, frame, back_frame = back_light2_effect(cap,frame, back_cap,back_frame, out, in_video, i)

    if i == 4600:
        i, frame, back_frame = back_light_effect(cap,frame, back_cap,back_frame, out, in_video, i)


    # write output frame
    out.write(frame)

    i += 1

cap.release()
out.release()
cv2.destroyAllWindows()

print("Done!")

# add audio
my_clip = mpe.VideoFileClip(out_video_path)
audio_background = mpe.VideoFileClip(in_video_path)
my_clip.audio = audio_background.audio
my_clip.write_videofile(out_video_path[:-4]+'_result.mp4',
  codec='libx264', 
  audio_codec='aac', 
  temp_audiofile='temp-audio.m4a', 
  remove_temp=True)

my_clip.close()
audio_background.close()