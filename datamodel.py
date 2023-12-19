#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


data = {
    'date': ['september', 'october', 'november', 'december', 'january', 'february'],
    'total sales': [5280000, 5501000, 5469000, 5480000, 5533000, 5554000],
    'target sales': [528000, 5500000, 5729000, 5968000, 6217000, 6476000],
    'ad costs': [1056000, 950400, 739200, 528000, 316800, 316800],
    'Unit price per ounce': [2.0, 2.0, 2.0, 1.9, 1.9, 1.9],
}


# In[3]:


df = pd.DataFrame(data)


# In[4]:


get_ipython().run_line_magic('matplotlib', 'inline')

# 한글 폰트 설정 (Windows 기준, Mac이나 Linux 사용자는 폰트 경로를 적절히 수정)
plt.rcParams['font.family'] = 'Malgun Gothic'

# 1. 과거 6개월 총 매출 추이 시각화
plt.figure(figsize=(10, 6))
sns.lineplot(x='date', y='total sales', data=df, marker='o', label='total sales')
plt.title('total sales')
plt.show()

# 2. 목표 매출과 비교
plt.figure(figsize=(10, 6))
sns.lineplot(x='date', y='total sales', data=df, marker='o', label='total sales')
sns.lineplot(x='date', y='target sales', data=df, marker='o', label='target sales')
plt.title('total sales and target sales')
plt.legend()
plt.show()

# 3. 광고 비용과 소셜네트워크 비용 비교
plt.figure(figsize=(10, 6))
sns.lineplot(x='date', y='ad costs', data=df, marker='o', label='ad costs')
plt.title('ad costs')
plt.show()

# 4. 1온스별 단가 변화 확인
plt.figure(figsize=(10, 6))
sns.lineplot(x='date', y='Unit price per ounce', data=df, marker='o', label='Unit price per ounce')
plt.title('Unit price per ounce')
plt.show()


# In[5]:


sns.lineplot(x='date', y='total sales', data=df, marker='o', label='total sales')
sns.lineplot(x='date', y='total sales', data=df, marker='o', label='total sales')
sns.lineplot(x='date', y='target sales', data=df, marker='o', label='target sales')
sns.lineplot(x='date', y='ad costs', data=df, marker='o', label='ad costs')
sns.lineplot(x='date', y='Unit price per ounce', data=df, marker='o', label='Unit price per ounce')
plt.show()


# In[ ]:




