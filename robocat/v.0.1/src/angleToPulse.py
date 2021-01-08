#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 16:27:16 2020

@author: miguel-asd

modified on Jan 08 2021 by Aiyyskhan
"""
import numpy as np

# def convert(FR_angles, FL_angles, BR_angles, BL_angles):
# 	pulse = np.empty([12])
# 	#FR
# 	pulse[0] = int(-10.822 * np.rad2deg(-FR_angles[0])) + 950
# 	pulse[1] = int(-10.822 * np.rad2deg(FR_angles[1])) + 2280
# 	pulse[2] = int(10.822 * (np.rad2deg(FR_angles[2]) + 90)) + 1000
# 	#FL
# 	pulse[3] = int(10.822 * np.rad2deg(FL_angles[0])) + 1020 
# 	pulse[4] = int(10.822 * np.rad2deg(FL_angles[1])) + 570
# 	pulse[5] = int(-10.822 * (np.rad2deg(FL_angles[2]) + 90)) + 1150
# 	#BR
# 	pulse[6] = int(10.822 * np.rad2deg(-BR_angles[0])) + 1060 
# 	pulse[7] = int(-10.822 * np.rad2deg(BR_angles[1])) + 2335 
# 	pulse[8] = int(10.822 * (np.rad2deg(BR_angles[2]) + 90)) + 1200
# 	#BL
# 	pulse[9] = int(-10.822 * np.rad2deg(BL_angles[0])) + 890
# 	pulse[10] = int(10.822 * np.rad2deg(BL_angles[1])) + 710
# 	pulse[11] = int(-10.822 * (np.rad2deg(BL_angles[2]) + 90)) + 1050
# 	return pulse

def angle2pulse(angle, a_min, a_max, p_min, p_max):
	return int((angle - a_min) * (p_max - p_min) / (a_max - a_min) + p_min)

def convert(FR_angles, FL_angles, BR_angles, BL_angles):
	a_min = 0
	a_max = 180
	p_min = 500
	p_max = 2500

	pulse = np.empty([12])
	#FR
	pulse[0] = angle2pulse(FR_angles[0], a_min, a_max, p_min, p_max)
	pulse[1] = angle2pulse(FR_angles[1], a_min, a_max, p_min, p_max)
	pulse[2] = angle2pulse(FR_angles[2], a_min, a_max, p_min, p_max)
	#FL
	pulse[3] = angle2pulse(FL_angles[0], a_min, a_max, p_min, p_max)
	pulse[4] = angle2pulse(FL_angles[1], a_min, a_max, p_min, p_max)
	pulse[5] = angle2pulse(FL_angles[2], a_min, a_max, p_min, p_max)
	#BR
	pulse[6] = angle2pulse(BR_angles[0], a_min, a_max, p_min, p_max)
	pulse[7] = angle2pulse(BR_angles[1], a_min, a_max, p_min, p_max)
	pulse[8] = angle2pulse(BR_angles[2], a_min, a_max, p_min, p_max)
	#BL
	pulse[9] = angle2pulse(BL_angles[0], a_min, a_max, p_min, p_max)
	pulse[10] = angle2pulse(BL_angles[1], a_min, a_max, p_min, p_max)
	pulse[11] = angle2pulse(BL_angles[2], a_min, a_max, p_min, p_max)

	return pulse