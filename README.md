# Hack-UCI-2018
Project from the hackathon Hack@UCI 2018

This is the program I worked on at the hackathon Hack@UCI during February 2018. It is inteded to be utilized with a Raspberry Pi 3 with a
camera module. The program is meant to be a security program that relies on facial recognition to determine if someone is a "whitelisted"
(ie a known person) or "blacklisted" (anyone not whitelisted). Upon detecting a blacklisted individual, the program sends out an email and/
or text alert to the registered user of the program and device. Unfortunately, the alert system is not fully implemented, however the 
facial recognition and deterministic capabilities are fully implemented and functional.

This program was created in Python using the OpenCV library, a Raspberry Pi 3 module with a camera attachment, and this open source
facial recognition library: https://github.com/ageitgey/face_recognition 
