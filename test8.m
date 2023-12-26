clc;clear;close all;format short g;format compact
a=0.7;
I=imread('lenatest.jpg');
if size(I,3)==3
I=rgb2gray(I);end
[m n]=size(I); 
subplot(351), imshow(I) ,title('原图像')
In=imnoise(I,'salt & pepper',a);
Rand=uint8(255*rand(size(I)));
In(In==0|In==255)=Rand(In==0|In==255);
subplot(352),imshow(In),title(['随机值脉冲噪声图像,PSNR=' num2str(psnr(I,In))]);
Jmed=medfilt2(In,[3,3],'symmetric'); 
subplot(353), imshow(Jmed),title(['中值滤波输出图像,PSNR=' num2str(psnr(I,Jmed))]);
[pmed,pmed2]=psnr(I,Jmed); %PSNR
%一种基于开关型中值滤波的随机脉冲噪声去除方法 SWM
T=11;
 
In=double(In); 
   % 噪声检测
    Noise=zeros(size(I));%取零矩阵作为噪声桌布
 for k=1:12
     Jmed=double(Jmed);   
       for i=2:m-1
       for j=2:n-1           
           blk=Jmed(i-1:i+1,j-1:j+1);%3*3检测窗口     
           blk(5)=[];%窗口中心设为空值
           AD=mean(abs(blk-In(i,j)));%邻域平均灰度差
           st=sort(blk);%升序排列该窗口
           AD1=mean(abs(st(1)-st(2:8)));%邻域像素与邻域最大值平均差
           AD2=mean(abs(st(8)-st(1:7)));%与最小值
           if  AD>T&(AD>AD1|AD>AD2) 
               Noise(i,j)=1; 
              
           end
       end
       end
     
    %噪声点的恢复；同时信号点保持不变
    J=In;
    for i=2:m-1
       for j=2:n-1    
           if Noise(i,j)==1
               blk=Jmed(i-1:i+1,j-1:j+1);%以当前像素为中心的Noise滤波窗口
               blk=blk(:);
               W=[1 2 1;2 0 2;1 2 1];
               W=W(:);
               blk = repelem(blk, W);
             J(i,j)=round(median(blk,'all'));
           end
       end
    end
  
   Jtemp=Jmed;
    Jtemp(2:m-1,2:n-1)=J(2:m-1,2:n-1);
    J=Jtemp;
    subplot(3,5,4), imshow(uint8(J)),title([  '12 次迭代的输出图像，PSNR=' num2str(psnr(I,uint8(J)))])
     Jmed=J;
     subplot(3,5,6),imhist(uint8(I)),title('原图直方图');
     subplot(3,5,7),imhist(uint8(J)),title('输出图像直方图');
  
   

   
 end