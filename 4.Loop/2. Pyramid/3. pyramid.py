import time
import sys


for i in range(20):
    print("I am a Programmer",flush=True)
    time.sleep(1.0)


for n in range(0,10):
    
    print "-"

    sys.stdout.flush()

    time.sleep(1.0)