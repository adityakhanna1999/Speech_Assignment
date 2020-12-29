import numpy as np
import math
import matplotlib.pyplot as plt
from scipy import signal

# Input Parameters
F_1=900
B_1=200
F_s=16000

r_i = np.exp(-B_1*3.142/F_s)	
theta_i = 2*3.142*F_1/F_s
denominator=[1,-2*r_i*math.cos(theta_i),r_i*r_i]
numerator=[1]
w, h = signal.freqz(numerator,denominator)

# plt.title('Freq Response')
# plt.plot(F_s*w/(2*3.142), 20 * np.log10(abs(h)))
# plt.ylabel('Amplitude -- 20log(|H(e^jw)|)')
# plt.xlabel('Frequency')
# plt.savefig('Q1_1.png')


y=[]
time=[]
for i in range(0,300):
	y.append(0)
	time.append(i)
# print(time)
y[0]=1 # impulse  
y[1]= -y[0]*denominator[1]
for i in range(2,299):
	y[i] = -y[i-1]*denominator[1]-y[i-2]*denominator[2]; #x[i]=0
plt.title('Impulse Response')
plt.plot(time, y)
plt.ylabel('Amplitude')
plt.xlabel('Samples')
plt.savefig('Q1_2.png')
