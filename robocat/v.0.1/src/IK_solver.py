#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Jan 07 2021

@author: Aiyyskhan
"""
import numpy as np

#this is based on this paper: 
#"https://www.researchgate.net/publication/320307716_Inverse_Kinematic_Analysis_Of_A_Quadruped_Robot"
"""
"using pybullet frame"
"  z                     "
"    |                   "
"    |                   "
"    |    /  y           "
"    |   /               "
"    |  /                "
"    | /                 "
"    |/____________  x       "
"""
#IK equations now written in pybullet frame.


# ************* Front Legs *************

def leg_FR(coord, coxa_l, femur_l, tibia_l): 

	l1 = np.sqrt(coord[1]**2 + coord[2]**2) - coxa_l
	l2 = np.sqrt(coord[0]**2 + l1**2)

	alpha = np.rad2deg( (np.pi/2) - np.arctan(coord[1]/coord[2]) )
	beta = np.rad2deg( (np.pi/2) - np.arctan(coord[0]/l1) - np.arccos((l2**2 + femur_l**2 - tibia_l**2)/(2 * l2 * femur_l)) )
	gamma = np.rad2deg( np.arccos((femur_l**2 + tibia_l**2 - l2**2)/(2 * femur_l * tibia_l)) )

	angles = np.array([alpha, beta, gamma])

	return angles

def leg_FL(coord, coxa_l, femur_l, tibia_l):

	l1 = np.sqrt(coord[1]**2 + coord[2]**2) - coxa_l
	l2 = np.sqrt(coord[0]**2 + l1**2)

	alpha = np.rad2deg( (np.pi/2) - np.arctan(coord[1]/coord[2]) )
	beta = np.rad2deg( (np.pi/2) + np.arctan(coord[0]/l1) + np.arccos((l2**2 + femur_l**2 - tibia_l**2)/(2 * l2 * femur_l)) )
	gamma = np.rad2deg( np.pi - np.arccos((femur_l**2 + tibia_l**2 - l2**2)/(2 * femur_l * tibia_l)) )

	angles = np.array([alpha, beta, gamma])

	return angles


# ************* Back Legs **************

def leg_BR(coord, coxa_l, femur_l, tibia_l): 

	l1 = np.sqrt(coord[1]**2 + coord[2]**2) - coxa_l
	l2 = np.sqrt(coord[0]**2 + l1**2)

	alpha = np.rad2deg( (np.pi/2) + np.arctan(coord[1]/coord[2]) )
	beta = np.rad2deg( (np.pi/2) - np.arctan(coord[0]/l1) + np.arccos((l2**2 + femur_l**2 - tibia_l**2)/(2 * l2 * femur_l)) )
	gamma = np.rad2deg( np.pi - np.arccos((femur_l**2 + tibia_l**2 - l2**2)/(2 * femur_l * tibia_l)) )

	angles = np.array([alpha, beta, gamma])

	return angles

def leg_BL(coord, coxa_l, femur_l, tibia_l):

	l1 = np.sqrt(coord[1]**2 + coord[2]**2) - coxa_l
	l2 = np.sqrt(coord[0]**2 + l1**2)

	alpha = np.rad2deg( (np.pi/2) + np.arctan(coord[1]/coord[2]) )
	beta = np.rad2deg( (np.pi/2) + np.arctan(coord[0]/l1) - np.arccos((l2**2 + femur_l**2 - tibia_l**2)/(2 * l2 * femur_l)) )
	gamma = np.rad2deg( np.arccos((femur_l**2 + tibia_l**2 - l2**2)/(2 * femur_l * tibia_l)) )

	angles = np.array([alpha, beta, gamma])

	return angles