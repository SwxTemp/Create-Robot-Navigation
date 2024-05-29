#!/usr/bin/env python

import rospy
from create_msgs.msg import DefineSong, PlaySong

def define_song_client():
    rospy.wait_for_service('/define_song')
    print("S: define song")
    try:
        define_song = rospy.ServiceProxy('/define_song', DefineSong)
        
        # Define the song
        song = DefineSong()
        song.song_number = 0  # Song number [0-3]
        song.length = 3  # Song length [1-16]
        song.notes = [60, 62, 64]  # Notes defined by MIDI note numbering scheme
        song.durations = [1.0, 1.0, 1.0]  # Durations in seconds
        
        response = define_song(song)
        return response
    except rospy.ServiceException as e:
        print("Service call failed: %s" % e)

def play_song_client(song_number):
    rospy.wait_for_service('/play_song')
    try:
        play_song = rospy.ServiceProxy('/play_song', PlaySong)
        response = play_song(song_number)
        return response
    except rospy.ServiceException as e:
        print("Service call failed: %s" % e)

if __name__ == '__main__':
    rospy.init_node('play_song_client_node')
    
    # Define the song
    response_define = define_song_client()
    print("Response from defining song: %s" % response_define)

    # Play the song
    song_number = 0  # Song number [0-3]
    response_play = play_song_client(song_number)
    print("Response from playing song: %s" % response_play)
