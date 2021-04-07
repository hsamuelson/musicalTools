#!/usr/bin/env python

'''
example to show optical flow
USAGE: opt_flow.py [<video_source>]
Keys:
 1 - toggle HSV flow visualization
 2 - toggle glitch
Keys:
    ESC    - exit
'''

# Python 2/3 compatibility
from __future__ import print_function

import numpy as np
import cv2 as cv
import video
# import winsound
import math
import pygame
import pygame.midi
import time
from time import sleep
import random


def draw_flow(img, flow, step=16):
    h, w = img.shape[:2]
    y, x = np.mgrid[step/2:h:step, step/2:w:step].reshape(2,-1).astype(int)
    fx, fy = flow[y,x].T
    lines = np.vstack([x, y, x+fx, y+fy]).T.reshape(-1, 2, 2)
    lines = np.int32(lines + 0.5)
    vis = cv.cvtColor(img, cv.COLOR_GRAY2BGR)
    cv.polylines(vis, lines, 0, (0, 255, 0))
    for (x1, y1), (_x2, _y2) in lines:
        cv.circle(vis, (x1, y1), 1, (0, 255, 0), -1)
    return vis


def draw_hsv(flow):
    h, w = flow.shape[:2]
    fx, fy = flow[:,:,0], flow[:,:,1]
    ang = np.arctan2(fy, fx) + np.pi
    v = np.sqrt(fx*fx+fy*fy)
    hsv = np.zeros((h, w, 3), np.uint8)
    hsv[...,0] = ang*(180/np.pi/2)
    hsv[...,1] = 255
    hsv[...,2] = np.minimum(v*4, 255)
    bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
    return bgr


def warp_flow(img, flow):
    h, w = flow.shape[:2]
    flow = -flow
    flow[:,:,0] += np.arange(w)
    flow[:,:,1] += np.arange(h)[:,np.newaxis]
    res = cv.remap(img, flow, None, cv.INTER_LINEAR)
    return res

def sigmoid(gamma):
  if gamma < 0:
    return 1 - 1/(1 + math.exp(gamma))
  else:
    return 1/(1 + math.exp(-gamma))

def norm(x):
    return (((x-100)/ 10000) * 3000) + 100
def nested_sum(L):
    total = 0  # don't use `sum` as a variable name
    for i in L:
        if isinstance(i, list):  # checks if `i` is a list
            total += nested_sum(i)
        else:
            total += i
    return total    

    
if __name__ == '__main__':
    import sys
    print(__doc__)
    try:
        fn = sys.argv[1]
    except IndexError:
        fn = 0

    cam = video.create_capture(fn)
    ret, prev = cam.read()
    prevgray = cv.cvtColor(prev, cv.COLOR_BGR2GRAY)
    show_hsv = False
    show_glitch = False
    cur_glitch = prev.copy()
    pygame.midi.init()
    player = pygame.midi.Output(0)
    # player.set_instrument(0)
    print("MADE IT HERE")
    port = pygame.midi.get_default_output_id()
    print("got here")
    print ("using output_id :%s:" % port)
    player.set_instrument(0)
    mega_counter = 0
    
    while True:
        ret, img = cam.read()
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        flow = cv.calcOpticalFlowFarneback(prevgray, gray, None, 0.5, 3, 15, 3, 5, 1.2, 0)
        prevgray = gray

        list_of_v_vals = list()
        new_num = nested_sum(flow)
        for i in range(0, len(new_num)):
            list_of_v_vals.append(abs(new_num[i][0] - new_num[i][1]))

        
        # avgg = sum_v / len_v
        avgg =  sum(list_of_v_vals) / len(list_of_v_vals)
        # print("STILL AVERAGE: " + str(avgg))
        val = int(norm(avgg)) + 37
        print(val)
        if val > 170: 
            # winsound.Beep(val, 100)
            # player.pitch_bend(val)
            player.note_on(val, 127)
            # sleep(0.05)
            # player.note_off(val,127)
            mega_counter += 1
            print("MEGA " +  str(mega_counter))
            # if mega_counter % 2000: print(mega_counter)
            #     player.note_off(val,127)
        
        #pygame midi 
        # val = int(sum(sum(sum(abs(flow))))) % (88)
        # player.note_on(val, 127)
        # time.sleep(1)
        # player.note_off(val, 127)

        cv.imshow('flow', draw_flow(gray, flow))
        if show_hsv:
            cv.imshow('flow HSV', draw_hsv(flow))
        if show_glitch:
            cur_glitch = warp_flow(cur_glitch, flow)
            cv.imshow('glitch', cur_glitch)

        ch = cv.waitKey(5)
        if ch == 27:
            break
        if ch == ord('1'):
            show_hsv = not show_hsv
            print('HSV flow visualization is', ['off', 'on'][show_hsv])
        if ch == ord('2'):
            show_glitch = not show_glitch
            if show_glitch:
                cur_glitch = img.copy()
            print('glitch is', ['off', 'on'][show_glitch])
    cv.destroyAllWindows()
