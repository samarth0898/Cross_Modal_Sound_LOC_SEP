#script to extract .mp3 and video frames

#
import os
# import cv2
import numpy as np
# import wave
# from random import randint, sample
# import torchvision.transforms as transforms
# import torch
import librosa
# from librosa import amplitude_to_db
# import math
# import matplotlib.pyplot as plt
import argparse
import soundfile as sf
import os
import sys
import cv2
from moviepy.editor import VideoFileClip
#
# def convert_video_to_audio_ffmpeg(video_file, output_ext="mp3"):
#     """Converts video to audio directly using `ffmpeg` command
#     with the help of subprocess module"""
#     filename, ext = os.path.splitext(video_file)
#     subprocess.call(["ffmpeg", "-y", "-i", video_file, f"{filename}.{output_ext}"], 
#                     stdout=subprocess.DEVNULL,
#                     stderr=subprocess.STDOUT)

def extractor(parent_dir,audio_dir,frames_dir):

    '''
    #convert videos to .mp4 file with rate=24, audio rate=44100 and audio channel=1
    vidlist=os.listdir(dirname)
    for vid in vidlist:
        src=os.path.join(dirname,vid)
        dst=os.path.join(dirname,new_name+'.mp4')
        cmd_str='ffmpeg -i '+dirname+'/'+vid+' -strict -2 -qscale 0 -r 24 -ar 44100 -ac 1 -y '+dirname+'/'+new_name+'.mp4'
        os.system(cmd_str)
        cmd_str='rm '+dirname+'/'+vid
        os.system(cmd_str)
    '''
    directories = os.listdir(parent_dir)
    sr=11000
    for direct in directories:
        current_direct=os.path.join(parent_dir,direct)
        files_list1=os.listdir(current_direct)
        new_directory=os.path.join(audio_dir,direct)
        if os.path.exists(new_directory) == False:
                os.mkdir(new_directory)
        
        for files1 in files_list1:
            sub_files=os.listdir(os.path.join(current_direct,files1))
            for files in sub_files:
                file_name=files1.split('.')[0]+'.wav'
                video_files=files1.split('.')[0]
                audio_data,sr = librosa.load(os.path.join(current_direct, files1,files))
                print(audio_dir,direct,file_name)
                write_path=os.path.join(audio_dir,direct,file_name)
                sf.write(write_path, audio_data, sr)

                if os.path.exists(os.path.join(frames_dir,direct,video_files)) == False: 
                    os.makedirs(os.path.join(frames_dir,direct,video_files))

                
                vidcap = cv2.VideoCapture(os.path.join(current_direct,files1,files))
                success,image = vidcap.read()
                count = 0
                while success:
                    cv2.imwrite(os.path.join(frames_dir,direct,video_files, str(count) + '.jpg'), image)    # save frame as JPEG file 
                    success,image = vidcap.read()     
                    count += 1

            
    print('Completed Pre-Processing')

    return None


    

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--root_path')
    parser.add_argument('--audio_write')
    parser.add_argument('--video_path')

    args = parser.parse_args()
    out=extractor(args.root_path,args.audio_write,args.video_path)
        
