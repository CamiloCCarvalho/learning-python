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
        sys.stdout.write(f'\rTesting your (Download: {c} | Upload: {c}) please wait.')
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
url_local_server = speed_test.results.server['url']
country = speed_test.results.server['country']
city = speed_test.results.server['name']
telecom = speed_test.results.server['sponsor']

# RESULT
print()
print('______________________')
print(f'DOWNLOAD: {download / (1024000):.2f} Mbps') # 1024000 or 10**6
print(f'UPLOAD: {upload / (1024000):.2f} Mbps')
print(f'PING: {ping:.2f} ms')
print('-------------------')
print('DADOS DETALHADOS')
print()
print(f'URL DO SERVIDOR: {url_local_server}')
print(f'LOCAL E OPERADORA (DO TESTE): {city}, {country} | {telecom}')
print('______________________')

done = True