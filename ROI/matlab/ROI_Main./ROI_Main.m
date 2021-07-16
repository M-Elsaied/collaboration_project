function [ROI]=ROI_Main(I,Z)

d=dist(Z); %Eucledean Distance
Y = prctile(d,[35 50 85],2);
%(k-a)/(n+1-2a),a=0.4
nin=size(d,1);
NST=nin/2;  %stations number divided by 2
d2=sort(d,2,'ascend');
for i=1:50
    S(i,:)=d2(i,:)<=Y(i,1); %number of station at minimum 25% percentile
    Nsi(i,:)=sum(S(i,:))-1;  %minimum distance at 25% percentile
    D(i,:)=Y(i,1)+((Y(i,3)-Y(i,1))*((NST-Nsi(i,:))/(NST))); %main Eqn. to get the optimum distance
    S2(i,:)=d2(i,:)<=D(i,:);
    Ns(i,:)=sum(S2(i,:))-1; %Number of stations in ROI
    M(i,:)=d(i,:)<=D(i,:); %stations by their number in ROI
end


for i=I
    for j=1:50
        if M(i,j)==1;
            S_all(:,j)=Z(:,j);
        end
    end
    Ss=S_all(:,:);
    [nin,pin]=size(Ss);
    Ser=1:1:pin;                                        %Index for the number of cases
    Ss_ser=cat(1,Ser,Ss);
    Ss_ser(:,any(Ss_ser==0))=[];
    ROI=Ss_ser(1,:)';
    clear Ss nin pin Ser Ss_ser 
end  

for i=size(ROI,1):-1:1
    if ROI(i,1)==I;
        ROI(i,:)=[];
    end
end

