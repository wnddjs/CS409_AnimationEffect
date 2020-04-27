import json
import numpy as np
from numpy import linalg

class Video():
    def __init__(self, frames, behaviors, hum_cnt):
        self.frames = frames #[Frame]
        self.behaviors = behaviors #[Behavior]
        self.hum_cnt = hum_cnt #number of humans

class Behavior():
    def __init__(self, id, akpnt):
        self.id = id
        self.akpnt = akpnt #[ankerpoint_idx]

class Human():
    def __init__(self, id, frame_id, pose_pos, box_pos):
        self.id = id
        self.frame_id = frame_id
        self.pose_pos = pose_pos #[[x,y],..,]
        self.box_pos = box_pos #[left, right, top, bottom]

class Frame():
    def __init__(self, id, humans, human_ind):
        self.id = id
        self.humans = humans #[Human]
        self.human_ind = human_ind
        self.human_motions = []
        self.human_motions_ind = []

class HumanMotion():
    def __init__(self, id, frame_id, pose_vector, top_point_ind, box_vector):
        self.id = id
        self.frame_id = frame_id
        self.pose_vector = pose_vector
        self.top_point_ind = top_point_ind
        self.box_vector = box_vector

anchor_points = ['nose', 'left_eye', 'right_eye', 'left_ear', 'right_ear', 'left_shoulder',
                'right_shoulder', 'left_elbow', 'right_elbow', 'left_wrist', 'right_wrist',
                'left_hip', 'right_hip', 'left_knee', 'right_knee', 'left_ankle', 'right_ankle']


def parse_json():
    print("generating json deserialization... ")
    with open('dance-effect-source/(G)I-DLE-01_matching.json') as json_file:
        json_string = json.load(json_file)

    json_data = json.loads(json_string)

    print("frame index ranges  from 0 to ", len(json_data))

    frames = []
    behaviors = []
    hum_cnt = 0
    for i in range(len(json_data)):
        boxes = json_data[str(i)]
        # if (i==100): print(boxes)
        if (len(boxes) == 0):
            continue
        humans = []
        human_ind = []
        for box_ind in boxes:
            human_box = boxes[box_ind]
            each = Human(human_box['id'], i, human_box['pose_pos'], human_box['box_pos'])
            # print(boxes[box_ind]['pose_pos'])
            humans.append(each)
            human_ind.append(boxes[box_ind]['id'])
            # print(each)
        frame = Frame(i, humans, human_ind)
        # print(frame.__dict__)
        frames.append(frame)
        # print(len(humans))
        if (hum_cnt < len(boxes)):
            hum_cnt = len(boxes)

    behaviors.append(Behavior(0, [9,10]))

    Video(frames, behaviors, hum_cnt)
    print(len(frames))
    return frames



# Calculate Human Motion Vectors
# Extract the most moved anchor point

def calculate_motion_vector(frames):
    for i in range(len(frames)):
        if (i == len(frames)-1): break
        frame = frames[i]
        frame_next = frames[i+1]

        human_motions = []
        human_motions_ind = []
        for h in frame.humans:
            if (h.id in frame_next.human_ind):
                h_next = frame_next.humans[frame_next.human_ind.index(h.id)]
                pose_vector = np.subtract(np.matrix(h_next.pose_pos), np.matrix(h.pose_pos))
                norm_pose_vector = linalg.norm(pose_vector, ord=2, axis=1)
                top_point_ind = np.argmax(norm_pose_vector)
                box_vector = np.subtract(np.matrix(h_next.box_pos), np.matrix(h.box_pos))

                human_motion = HumanMotion(h.id, frame.id, pose_vector.tolist(), top_point_ind, box_vector.tolist())
                human_motions.append(human_motion)
                human_motions_ind.append(h.id)

        frame.human_motions = human_motions
        frame.human_motions_ind = human_motions_ind


def print_top_anchor_of_member(frames, hid):
    for frame in frames:
        if (hid in frame.human_motions_ind):
            hind = frame.human_motions_ind.index(hid)
            hm = frame.human_motions[hind]

            if (frame.id < 100):
                print("frame: %d / top_anchor: %s" %(frame.id, anchor_points[hm.top_point_ind]))


def main():
    frames = parse_json()
    calculate_motion_vector(frames)
    print_top_anchor_of_member(frames, 1)


if __name__ == "__main__":
    main()