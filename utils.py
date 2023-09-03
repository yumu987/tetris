# import time

# def getCurrentTime():
#     t = time.time()
#     return int(t * 1000)

# def checkAndSetPressTime(self, key):
#     ret = False
#     if getCurrentTime() - self.pressTime.get(key, 0) > 30:
#         ret = True
#     self.pressTime[key] = getCurrentTime()
#     return ret

import time

def getCurrentTime():
    t = time.time()
    return int(t * 1000)
