# -*- coding: UTF-8 -*-
#这是主要的程序文件
import PCA
import openpicture
import numpy
from sklearn.cluster import KMeans
import arrange
import mPCA
a = 'test/'
imageData,addressList = openpicture.openPictures(a)
imageData,addressList=arrange.arrangeData(imageData,addressList)#排序
f=[]
dataShape=[]
for i in xrange(len(imageData)):
    z,ff = PCA.myPCA(imageData[i],128)
    z=z.T
    dataShape=z.shape
    z=z.reshape(1,128*dataShape[0])
    f.append(z)
f=numpy.array(f)
f=f.reshape(len(addressList),128*dataShape[0])
K_Means = KMeans(n_clusters=3).fit(f)
label=K_Means.labels_
number=0
number1=0
list1=[]
list0=[]
for i in xrange(len(label)):
    if label[i]:
        number=number+1
        list1.append(addressList[i])
    else:
        if addressList[i][3]=='1':
            number1=number1+1
        list0.append(addressList[i])
#print number
#print number1
#print len(label)
#print list0
#print list1
print label


