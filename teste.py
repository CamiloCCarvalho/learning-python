import itertools
import threading
import time
import sys
import speedtest

done = False
speed = speedtest.Speedtest()

#here is the loading animation
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rTesting (Download | Upload) loading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDone!     ')

t = threading.Thread(target=animate)
t.start()

#long process here
download = speed.download() 
upload = speed.upload()
ping = speed.results.ping


#result
print()
print()
print(f'DOWNLOAD: {download / (10**6):.2f} Mbps')
print(f'UPLOAD: {upload / (10**6):.2f} Mbps')
print(f'PING: {ping:.2f} ms')
print()


#finish
done = True
