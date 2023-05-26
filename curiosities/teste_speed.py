import speedtest
import time


# instanciar speedtest em uma variavel
speed = speedtest.Speedtest()
seg = 10

print("aguarde enquanto calculamos")

download = speed.download() 
upload = speed.upload()
ping = speed.results.ping


# RESULT
print(type(download))
print(type(upload))
print(type(ping))
print(f'DOWNLOAD: {download / (10**6):.2f} Mbps')
print(f'UPLOAD: {upload / (10**6):.2f} Mbps')
print(f'PING: {ping:.2f} ms')
