# -*- coding: utf-8 -*-
"""

"""
import numpy as np

reg=np.arange(0.25, 1,  0.25)
m=0
k=0
for i in range(50): #50
    X=np.loadtxt('St_'+str(i+1)+'.dat')  
    if X.shape[0]>m:
        m=X.shape[0]
    if X.shape[1]>k:
        k=X.shape[1]
        
WQ_data=np.zeros(shape=[m, k,50])
WQ_Sort=np.zeros(shape=[m, k,50])

P=np.zeros(shape=[k, 50 ,m])
Prc= np.zeros(shape=[k, 50,reg.shape[0]]) 
Y_Prc= np.zeros(shape=[50, reg.shape[0], k])
N=np.zeros(shape=[50,k])
    

for i in range(50): #50
    X=np.loadtxt('St_'+str(i+1)+'.dat')   #download data "the data is saved in a dat file called St_1 to St_50
                                        #call the downloaded data matrix X     
    
    
    WQ_data[:,:,i]=X;                   #WQ_data is a matrix by all the data


    ii=0
    
    for ii in range(X.shape[1]):
        
        
        X2=WQ_data[:,ii,i]
        idx=np.argsort(X2) #[1,3,0] are the **indices of the predicted sorted array**
        XX2=X2[idx] #boolean indexing which sorts the array on basis of indices saved in z
            #X2=sort(X2,1,'ascend');               %sort the vector X in an acsending order
         
        WQ_Sort[:,ii,i]=X2[idx]                    # WQ_Sort is a matrix of WQ data sorted in ascending order
        n=X2.shape[0]                             #n is the size of cases (monthly records)
        N[i,ii]=n
        #P=np.zeros(shape=[X.shape[1], i+1 ,n])
        
        for iii in range(0,n):                    #for each record
            P[ii,i, iii]=((iii+1)-0.4)/(n+0.2)           #get its position based on the Empirical Equation of (k-a)/(n+1-2a),a=0.4
                    
         #P includes the percentiles associated with each station in col from 1 to 50
        m=0 
        
        
        
        
        for iii in reg:      #for each percentile from 0.05 to 0.95 (including 0.05 step) (0.05; 0.1;0.15;0.2;0.25;......0.85;0.9;0.95)
                    #ind=find( P[:,ii,i]<iii);       #find in P for the WQ variable under study (ii) for the catchment under study (i) cases with values less than the percentile to compute (iii in turn 0.05 then 0.1 then 0.15 and so on)
                    ind = np.argwhere(P[ii,i,:]<iii) 
                    #print(ind)
                    
                    index=ind.shape[0]-1               # index is the index of the closest to the percentile value (just less than the percentile considered)
                    sol1=iii*WQ_Sort[index,ii,i]/P[ii,i, index]   #compute the percentile value as a ratio with the percentile associated with the smaller position
                    sol2=iii*WQ_Sort[index+1,ii,i]/P[ii,i,index+1] #compute the percentile value as a ratio with the percentile associated witht the closer larger position
                    wsol1=(1.0/(iii-P[ii,i,index]))                    #compute weight of the computed percentile based on the lower position
                    wsol2=(1.0/(P[ii,i,index+1]-iii))                  #compute weight of the computed percentile based on the upper position
                    Prc[ii,i,m]=((sol1*wsol1)+(sol2*wsol2))/(wsol1+wsol2)#compute a weighted average between the two computed percentiles; this will be the final results for this percentile (iii) for this WQvariable (ii) at this catchment (i)
                                                             #Prc is a mtarix of percentiles arranged as follows (1-d: raws represent percentiles from 0.05 to 0.95; 2-d: columns represent different WQ variables; and 3-d: represents the 50 catchments
                    Y_Prc[i,m,ii]=Prc[ii,i,m]
                    m=m+1              
            
