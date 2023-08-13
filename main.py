import os # Make sure install OS package using "pip install os-sys"
import cv2 # Make sure to install OpenCV package using "pip install opencv-python"

videos_file_path = "C:\\Users\\nojood\\Desktop\\Videos_file" # Change the file path, and replace each \ with \\ (for windows users)

all_vid_resolution = {}

# Get the resolution of the videos in the file (Make sure ALL the file content are videos only)
for video in os.listdir(videos_file_path):
    # Get the path for each video
    video_path = videos_file_path+"\\"+video
   
    vid = cv2.VideoCapture(video_path)
    height = vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
    width = vid.get(cv2.CAP_PROP_FRAME_WIDTH)
    resolution = str(width) +" X "+ str(height)
    print(f"The video {video} resolution is {resolution}")

    #store all the resolutions (Optional)
    all_vid_resolution[video] = resolution


# Print all videos resolution stored in the dictionary (Optional)
print(all_vid_resolution)