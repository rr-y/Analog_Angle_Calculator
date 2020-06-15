
def caculate_angel(hour, minute): 
    if (hour > 12 or minute > 60):
        return "incorrect input" 
    
    if (hour == 12): 
        hour = 0
        
    if (minute == 60): 
        minute = 0
    
    hour_angle = 0.5 * (hour * 60 + minute) 
    minute_angle = 6 * minute
    angle = abs(hour_angle - minute_angle)
    angle = min(360 - angle, angle)  
    
    return angle 

hour = 6
minute = 15

print(caculate_angel(12, 15))

