# Line Following Robot

## Related Equipments
1. Arduino Micro Controller
2. Video Camera
3. Servomotor + Power Wheel

## Introduction
* The video camera is responsible for capturing the images and identifing the track position, judging whether the current situation should turn left, turn right or go straight.
* Arduino micro controller is responsible for controlling the servomotors, according to the different situations, let the two servomotors run in appropriate direction and speed.

## Current Problems
* Sometimes when encountering reflections, it will affect the processing of the image, causing the actually black areas to be judged as other colors and thus blocked by the mask. 
On the contrary, sometimes when encountering a shadow, it will be mistaken for the track and go wrong, but this problem is relatively small and can be solved by adjusting the parameters.
