import re
def timeToEat(currentTimeStr: str) -> tuple[int, int]:
    MEALS_TIMES = {7.0,12.0,19.0} # breakfast, lunch, dinner

    try:
        match = re.match(r"(\d{1,2}):(\d{2})", currentTimeStr, re.IGNORECASE) # get hours and minutes
        if match:
            currentHours = float(match.group(1))
            currentMinute = float(match.group(2))
        else:
            raise ValueError("Invalid time format")
        
        currentTime = currentHours + (currentMinute / 60) # convert to decimal hours

        # meridian indicator (period)
        if re.search(r"p.m.", currentTimeStr.replace(" ",""), re.IGNORECASE) and currentTime != 12: # post meridiem
            currentTime += 12
        elif re.search(r"a.m.", currentTimeStr.replace(" ",""), re.IGNORECASE) and currentTime == 12: # ante meridiem
            currentTime = 0

        res = float('inf') # set to infinity to find the minimum difference
        for mealTime in MEALS_TIMES: # find the closest meal time 
            res = min(res, abs(currentTime - mealTime))
        
        return (abs(int(res)), abs(int((res - int(res)) * 60))) # convert to hours and minutes
    
    except Exception as e:
        print(f"Error: {e}")
        return None