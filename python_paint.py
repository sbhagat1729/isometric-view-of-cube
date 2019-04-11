import time 
import pyautogui 
import math

# pause for 10 seconds
time.sleep(10)  

# coordinates of bottom right corner
end_x, end_y = (pyautogui.size())

start_x, start_y = end_x/2, end_y/2

# set size of cube
a=200

x=a*math.cos(math.pi/6)
y=a*math.sin(math.pi/6)

pyautogui.moveTo(start_x, start_y, duration = 1) 
pyautogui.dragRel(0, a, duration = 1) 
pyautogui.dragRel(x, -y, duration = 1) 
pyautogui.dragRel(0, -a, duration = 1) 
pyautogui.dragRel(-x, y, duration = 1) 
pyautogui.dragRel(-x, -y, duration = 1)
pyautogui.dragRel(0, a, duration = 1)
pyautogui.dragRel(x, y, duration = 1)
pyautogui.dragRel(0, -a, duration = 1)    
pyautogui.dragRel(x, -y, duration = 1) 
pyautogui.dragRel(-x, -y, duration = 1) 
pyautogui.dragRel(-x, y, duration = 1) 