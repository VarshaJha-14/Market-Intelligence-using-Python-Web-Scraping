#!/usr/bin/env python
# coding: utf-8

# # IMDb Movie Analytics

# **Print the data of first 3 movies**
# 
# 
# From this link: https://www.imdb.com/search/title/?release_date=2018&sort=num_votes,desc&page=1&ref_=adv_nxt
# Find and print the name and genre of the first 3 titles
# Output Format :
# title_name_1 ; genre1_1, genre1_2 ..
# title_name_2 ; genre2_1, genre2_2 ..
# title_name_2 ; genre3_1, genre3_2 ..

# In[54]:


import requests 
from bs4 import BeautifulSoup as soup 

response=requests.get('https://www.imdb.com/search/title/?release_date=2018&sort=num_votes,desc&page=1&ref_=adv_nxt')
data=soup(response.text,'html.parser')
data


# In[55]:


count=0
liname=data.find_all(class_="lister-item-header")
ligenre=data.find_all(class_='genre')
d={}
for i in liname :
    if count==3:
        break 
    d[liname[count].a.text]=list(ligenre[count].stripped_strings)[0]  #to get name 
#     print(li[count].a.text)
    count+=1
# print(d)

for key,value in d.items():
    print(key,";",value)


# In[56]:


ligenre=data.find_all(class_='genre')  #to get genre as used abve 
list(ligenre[0].stripped_strings)[0]


# **titles with most votes**
# 
# Print the names of movies with highest number of votes from year 2010 to 2014
# Note : Print the titles line wise starting from year 2010
# Output Format :
# title_name_1
# title_name_2
# title_name_3
# .
# Link:https://www.imdb.com/search/title/?release_date=2018&sort=num_votes,desc&page=1&ref_=adv_nxt

# In[ ]:


#called link has already filtered as per number of votes 

response=requests.get('https://www.imdb.com/search/title/?release_date=2018&sort=num_votes,desc&page=1&ref_=adv_nxt')
data=soup(response.text,'html.parser')

#as you can see in the url release data =2018 we need to update the url as per our requirement so : 
#first firlter using release date you will get this link :https://www.imdb.com/search/title/?release_date=2018-01-01,2018-12-31&sort=release_date,desc
#now update the link as per your date 


# In[70]:


import requests
from bs4 import BeautifulSoup as soup

# Define the URL for IMDb's advanced search for movies released between 2010 and 2014, sorted by number of votes.
# base_url = "https://www.imdb.com/search/title/?release_date=2010-01-01,2014-12-31&sort=num_votes,desc&page="
#but note we only need top rated movie from each year so we can first visit filters for each ear and update based on number 
#of votes 
years=["2010","2011","2012","2013","2014"]
base_url="https://www.imdb.com/search/title/?"
for i in years:
    restofurl="release_date="+i+"&sort=num_votes,desc&page=1&ref_=adv_nxt"
    response=requests.get(base_url+restofurl)
    data=soup(response.text,'html.parser')
    ans=data.find_all(class_="lister-item-header")[0].a.text
    print(ans)




# **title with maximum duration**
# 
# Out of the first 250 titles with highest number of votes in 2018,find which title has the maximum duration.
# Output Format :
# title_name title_duration
# 
# link:https://www.imdb.com/search/title/?release_date=2018&sort=num_votes,desc&page=1&ref_=adv_nxt

# In[78]:


#each page has 50 so total page we need to call = 5, 5x50=250 for highest number of votes 
#then see maximum duration 
#first to get the runtime 

data.find_all(class_="runtime")[0].string
#need to convert it to int to compare properly


# In[88]:


#step calling all pages and comparing the runtime, keep the title which has max 

import requests 
from bs4 import BeautifulSoup as soup
import re 

base_url="https://www.imdb.com/"
current_page="search/title/?release_date=2018-01-01,2018-12-31&sort=num_votes,desc"
next_page_url=data.find(class_="lister-page-next next-page")["href"]
title=""
duration=0
for i in range(5):
    response=requests.get(base_url+current_page)
    data=soup(response.text,"html.parser")
    for j in range(50):
        runtime=data.find_all(class_="runtime")[j].string
        runtime=int(re.search('\d+',runtime).group())
        if runtime>duration:
            duration=runtime 
            runtime=0 
            title=data.find_all(class_="lister-item-header")[j].a.text #store the title as well if runtime is max 
print(title,duration)

    

