import cv2
import os
import argparse
import sys

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Capture frames from an MP4 video file.')
parser.add_argument('input_file', metavar='input_file', type=str, help='path to the input MP4 file')
parser.add_argument('num_frames', metavar='num_frames', type=int, help='number of frames to capture')
args = parser.parse_args()

# Check if the input file exists
if not os.path.isfile(args.input_file):
    print(f"Error: The input file '{args.input_file}' does not exist.")
    exit(1)

# Check if the number of frames is positive
if args.num_frames <= 0:
    print("Error: The number of frames must be positive.")
    exit(1)

# Check if the correct number of arguments was provided
if len(sys.argv) != 3:
    print("Error: Invalid number of arguments.")
    print("Usage: python capture_frames.py input_file num_frames")
    exit(1)

# Open the MP4 file using OpenCV
vidcap = cv2.VideoCapture(args.input_file)

# Get the frame rate and duration of the video
fps = vidcap.get(cv2.CAP_PROP_FPS)
duration = vidcap.get(cv2.CAP_PROP_FRAME_COUNT) / fps

# Set the interval between frames to capture
interval = duration / args.num_frames

# Create a directory to store the screenshots
output_folder = os.path.splitext(args.input_file)[0]
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop through the frames and save the screenshots
for i in range(args.num_frames):
    # Set the time to capture the frame
    time = i * interval

    # Set the position of the video to the desired time
    vidcap.set(cv2.CAP_PROP_POS_MSEC, time * 1000)

    # Read the frame at the current position
    success, image = vidcap.read()

    # Save the frame as a JPEG file
    if success:
        cv2.imwrite(f"{output_folder}/frame{i:04d}.jpg", image)
