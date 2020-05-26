import cv2
import numpy as np
import math
from parser import in_video
import sympy

in_video_path = '../../Naver_video_02.mp4'
#out_video_path = '../Result_Naver_video_01.mp4'
out_video_path = '../../test_0524_1.mp4'
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
    if i > 1000 :
        break

    fr_humans = in_video.frames[i].humans
    
    print(i)
    if i < 500 :
        i += 1
        continue
    # Draw a point for each person.
    for j in range(len(fr_humans)):
        human_color = colors[fr_humans[j].id - 1]
    
        # handneck anchor
        human_id = fr_humans[j].id - 1
        anchors = fr_humans[j].pose_pos

        # # Arm 5~10
        # for k in range(5,11):
        #     point = (anchors[k][0],anchors[k][1])
        #     frame = cv2.line(frame, point, point, human_color, 7)

        right_handneck = (anchors[10][0],anchors[10][1])
        left_handneck = (anchors[9][0],anchors[9][1])
        right_elbow = (anchors[8][0],anchors[8][1])
        left_elbow = (anchors[7][0],anchors[7][1])
        right_shoulder = (anchors[6][0],anchors[6][1])
        left_shoulder = (anchors[5][0],anchors[5][1])

        #handneck
        x_1 = anchors[9][0]
        y_1 = anchors[9][1]
        x_2 = anchors[7][0]
        y_2 = anchors[7][1]

        if y_1 - y_2 == 0:
            break

        x = sympy.Symbol('x')
        y = sympy.Symbol('y')
    
        eq1 = ((x_1-x_2)/(y_2-y_1))*(x-x_1) + y_1 - y
        eq2 = 10 - ( ((x-x_1)**2) + ((y-y_1)**2) )**(1/2)

        result = sympy.solve((eq1,eq2), dict=True)
        point_1 = (int(result[0][x]),int(result[0][y]))
        point_2 = (int(result[1][x]),int(result[1][y]))

        #elbow
        x_1 = anchors[9][0]
        y_1 = anchors[9][1]
        x_2 = anchors[7][0]
        y_2 = anchors[7][1]

        if y_1 - y_2 == 0:
            break

        x = sympy.Symbol('x')
        y = sympy.Symbol('y')
    
        eq1 = ((x_1-x_2)/(y_2-y_1))*(x-x_2) + y_2 - y
        eq2 = 11 - ( ((x-x_2)**2) + ((y-y_2)**2) )**(1/2)

        result = sympy.solve((eq1,eq2), dict=True)
        point_3 = (int(result[0][x]),int(result[0][y]))
        point_4 = (int(result[1][x]),int(result[1][y]))

        #shoulder
        x_1 = anchors[5][0]
        y_1 = anchors[5][1]
        x_2 = anchors[7][0]
        y_2 = anchors[7][1]

        if y_1 - y_2 == 0:
            break

        x = sympy.Symbol('x')
        y = sympy.Symbol('y')
    
        eq1 = ((x_1-x_2)/(y_2-y_1))*(x-x_1) + y_1 - y
        eq2 = 12 - ( ((x-x_1)**2) + ((y-y_1)**2) )**(1/2)

        result = sympy.solve((eq1,eq2), dict=True)
        point_5 = (int(result[0][x]),int(result[0][y]))
        point_6 = (int(result[1][x]),int(result[1][y]))

        frame = cv2.line(frame,point_1 ,point_3 ,human_color,7)
        frame = cv2.line(frame,point_3 ,point_5 ,human_color,7)
        frame = cv2.line(frame,point_2 ,point_4 ,human_color,7)
        frame = cv2.line(frame,point_4 ,point_6 ,human_color,7)

        # frame = cv2.line(frame, left_handneck, left_elbow,human_color,20)
        # frame = cv2.line(frame, left_shoulder, left_elbow,human_color,20)
        # frame = cv2.line(frame, right_handneck, right_elbow,human_color,20)
        # frame = cv2.line(frame, right_shoulder, right_elbow,human_color,20)

        # # left handneck
        # point = (anchors[9][0], anchors[9][1]) 
        # left_hand[human_id].append(point)
        # if (len(left_hand[human_id])>10): # 1th~10th points tracked
        #     for k in range(1,10): 
        #         if -80 < (left_hand[human_id][k+1][0] - left_hand[human_id][k][0]) < 80: # To elimate bad point
        #             if  -80 < (left_hand[human_id][k+1][1] - left_hand[human_id][k][1]) < 80:
        #                 frame = cv2.line(frame, left_hand[human_id][k], left_hand[human_id][k+1], human_color, 2+k)
        #         left_hand[human_id][k] = left_hand[human_id][k+1]
        #     del left_hand[human_id][-1]

        # # right handneck
        # point = (anchors[10][0], anchors[10][1]) 
        # right_hand[human_id].append(point)
        # if (len(right_hand[human_id])>10):
        #     for k in range(1,10):
        #         if -80 < (right_hand[human_id][k+1][0] - right_hand[human_id][k][0]) < 80:
        #             if -80 < (right_hand[human_id][k+1][1] - right_hand[human_id][k][1]) < 80: 
        #                 frame = cv2.line(frame, right_hand[human_id][k], right_hand[human_id][k+1], human_color, 2+k)
        #         right_hand[human_id][k] = right_hand[human_id][k+1]
        #     del right_hand[human_id][-1]

    ## opacity version ##
    # for k in range(1,11):
    #     for h in range(len(left_hand)):
    #         human_color = colors[h]
    #         if (len(left_hand[h])==12):
    #             if -40 < (left_hand[h][k+1][0] - left_hand[h][k][0]) < 40:
    #                     if  -40 < (left_hand[h][k+1][1] - left_hand[h][k][1]) < 40:
    #                         frame = cv2.line(frame, left_hand[h][k], left_hand[h][k+1], human_color, 1+k)
    #         if (len(right_hand[h])==12):
    #             if -40 < (right_hand[h][k+1][0] - right_hand[h][k][0]) < 40:
    #                     if -40 < (right_hand[h][k+1][1] - right_hand[h][k][1]) < 40: 
    #                         frame = cv2.line(frame, right_hand[h][k], right_hand[h][k+1], human_color, 1+k)
    #     frame = cv2.addWeighted(back_frame, 0.7-0.05*k, frame, 0.3+0.05*k, 0)

    # Give Opacity
    # frame = cv2.addWeighted(back_frame,0.4,frame,0.6,0)
    # write output frame
    out.write(frame)

    i += 1

cap.release()
out.release()
cv2.destroyAllWindows()

print("Done!")