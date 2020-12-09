#!/usr/bin/python
#  _         _                 
# | |_  ___ | |_  __ _  _ __  _ __
# | __|/ __|| __|/ _` || '__|| '__|
# | |_ \__ \| |_| (_| || |   | |
#  \__||___/ \__|\__,_||_|   |_|
#
# Description: Custom youtube-dl audio script with notification that
#              download has started and finished.
# Author: Tyler Starr
# Date Created: 7 November 2020
# https://github.com/starr-dusT/dotfiles
# Usage: youtube_dl_audio DIR_TO_SAVE_FILES LINK_TO_DOWNLOAD


# Import libraries
import youtube_dlc
import os
import sys


# Hook to send notification that download has finished
def my_hook(d):
    if d['status'] == 'finished':
        file_tuple = os.path.split(os.path.abspath(d['filename']))
        done_msg = "Audio download {} finished!".format(file_tuple[1])
        os.system("notify-send \'" + done_msg + "\'")


# Options for youtube-dl
ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': str(sys.argv[1]) + '%(title)s.%(ext)s',
    'noplaylist': 'True',
    'quiet': 'True',
    'progress_hooks': [my_hook],
}


# Send notification and start download
with youtube_dlc.YoutubeDL(ydl_opts) as ydl:
    os.system("notify-send \'Starting audio download...\'")
    meta = ydl.download([str(sys.argv[2])])
