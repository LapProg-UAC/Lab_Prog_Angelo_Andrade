import numpy as np                      
from scipy.fft import fft, fftfreq      
import matplotlib.pyplot as plt         

"""
Gera um sinal composto por duas frequências (50 Hz e 120 Hz), calcula a sua
FFT e guarda o gráfico do espectro de frequências como imagem PNG.
"""

fs = 1000                               
t = np.arange(0, 1, 1/fs)               


sinal = (np.sin(2*np.pi*50*t)               
    + 0.5*np.sin(2*np.pi*120*t))         



Y = np.abs(fft(sinal))                    


N = len(sinal)                            
freqs = fftfreq(N, 1/fs)                


half = N // 2                           
freqs_pos = freqs[:half]                
Y_pos = Y[:half] * 2 / N                

Y_pos[0] /= 2                           
if N % 2 == 0:                          
    Y_pos[-1] /= 2                      

plt.figure(figsize=(8, 4))              
plt.plot(freqs_pos, Y_pos, 'b-', linewidth=2)                   
plt.xlabel('Frequência (Hz)')           
plt.ylabel('Amplitude')                 
plt.title('FFT do sinal')               
plt.grid(True)                
plt.savefig("fft_resultado.png", dpi=300, bbox_inches='tight')          
plt.show()                              