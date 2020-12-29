import numpy as np
import math
import matplotlib.pyplot as plt
from scipy import signal
from scipy.io.wavfile import write


B_1=100
playingtime=0.5
F_0=220
F_s=16000

x=[]
y=[]
y_1=[]
y_2=[]
time=[]
total_samples=int(F_s*playingtime)

for i in range(0,total_samples):
	x.append(0)
	y.append(0)
	y_1.append(0)
	y_2.append(0)
	time.append(i)


i=0
count=0

while i<total_samples and count < int(F_0*playingtime):
	x[i]= 1;
	i=i+int(F_s/F_0);
	count+=1





# Input Parameters
F_1=300
F_2=870
F_3=2240



def response(x,y,F):
	r_i = np.exp(-B_1*3.142/F_s)	
	theta_i = 2*3.142*F/F_s
	denominator=[1,-2*r_i*math.cos(theta_i),r_i*r_i]
	y[0]=x[0] # impulse  
	y[1]= x[1]-y[0]*denominator[1]
	for i in range(2,total_samples):
		y[i] = x[i]-y[i-1]*denominator[1]-y[i-2]*denominator[2];
	return y



y=response(x,y,F_1)

y_1=response(y,y_1,F_2)

y_2=response(y_1,y_2,F_3)






plt.title('Impulse Train Response')
plt.plot(time[0:750], y_2[0:750]) 
plt.ylabel('Amplitude Vowel /u/ F_0 = 220 Hz')
plt.xlabel('Samples')
plt.savefig('Q4_u_220.png')

y_2 = np.array(y_2)
write('Q4_u_220.wav', F_s, y_2)
