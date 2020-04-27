import json

class Video():
    # def __init__(self, frame, behavior, hmcnt):
    #     frame = frame 
    #     behavior = behavior 
    #     hmcnt = hmcnt

    def __init__(self, name):
        with open(name) as json_file:
            json_string = json.load(json_file)
        json_data = json.loads(json_string)
        hum_cnt = 0

        for i in range(len(json_data)):
            boxes = json_data[str(i)]
            # if (len(boxes) == 0):
            #     continue
            humans = []
            for box_ind in boxes:
                each = Human(boxes[box_ind]['id'], i, boxes[box_ind]['pose_pos'])
                # print(boxes[box_ind]['pose_pos'])
                humans.append(each)
                # print(each)
            # print(frame.__dict__)
            # frames.append(Frame(i, humans))
            Frame(i, humans)
            # print(len(humans))
            if (hum_cnt < len(boxes)):
                hum_cnt = len(boxes)
        # return Video(Frame, Behavior, hum_cnt)
        self.frame = Frame
        self.behavior = Behavior
        self.hmcnt = hum_cnt

    def Track(self, bh, start, end):
        trk = []
        for frame_id in range(start, end):
            for human in Frame.get(frame_id).humans:
                li = [ human.pose_pos[anker] for anker in bh.akpnt]
                trk.append(json.dumps({'frame_id': human.frame_id, 'human_id': human.id, 'pose_pos': li}, sort_keys=True))
        return trk

class Behavior():
    instances = []
    def __init__(self, id, akpnt):
        self.id = id
        self.akpnt = akpnt #[ankerpoint_idx]
        Behavior.instances.append(self)

    @classmethod
    def get(cls, id):
        for inst in cls.instances:
            if (inst.id == id):
                return inst

class Human():
    def __init__(self, id, frame_id, pose_pos):
        self.id = id
        self.frame_id = frame_id
        self.pose_pos = pose_pos #[[x,y],..,]

class Frame():
    instances = []
    def __init__(self, id, humans):
        self.id = id
        self.humans = humans #[Human]
        #self.time
        Frame.instances.append(self)

    @classmethod
    def get(cls, id):
        for inst in cls.instances:
            if (inst.id == id):
                return inst
    @classmethod
    def getLength(cls):
        return len(cls.instances)
    


# def makeVideo(name):
#     with open(name) as json_file:
#         json_string = json.load(json_file)
#     json_data = json.loads(json_string)
#     hum_cnt = 0

#     for i in range(len(json_data)):
#         boxes = json_data[str(i)]
#         # if (len(boxes) == 0):
#         #     continue
#         humans = []
#         for box_ind in boxes:
#             each = Human(boxes[box_ind]['id'], i, boxes[box_ind]['pose_pos'])
#             # print(boxes[box_ind]['pose_pos'])
#             humans.append(each)
#             # print(each)
#         # print(frame.__dict__)
#         # frames.append(Frame(i, humans))
#         Frame(i, humans)
#         # print(len(humans))
#         if (hum_cnt < len(boxes)):
#             hum_cnt = len(boxes)
#     return Video(Frame, Behavior, hum_cnt)

# vd = makeVideo('../(G)I-DLE-01_matching.json')
# print (vd.frame.get(10).__dict__)



# print("generating json deserialization... ")
# with open('../(G)I-DLE-01_matching.json') as json_file:
#     json_string = json.load(json_file)

# json_data = json.loads(json_string)

# print("frame index ranges  from 0 to ", len(json_data))
# frame_ind = input("enter frame index: ")
# print("frame index ranges  from 1 to ", len(json_data[frame_ind]))
# box_ind =  input("enter frame index: ")
# print(json_data[frame_ind][box_ind])
# print (json_data['0']['1'])

# print ("frame length: ", len(json_data))
# # print (json_data['99']['1'])
# for i in range(len(json_data)):
#     each  = json_data[str(i)]
#     for j in json_data[str(i)]:
#         print (each[j])

frames = []
behaviors = []
hum_cnt = 0

# for i in range(len(json_data)):
#     boxes = json_data[str(i)]
#     # if (len(boxes) == 0):
#     #     continue
#     humans = []
#     for box_ind in boxes:
#         each = Human(boxes[box_ind]['id'], i, boxes[box_ind]['pose_pos'])
#         # print(boxes[box_ind]['pose_pos'])
#         humans.append(each)
#         # print(each)
#     # print(frame.__dict__)
#     frames.append(Frame(i, humans))
#     # print(len(humans))
#     if (hum_cnt < len(boxes)):
#         hum_cnt = len(boxes)

# Video(frames, behaviors, hum_cnt)
# print("number of humans in this video: ", hum_cnt)
# print(Frame.instances[0].__dict__)
# print(Frame.instances[0].id)
# print(Frame.instances[0].humans[0].frame_id)
# print(Frame.instances[0].humans[0].pose_pos)
# print (Frame.get(9).__dict__)

""" for example, behavior id 0 with anker point 9, 10 """
behaviors.append(Behavior(0, [9,10]))

""" for example, track motion for frame id 9~19, Behavior id 0 """
# for frame_id in range(9, 20):
#     for human in Frame.get(frame_id).humans:
#         print(human.frame_id)
#         print(human.id)
#         # print(human.pose_pos)
#         li = [ human.pose_pos[anker] for anker in Behavior.get(0).akpnt]
#         print (li)

# for anker in Behavior.get(0).akpnt:
#     # print(anker)
#     human.pose_pos[anker]

# def Track(bh, start, end):
#     trk = []
#     for frame_id in range(start, end):
#         for human in Frame.get(frame_id).humans:
#             li = [ human.pose_pos[anker] for anker in Behavior.get(bh).akpnt]
#             trk.append(json.dumps({'frame_id': human.frame_id, 'human_id': human.id, 'pose_pos': li}, sort_keys=True))
#     return trk


# print(Track(0, 9, 11))

# def getAnkpntInBehavior(idx):
#     return Behavior.get(idx).akpnt

# print (getAnkpntInBehavior(0))