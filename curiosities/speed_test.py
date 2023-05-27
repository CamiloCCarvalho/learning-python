import itertools
import threading
import time
import sys
import speedtest

done = False
speed_test = speedtest.Speedtest()

#here is the animation
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rTesting your (Download | Upload) ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    print()
    sys.stdout.write('\rDone!     ')


t = threading.Thread(target=animate)
t.start()


#long process here
download = speed_test.download() 
upload = speed_test.upload()
ping = speed_test.results.ping


# RESULT
print()
print('______________________')
print(f'DOWNLOAD: {download / (1024000):.2f} Mbps')
print(f'UPLOAD: {upload / (1024000):.2f} Mbps')
print(f'PING: {ping:.2f} ms')
print('______________________')

done = True