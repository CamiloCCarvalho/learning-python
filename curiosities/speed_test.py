import itertools
import threading
import time
import sys
import speedtest
from colorama import Fore, init

done = False
speed_test = speedtest.Speedtest()


#here is the animation
init()
def animate():
    for icon in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write(f'{Fore.CYAN}\rTesting your {Fore.GREEN}(Download: {icon} | Upload: {icon}) {Fore.CYAN}please wait.')
        sys.stdout.flush()
        time.sleep(0.1)
    print()
    sys.stdout.write(F'{Fore.BLUE}\rDone!     ')


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
print(f'DOWNLOAD: {Fore.GREEN}{download / (1024000):.2f} {Fore.MAGENTA}Mbps') # 1024000 or 10**6
print(f'{Fore.CYAN}UPLOAD: {Fore.GREEN}{upload / (1024000):.2f} {Fore.MAGENTA}Mbps')
print(f'{Fore.CYAN}PING: {Fore.GREEN}{ping:.2f} {Fore.MAGENTA}ms')
print(f'{Fore.CYAN}-------------------')
print('DADOS DETALHADOS')
print()
print(f'URL DO SERVIDOR: {Fore.BLUE}{url_local_server}')
print(f'{Fore.CYAN}LOCAL E OPERADORA (DO TESTE): {Fore.MAGENTA}{city}, {country} | {telecom}')
print(f'{Fore.CYAN}______________________')

done = True
