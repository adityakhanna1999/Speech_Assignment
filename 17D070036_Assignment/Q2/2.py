import numpy as np
import math
import matplotlib.pyplot as plt
from scipy import signal
from scipy.io.wavfile import write

# Input Parameters
F_1=900
B_1=200
playingtime=0.5
F_0=140
F_s=16000

r_i = np.exp(-B_1*3.142/F_s)	
theta_i = 2*3.142*F_1/F_s
denominator=[1,-2*r_i*math.cos(theta_i),r_i*r_i]
numerator=[1]
w, h = signal.freqz(numerator,denominator)


#Impulse Response x[0]=1 else all 0
#y[n]+y[n-1]*-2*r*cos(theta_i)+r_i*r_i*y[n-2]=x[n]

x=[]
y=[]
time=[]

total_samples=int(F_s*playingtime)
for i in range(0,total_samples):
	x.append(0)
	y.append(0)
	time.append(i)


i=0
count=0
while i<total_samples and count < int(F_0*playingtime):
	x[i]= 1;
	i=i+int(F_s/F_0);
	count+=1


y[0]=1 # impulse  
y[1]= x[1]-y[0]*denominator[1]
for i in range(2,total_samples):
	y[i] = x[i]-y[i-1]*denominator[1]-y[i-2]*denominator[2];
plt.title('Impulse Train Response')
# plt.plot(time[0:500], y[0:500]) 
plt.plot(time, y) 
plt.ylabel('Amplitude')
plt.xlabel('Samples')
# plt.savefig('Q2_1.png')
plt.savefig('Q2_2.png')

y = np.array(y)
write('Q2_1.wav', F_s, y)
