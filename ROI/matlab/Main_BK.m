%50 Catchemnets under study (Nile Delta Drainage catchments)

%Inputs: Data is prepared in dat files St_1.dat to St_50.dat(monthly records for NO3 = 1st col; NH4 = 2nd col and TP = 3rd col)
%Inputs: XX is the matrix of catchment attributes

XX=load ('X.dat');                   %XX is the matrix of catchment attributes 
% p=load('p.dat');                   %p is standardised data for catchments attributes
Z=zscore(XX(:,1:13));
ZS=zscore(XX(:,:));
%Outputs : 
%WQ_data (3-d matrix contain the data for the 50 catchments arranged as follows:
%1st dimension: raws represent the WQ monthly records
%2nd dimension: columns represent different WQ variables 
%3rd dimension: represents the 50 catchments

%WQ_Sort (3-d matrix == WQ_data, but data for each variable is sorted in an ascending order)

%P is the matrix of position associated with each record based on
%Empirical Equation (k-a)/(n+1-2a)
% a=0.4 
% n is the number of available cases (monthly records)
% k is the order of the record in the ascending order

%Prc is the matrix of percentiles computed for each of the WQ variables at each of gauged catchments
% 1st dimension: raws represent percentiles from 0.05 to 0.95
% 2nd dimension: columns represent different WQ variables
% 3rd dimension: represents the 50 catchments


for i=1:50         %50 is the number of catchments; for each catchment
    
    %--Load data files
    %-----------------
    load(['St_',num2str(i),'.dat'])   %download data "the data is saved in a dat file called St_1 to St_50
    X=eval(['St_',num2str(i)]);         %call the downloaded data matrix X     
    WQ_data(:,:,i)=X;                   %WQ_data is a matrix by all the data
    
      
    %--Percentile calculation at gauged sites
    %----------------------------------------
    for ii=1:size(X,2)
        X2=WQ_data(:,ii,i);
        X2=sort(X2,1,'ascend');               %sort the vector X in an acsending order 
        WQ_Sort(:,ii,i)=X2;                    % WQ_Sort is a matrix of WQ data sorted in ascending order
        n=size(X2,1);                           %n is the size of cases (monthly records)
        N(i,ii)=n;
        
        for iii=1:n;                         %for each record
            P(iii,ii,i)=(iii-0.4)/(n+0.2);           %get its position based on the Empirical Equation of (k-a)/(n+1-2a),a=0.4
            
        end             %P includes the percentiles associated with each station in col from 1 to 50
        m=1;
        for iii=0.25:0.25:0.75      %for each percentile from 0.05 to 0.95 (including 0.05 step) (0.05; 0.1;0.15;0.2;0.25;......0.85;0.9;0.95)
            ind=find( P(:,ii,i)<iii);       %find in P for the WQ variable under study (ii) for the catchment under study (i) cases with values less than the percentile to compute (iii in turn 0.05 then 0.1 then 0.15 and so on)
            index=ind(end,1);               % index is the index of the closest to the percentile value (just less than the percentile considered)
            sol1=(iii*WQ_Sort(index,ii,i)/P(index,ii,i));   %compute the percentile value as a ratio with the percentile associated with the smaller position
            sol2=(iii*WQ_Sort(index+1,ii,i)/P(index+1,ii,i)); %compute the percentile value as a ratio with the percentile associated witht the closer larger position
            wsol1=(1/(iii-P(index,ii,i)));                    %compute weight of the computed percentile based on the lower position
            wsol2=(1/(P(index+1,ii,i)-iii));                  %compute weight of the computed percentile based on the upper position
            Prc(m,ii,i)=((sol1*wsol1)+(sol2*wsol2))/(wsol1+wsol2);%compute a weighted average between the two computed percentiles; this will be the final results for this percentile (iii) for this WQvariable (ii) at this catchment (i)
                                                      %Prc is a mtarix of percentiles arranged as follows (1-d: raws represent percentiles from 0.05 to 0.95; 2-d: columns represent different WQ variables; and 3-d: represents the 50 catchments
            Y_Prc(i,m,ii)=Prc(m,ii,i);
            m=m+1;               
            clear ind index sol1 sol2 wsol1 wsol2          
        end
    end
        clear X X2 n m 
end

for i=1:50
    
    %--Identify neighbour catchments based on ROI approach
    %-----------------------------------------------------
    [ROI]=ROI_Main(i,Z');
    eval(['ROI_',num2str(i),'=','ROI',';']);   %ROI_ is a vector of neighbour catchments
   
    %--Identify best set of predictors
    %---------------------------------
    %for ii=1:3
      %  [inmodel]=Stepwise_Main(ZS,Y_Prc(:,:,ii),ROI);
      %  eval(['inmodel_',num2str(i),'_',num2str(ii),'=','inmodel',';']);   %ROI_ is a vector of neighbour catchments
       %     end
end
