import numpy as np
from scipy.fftpack import fft, dct, idct
from scipy import fft
a = [1,2,3,4,5,4,3,2,1]
########## 2D data construction ##################
data = list()
sum2D=list()
for i in range(9):
    if i <=4:
       b = [x+i for x in a]
       
    else:
        print(i, i%5)
        b = [x+3-(i-5) for x in a]
    sum1D = sum(b)
    data.append(b)
    sum2D.append(sum1D)
sum2Dvalue = sum(sum2D)/81
print("sum: {}".format(sum2Dvalue))
data = np.array(data)
###################################################

##### 1D DCT by using numpy fft package ##############
dct_result = dct(a,type = 2, norm=None)/9/2
print(dct_result)
######################################################

###### 1D DCT by manual ###################
manual = list()
for i in range(9):
    total = 0
    for idx, x in enumerate(a):
        y = x*np.cos((np.pi*(2*idx+1)*i/2/9))
        total += y 
    manual.append(total/9)
print(manual)
################################

###### 2D DCT by using numpy package ##################
print("dct 2D packaage")
dct2D = dct(dct(data.T,2, axis=0).T,2,axis=0)/2/2/9/9
print("\n")
print(dct2D.T)
#######################################################

############ 2D DCT by manual ####################### 
print("\n\n")
manual2D = list()
for j in range(9):
    row = list()
    for i in range(9):
        total = 0
        for y in range(9):
            for x in range(9):
                value = data[y][x]*np.cos(np.pi*(2*x+1)*i/2/9)*np.cos(np.pi*(2*y+1)*j/2/9)
                total += value
        uij = total/9/9 
        row.append(uij)
    manual2D.append(row)
print(manual2D)
###########################################################################################
print("\n\n")
print("^^^^^^^^^^^^^^")


#print("dct result: {}".format(dct_result))
dct_result = [ 30, -8, -6, 2, -6, -8, 30]
#dct_result = [1,1,1,1]
idct1D = fft.idct(dct_result,3)
print(idct1D)
idct1D = idct(dct_result,type=3)
print(idct1D)


idct_manual = list()
for x in range(len(dct_result)):
    total = 0
    for i in range(len(dct_result)):
        value = dct_result[i]*np.cos(np.pi*(2*i+1)*x/2/len(dct_result))
        total += value
    idct_manual.append(total/len(dct_result))
print(idct_manual)


dct_result = [ 30, -8, -6, 2]
idct1D = fft.idct(dct_result,3)
print(idct1D)
idct1D = idct(dct_result,type=3)/len(2*dct_result)
print(idct1D)


idct_manual = list()
for x in range(len(dct_result)):
    total = 0
    for i in range(len(dct_result)):
        value = dct_result[i]*np.cos(np.pi*(2*i+1)*x/2/len(dct_result))
        total += value
    idct_manual.append(total/len(dct_result))
print(idct_manual)



