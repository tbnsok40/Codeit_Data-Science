#!/usr/bin/env python
# coding: utf-8

# #### 파이썬이 데이터를 잘 다룰 수 있는 R의 장점을 가져옴. : Pandas
# #### pandas 는 numpy의 기능을 기초로 만들어졌다.
# #### pandas 는 표 형식 데이터 다루는데 좋아.
# 
# - 파이썬이 내 종교
# 

# DataFrame : 표형식의 데이터를 담는 자료형
# 
# pandas dataframe은 numpy array를 기반으로 만들어짐. 즉 numpy array에서 기능이 추가된 것.

# In[1]:


import pandas as pd


# In[2]:


two_dimensional_list = [['dongwook', 50, 86], ['sineui', 89, 31], ['ikjoong', 68, 91], ['yoonsoo',66,75]]


# In[5]:


my_df = pd.DataFrame(two_dimensional_list, columns = ['name', 'eng_score','math_score'], index = ['a','b','c','d'] )
my_df


# In[6]:


type(my_df)


# In[7]:


my_df.columns


# In[8]:


my_df.index


# In[11]:


# object 판다스의 문자열, int64는 숫자형
my_df.dtypes


# # DataFrame을 만드는 다양한 방법

# In[12]:


import numpy as np
import pandas as pd


# In[15]:


two_dimensional_list =[['dongwook', 50, 86], ['sineui', 89, 31], ['ikjoong', 68, 91], ['yoonsoo',66,75]]
two_dimensional_array = np.array(two_dimensional_list)
list_of_series = [
    pd.Series(['dongwook', 50, 86]),
    pd.Series(['sineui', 89, 31]), 
    pd.Series(['ikjoong', 68, 91]),
    pd.Series(['yoonsoo',66,75])
]

# 아래 셋은 모두 동일
df1 = pd.DataFrame(two_dimensional_list)
df2 = pd.DataFrame(two_dimensional_array)
df3 = pd.DataFrame(list_of_series)

print(df1)


# ### 파이썬 사전으로도 DataFrame을 만들 수 있다.

# In[17]:


names = ['dongwook', 'sineui', 'ikjoong', 'yoonsoo']
english_scores = [50, 89, 68, 88]
math_scores = [86, 31, 91, 75]

dict1 = {
    'name': names, 
    'english_score': english_scores, 
    'math_score': math_scores
}

dict2 = {
    'name': np.array(names), 
    'english_score': np.array(english_scores), 
    'math_score': np.array(math_scores)
}

dict3 = {
    'name': pd.Series(names), 
    'english_score': pd.Series(english_scores), 
    'math_score': pd.Series(math_scores)
}


# 아래 셋은 모두 동일합니다
df1 = pd.DataFrame(dict1)
df2 = pd.DataFrame(dict2)
df3 = pd.DataFrame(dict3)

print(df1)


# ### 사전이 담긴 리스트로도 DataFrame을 만들 수 있다.

# In[18]:


my_list = [
    {'name': 'dongwook', 'english_score': 50, 'math_score': 86},
    {'name': 'sineui', 'english_score': 89, 'math_score': 31},
    {'name': 'ikjoong', 'english_score': 68, 'math_score': 91},
    {'name': 'yoonsoo', 'english_score': 88, 'math_score': 75}
]

df = pd.DataFrame(my_list)
print(df)


# # Q. 스타들의 생일은 언제?
# 

# In[22]:


name = ['Taylor Swift',"Aaron Sorkin",'Harry Potter','Ji-Sung Park']
birthday = ['13-Dec-89','09-Jun-61','31-Jul-80','25-Feb-81']
occupation = ['Singer-songwriter','Screenwriter','Wizard','Footballer']

diction = {
    'name': name, 
    'birthday': birthday, 
    'occupation': occupation
}

df1 = pd.DataFrame(diction)
df1


# # pandas로 데이터 읽어들이기

# In[25]:


df = pd.read_csv('C:/codeit/iphone.csv')
df
# csv의 첫번째 줄을 자동으로 header로 인식한다.
# 헤더가 카테고리화 돼있지 않을 땐, header = None을 read_csv안에 써주어야 한다.


# In[29]:


df = pd.read_csv('C:/codeit/iphone.csv', index_col = 0)
#index column[0]을 row로 설정해주란 뜻
df


# # Q. dataFrame의 첫번째 컬럼을 인덱스로 바꾸는 법

# In[32]:


df = pd.read_csv('C:/codeit/mega_millions.csv', index_col = 0)
df
# index_col = 0을 알고 써란 뜻


# In[ ]:





# In[ ]:




