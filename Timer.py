'''
Create a timer in python starting from 00:00:00. The timer should pause/resume if interrupted by keyboard.
'''

import time
def timer():
    for i in range(12):
        for j in range(60):
            for k in range(60):
                try:
                    print(f"{i:02d}:{j:02d}:{k:02d}")
                    time.sleep(0.4)
                except KeyboardInterrupt:
                    input('\nPress any key to resume\n')

timer()
