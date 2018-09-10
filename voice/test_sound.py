import pyaudio
import numpy as np
import time

CHUNK = 2048
RATE = 44100

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16,channels=1,rate=RATE,input=True,
              frames_per_buffer=CHUNK)

start = time.time()

for i in range(int(100 * 44100 / CHUNK)): #go for 100 seconds
    data = np.fromstring(stream.read(CHUNK), dtype=np.int16)
    peak = np.average(np.abs(data)) * 2
    bars = "#" * int(50 * peak / 2**16)
    print("%04d %04d %05d %s" % (time.time() - start, i, peak, bars))

stream.stop_stream()
stream.close()
p.terminate()

