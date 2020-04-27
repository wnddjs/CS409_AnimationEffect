from parse import Behavior
from parse import Human
from parse import Frame
from parse import Video

""" initialize behavior """
clap = Behavior(0, [9,10])
raiseArm = Behavior(1, [0,1,4,7])

print (clap.akpnt)

""" initialize video """
video = Video('../(G)I-DLE-01_matching.json')

print ("There are ", video.hmcnt, "people in this video")
print ("There are ", len(video.frame.get(9).humans), "people in this frame")
print ("There are ", video.frame.getLength(), "frames")

""" track frame 99 ~ 101 by clap behavior """
print(video.Track(clap, 99, 101))

