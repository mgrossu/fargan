# Author: mgrossu
# This script either converts images to compressed videos or extracts frames from videos
# Useful for preparing face compressed datasets for GAN training

import os
import argparse
import imageio
import cv2


def convert_images_to_videos(input_folder, output_folder, compression_standard='libx264', bitrate='1M', verbose=False):
    """Convert images in a folder to separate compressed videos"""
    img_count = 0
    os.makedirs(output_folder, exist_ok=True)

    for image_name in os.listdir(input_folder):
        if image_name.endswith((".jpg", ".png")):
            input_image_path = os.path.join(input_folder, image_name)
            frame = imageio.v2.imread(input_image_path)
            img_count += 1
            out_filename = os.path.join(output_folder, f"compressed_{img_count:07d}.mp4")
            writer = imageio.get_writer(out_filename, fps=30, codec=compression_standard, bitrate=bitrate)
            writer.append_data(frame)
            writer.close()
            if verbose:
                print(f"[CONVERT] Frame compressed and saved to {out_filename}")

def extract_frames(input_folder, output_folder, verbose=False):
    """Extract frames from videos in a folder"""
    frame_count = 0
    os.makedirs(output_folder, exist_ok=True)

    for video_name in os.listdir(input_folder):
        if video_name.endswith(".mp4"):
            video_path = os.path.join(input_folder, video_name)
            cap = cv2.VideoCapture(video_path)

            if not cap.isOpened():
                print(f"Error: Could not open video {video_path}")
                continue

            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                frame_count += 1
                frame_filename = os.path.join(output_folder, f"img_{frame_count:07d}.jpg")
                cv2.imwrite(frame_filename, frame)

            cap.release()
            if verbose:
                print(f"[EXTRACT] Frames from {video_name} saved to {output_folder}")

def main():
    parser = argparse.ArgumentParser(description="Prepare dataset: convert images to compressed videos or extract frames from videos")
    parser.add_argument("mode", choices=["convert", "extract"], help="Mode: 'convert' images to videos or 'extract' frames from videos")
    parser.add_argument("input_folder", help="Input folder path")
    parser.add_argument("output_folder", help="Output folder path")
    parser.add_argument("--compression_standard", default="libx264", help="Compression standard (default: libx264, only for convert mode)")
    parser.add_argument("--bitrate", default="1M", help="Bitrate like 32k, 128k, 1M (only for convert mode)")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    if args.mode == "convert":
        convert_images_to_videos(args.input_folder, args.output_folder, args.compression_standard, args.bitrate, args.verbose)
    elif args.mode == "extract":
        extract_frames(args.input_folder, args.output_folder, args.verbose)

if __name__ == "__main__":
    main()
