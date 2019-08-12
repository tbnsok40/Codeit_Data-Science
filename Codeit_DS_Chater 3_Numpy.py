#!/usr/bin/env python
# coding: utf-8

# ### Numpy = Numerical + Python

# In[27]:


import numpy


# In[28]:


array1 = numpy.array([2,3,5,6,7,8,9,11,23,34,51])


# In[29]:


array1


# In[30]:


type(array1)
# numpy모듈의 array를 쓴 것이고


# In[31]:


array1.shape


# In[32]:


array2 = numpy.array([[1,2,3,4,],[5,6,7,8],[9,10,11,12]])


# In[33]:


type(array2)
# n-dimension array


# In[34]:


array2


# In[35]:


array2.shape


# In[36]:


array1.size


# In[37]:


array2.size


# In[39]:


# print로 출력해주면 리스트의 형태로 나온다
print(array1)


# In[41]:


array3 = numpy.full(6,8)
print(array3)
# 8이 6개로 나온다


# In[42]:


array1 = numpy.full(6,0)
array2 = numpy.zeros(6, dtype= int)


# In[45]:


# 모든 값이 0인 numpy array생성
print(array1)
print()
print(array2)


# In[46]:


# 모든 값이 1인 numpy array를 생성
array1 = numpy.full(6, 1)
array2 = numpy.ones(6, dtype=int)
    
print(array1)
print()
print(array2)


# In[48]:


# random 값들로 채우기 /  random 모듈 안의 random 함수를 사용
array1 = numpy.random.random(6)
array2 = numpy.random.random(6)
    
print(array1)
print()
print(array2)


# In[51]:


# arange(m) : 0부터 m-1까지 값들이 담긴 numpy arrange 리턴
array1 = numpy.arange(6)
print(array1)


# In[52]:


array1 = numpy.arange(2,7)
print(array1)


# In[53]:


array1 = numpy.arange(2,18,2)


# In[54]:


print(array1)


# # 모듈 별명 지어주기

# In[57]:


import numpy
import numpy as np
# 이런 별명을 붙여주는 것이 aliasing


# 
# import matplotlib.pyplot as plt
# 같이 matplotlib은 plt로 aliasing해준다.

# # Q. numpy array 생성 연습1
# 1부터 100까지 담겨있는 numpy array 생성/출력

# In[59]:


arr = np.arange(1,101)
print(arr)


# # Q. numpy array 생성 연습2
# 1부터 100까지 중 3의 배수만 담겨 있는 numpy array를 생성 출력

# In[61]:


arr = np.arange(1,100,3)
arr


# # Indexing, Slicing

# In[62]:


arr1 = np.array([2,3,4,6,7,8,9,10,12,14,15])


# In[64]:


arr1[-1]


# In[65]:


arr1[-3]


# In[67]:


arr1[[1,3,4]]


# In[69]:


arr2 = np.array([2,1,3])


# In[70]:


arr2


# In[72]:


arr1[arr2]
# Indexing


# In[74]:


arr1[2:7] 
#2번 인덱스부터 6번 인덱스까지 짤린다.


# In[75]:


arr1[0:7]


# In[76]:


arr1[:7]


# In[78]:


arr1[2:]


# In[80]:


arr1[2:11:2]
# 2번 인덱스에서 하나 씩 띄어 넘으면서 인덱스


# In[83]:


arr1 = np.arange(10)
arr2 = np.arange(10,20)
arr1


# In[84]:


arr2


# In[85]:


#numpy는 수치계산을 위한 도구


# In[87]:


arr1 * 2
# 이게 다여


# In[91]:


# 일반 파이썬 리스트에서 원소 값 2배 하려면
for i in range(len(arr1)):
    arr1[i] = 2* arr1[i]
arr1
# 이렇게 복잡한 반면 numpy사용하면 쉽게 계산 가능


# In[92]:


arr1 / 2


# In[93]:


arr1 + 2


# In[94]:


arr1 ** 2


# In[95]:


arr1


# In[96]:


arr1 = arr1 * 2 
# 이러면 원래 arr1값도 2배 되어 저장된다.


# In[97]:


arr1 * arr2


# In[98]:


arr1 + arr2


# In[99]:


# 지금 사용하는 numpy 연산들이 얼마나 편한지 느끼게 된다.


# # Q. 신주쿠 흥부 부대찌개
# 엔화로 저장한 매출 데이터를 원화로 변환하는 작업

# In[102]:


revenue_in_yen = [
    300000, 340000, 320000, 360000, 
    440000, 140000, 180000, 340000, 
    330000, 290000, 280000, 380000, 
    170000, 140000, 230000, 390000, 
    400000, 350000, 380000, 150000, 
    110000, 240000, 380000, 380000, 
    340000, 420000, 150000, 130000, 
    360000, 320000, 250000
]

revenue_in_yen = numpy.array(revenue_in_yen)

revenue_in_yen = revenue_in_yen * 10.08
revenue_in_yen


# # Q. 흥부부대찌개 LA진출
# 일본점과 LA점의 매출을 원화로 변환하여 합산하라.

# In[104]:


revenue_in_yen = [
    300000, 340000, 320000, 360000, 
    440000, 140000, 180000, 340000, 
    330000, 290000, 280000, 380000, 
    170000, 140000, 230000, 390000, 
    400000, 350000, 380000, 150000, 
    110000, 240000, 380000, 380000, 
    340000, 420000, 150000, 130000, 
    360000, 320000, 250000
]

revenue_in_dollar = [
    1200, 1600, 1400, 1300, 
    2100, 1400, 1500, 2100, 
    1500, 1500, 2300, 2100, 
    2800, 2600, 1700, 1400, 
    2100, 2300, 1600, 1800, 
    2200, 2400, 2100, 2800, 
    1900, 2100, 1800, 2200, 
    2100, 1600, 1800
]

yen = numpy.array(revenue_in_yen)
dol = numpy.array(revenue_in_dollar)
won = (yen*10.08) + (dol*1138)
won


# # Numpy 불린 연산

# In[105]:


arr1


# In[106]:


arr1 > 4


# In[107]:


arr1 % 2 == 0


# In[110]:


booleans = np.array([ True,  False,  True,  True,  False,  True,  True,  True,  True,
        True])


# In[111]:


np.where(booleans)


# In[112]:


arr1 > 4


# In[119]:


np.where(arr1>4)
# 4보다 큰 인덱스만 받아온다.


# In[128]:


filter = np.where(arr1> 4)
filter


# In[129]:


arr1[filter]
# [중요] 4보다 큰 원소만 받아와 출력


# # 부대찌개 목표 일 매출
# 20만엔 이하의 매출만 담긴 numpy array출력

# In[130]:


yen = [
    300000, 340000, 320000, 360000, 
    440000, 140000, 180000, 340000, 
    330000, 290000, 280000, 380000, 
    170000, 140000, 230000, 390000, 
    400000, 350000, 380000, 150000, 
    110000, 240000, 380000, 380000, 
    340000, 420000, 150000, 130000, 
    360000, 320000, 250000
]

yen = np.array(yen)
filter = (yen <= 200000)
bad_days_revenue = yen[filter]


# In[132]:


bad_days_revenue


# # numpy array vs python list
# 
# 굳이 numpy array를 쓰는 이유
# 1. 문법차이 : np arr 를 더하면 같은 인덱스의 해당하는 원소끼리 더함 / 반면 python list더하면 그냥 리스트를 갖다 잇는 효과만 나와
# 
# 2. 성능차이/ numpy가 빨라. 값들이 저장되는 방식의 차이에서 나오는 성능차
# 
# 3. 값을 추가하고 제거하는 일: 파이썬, 수치계산 많고 복잡할 때: numpy
# 

# # numpy 기본 통계

# In[142]:


import numpy as np
arr1 = np.array([4,14,56,3,25,3,15])

print('최댓값: ', arr1.max())
print
print('최솟값: ', arr1.min())

print('평균값: ', arr1.mean()) # 평균값

print('중앙값: ', np.median(arr1))
# 중앙값은 특이하게 numpy array의 메소드가 아닌 numpy의 메소드

print('표준편차: ', arr1.std()) # 표준 편차

print('분산: ', arr1.var()) # 분산


# In[ ]:




