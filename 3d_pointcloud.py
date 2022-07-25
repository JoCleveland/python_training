import cv2
import numpy as np
import matplotlib.pyplot as plt
from pyntcloud import PyntCloud
import pyrealsense2 as rs
print("Environment ready.")


pipe = rs.pipeline()
cfg  = rs.config()


# cfg.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
# cfg.enable_stream(rs.stream.color, 640, 480, rs.format.rgb8, 30)
# cfg.enable_record_to_file("test.bag")


cfg.enable_device_from_file("stairs.bag")


pipe.start(cfg)


for x in range (5):
    pipe.wait_for_frames()


frameset = pipe.wait_for_frames()
color_frame = frameset.get_color_frame()
depth_frame = frameset.get_depth_frame()


pipe.stop()
print("Frames captured.")


color = np.asanyarray(color_frame.get_data())
plt.rcParams["axes.grid"] = False
plt.imshow(color)


colorizer = rs.colorizer()
colorized_depth = np.asanyarray(colorizer.colorize(depth_frame).get_data())
plt.imshow(colorized_depth)


pc = rs.pointcloud()
pc.map_to(color_frame)
pointcloud = pc.calculate(depth_frame)
pointcloud.export_to_ply("Zero_degrees.ply", color_frame)
cloud = PyntCloud.from_file("Zero_degrees.ply")
cloud.plot()