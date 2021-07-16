# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 17:34:46 2021

@author: a1
"""

import numpy as np

   
def zscore(A, size):
    B=np.zeros(shape=[A.shape[0],size])
    for j in range(size):
        mean=np.mean(A[:,j])
        std=np.std(A[:,j], ddof=1)
        
        for i in range(A.shape[0]):    
            B[i,j] = (A[i,j] - mean) / std
    return B


def dist(Z):
    D=np.zeros(shape=[Z.shape[0],Z.shape[0]])
    
    for i in range(Z.shape[0]):
        point1=Z[i,:]
        for j in range(Z.shape[0]):
            point2=Z[j,:]
            diff=point1 - point2
            D[i,j] =  np.sqrt(np.sum(diff*diff))
            
    return D
    

def ROI_Main(I,Z):
    d=dist(Z) #Eucledean Distance
    Z=np.transpose(Z)
    
    Y=np.transpose(np.percentile(d, [35, 50, 85], axis=1))
    
    nin=d.shape[0]
    NST=nin/2  #stations number divided by 2
    
    d2=np.zeros(shape=[d.shape[0],d.shape[1]])
    S =np.zeros(shape=[d.shape[0],d.shape[1]])
    Nsi=np.zeros(shape=[d.shape[0],d.shape[1]])
    D=np.zeros(shape=[d.shape[0],d.shape[1]])
    S2=np.zeros(shape=[d.shape[0],d.shape[1]])
    Ns=np.zeros(shape=[d.shape[0],d.shape[1]])
    M=np.zeros(shape=[d.shape[0],d.shape[1]])
    S_all=np.zeros(shape=[Z.shape[0],Z.shape[1]])
    #Ss=np.zeros(shape=[Z.shape[0],Z.shape[1]])
    
    for k in range(d.shape[0]):
        d2[k,:]=d[k, d[k, :].argsort()]
        
    for i in range(50):
        S[i,:]=d2[i,:]<=Y[i,0] #number of station at minimum 25% percentile
        Nsi[i,:]=np.sum(S[i,:])-1  #minimum distance at 25% percentile
        D[i,:]=Y[i,0]+((Y[i,2]-Y[i,0])*((NST-Nsi[i,:])/(NST)))  #main Eqn. to get the optimum distance
        S2[i,:]=d2[i,:]<=D[i,:]
        Ns[i,:]=sum(S2[i,:])-1   #Number of stations in ROI
        M[i,:]=d[i,:]<=D[i,:]  #stations by their number in ROI
    
  
    imax=0
    for j in range(50):
            if M[I,j] == 1:
                S_all[:,j]=Z[:,j]
                imax=j
      
    Ss=S_all[:,0:imax+1]
    pin=imax
             #Index for the number of cases
    row=np.zeros(shape=[1,pin+1])
    row[0,:]=range(1,(pin+2))
    Ss_ser=np.append(row, Ss, axis=0)
    idx = np.argwhere(np.any(Ss_ser[..., :] == 0, axis=0))
    Ss_ser=np.delete(Ss_ser, idx, axis=1)
    
    ROI=np.transpose(Ss_ser[0,:])
    Temp=ROI
    
    imax=0
    for jj in range(ROI.shape[0]):
        if ROI[jj] != I+1:
                Temp[imax]=ROI[jj]
                imax+=1
                
    ROI=Temp[0:imax]
    
    return ROI
    
XX = np.loadtxt( 'X.dat' )
Z=zscore(XX,13)

for i in range(50):
    locals()['ROI_'+str(i+1)]=ROI_Main(i,Z)
    

#ROI_1=ROI_Main(0,Z)
#ROI_2=ROI_Main(1,Z)
#ROI_3=ROI_Main(2,Z)
#ROI_4=ROI_Main(3,Z)
#ROI_5=ROI_Main(4,Z)
#ROI_6=ROI_Main(5,Z)
#ROI_7=ROI_Main(6,Z)
#ROI_8=ROI_Main(7,Z)
#ROI_9=ROI_Main(8,Z)
#
#ROI_10=ROI_Main(9,Z)
#ROI_11=ROI_Main(10,Z)
#ROI_12=ROI_Main(11,Z)
#ROI_13=ROI_Main(12,Z)
#ROI_14=ROI_Main(13,Z)
#ROI_15=ROI_Main(14,Z)
#ROI_16=ROI_Main(15,Z)
#ROI_17=ROI_Main(16,Z)
#ROI_18=ROI_Main(17,Z)
#ROI_19=ROI_Main(18,Z)
#ROI_20=ROI_Main(19,Z)
#
#ROI_21=ROI_Main(20,Z)
#ROI_22=ROI_Main(21,Z)
#ROI_22=ROI_Main(22,Z)
#ROI_24=ROI_Main(23,Z)
#ROI_25=ROI_Main(24,Z)
#ROI_26=ROI_Main(25,Z)
#ROI_27=ROI_Main(26,Z)
#ROI_28=ROI_Main(27,Z)
#ROI_29=ROI_Main(28,Z)
#ROI_30=ROI_Main(29,Z)
#
#ROI_31=ROI_Main(30,Z)
#ROI_32=ROI_Main(31,Z)
#ROI_33=ROI_Main(32,Z)
#ROI_34=ROI_Main(33,Z)
#ROI_35=ROI_Main(34,Z)
#ROI_36=ROI_Main(35,Z)
#ROI_37=ROI_Main(36,Z)
#ROI_38=ROI_Main(37,Z)
#ROI_39=ROI_Main(38,Z)
#
#ROI_40=ROI_Main(39,Z)
#ROI_41=ROI_Main(40,Z)
#ROI_42=ROI_Main(41,Z)
#ROI_43=ROI_Main(42,Z)
#ROI_44=ROI_Main(43,Z)
#ROI_45=ROI_Main(44,Z)
#ROI_46=ROI_Main(45,Z)
#ROI_47=ROI_Main(46,Z)
#ROI_48=ROI_Main(46,Z)
#ROI_49=ROI_Main(48,Z)
#
#ROI_50=ROI_Main(49,Z)






