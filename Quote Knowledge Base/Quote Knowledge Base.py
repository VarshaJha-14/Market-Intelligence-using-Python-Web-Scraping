#!/usr/bin/env python
# coding: utf-8

# # Quote Knowledge Base 

# **Quotes with tag humor**
# 
# Find all the quotes that have the tag as "humor" from this website
# Output Format :
# quote1
# quote2
# quote3
# .
# .
# .
# 
# link:https://quotes.toscrape.com/

# In[137]:


#to find tag
data.find_all(class_="tag")  #but this will not be parallel to count of quote since one quote has multiple tags so 
data.find_all(class_="keywords") #it has tags in content value !!
a=data.find_all(class_="keywords")[5]["content"]
#to get seperate string values
a.split(",")


# In[142]:


re.search("value",a).group() # to find the given 


# In[115]:


#to find quote 
data.find_all(class_="text")


# In[146]:


import requests 
import re
from bs4 import BeautifulSoup as soup 

response=requests.get("https://quotes.toscrape.com/")
data=soup(response.text,"html.parser")
#so now to get all tags named humor
quotelist=data.find_all(class_="text")
for i in range(len(quotelist)):
    keyword=data.find_all(class_="keywords")[i]["content"]
    if re.search("humor",keyword) is not None:
        print(data.find_all(class_="text")[i].string)
        
        
#but this is only for one page 
#all te quotes are asked so need to loop over all the availale pages 
#one more thing we can do is filter humor in link itself:https://quotes.toscrape.com/tag/humor/ 


# In[ ]:


import requests 
import re
from bs4 import BeautifulSoup as soup 

base_url="https://quotes.toscrape.com/tag/humor/"
response=requests.get(base_url)
i=1
while response.status_code==200:  #this won't work as all other pages are still loading no 404 error so just do it twice 
    
    current_page="page/"+str(i)+"/"
    response=requests.get(base_url+current_page)
    i=i+1
    data=soup(response.text,'html.parser')
    quotelist=data.find_all(class_="text")
    for i in range(len(quotelist)):
        print(data.find_all(class_="text")[i].string)

    


# In[3]:


import requests 
import re
from bs4 import BeautifulSoup as soup 

base_url="https://quotes.toscrape.com/tag/humor/"
response=requests.get(base_url)
i=1
while i<3: 
    
    current_page="page/"+str(i)+"/"
    response=requests.get(base_url+current_page)
    i=i+1
    data=soup(response.text,'html.parser')
    quotelist=data.find_all(class_="text")
    for k in range(len(quotelist)):
        print(data.find_all(class_="text")[k].string)


# **Print all authors**
# 
# Find and print the names of all the different authors from all pages of this website
# Note : Print the names of all authors line wise sorted in dictionary order
# Output Format :
# author1
# author2
# author3
# .
# .
# .
# link:https://quotes.toscrape.com/

# In[19]:


import requests
from bs4 import BeautifulSoup as soup 

dauthors={}
base_url="https://quotes.toscrape.com/"
#for fist page or homepage
response=requests.get(base_url)
data=soup(response.text,'html.parser')
#to find authors
for a in range(len(data.find_all(class_="quote"))):
    author=data.find_all(class_="quote")[a].find(class_="author").string
    #add it to dict to keep unique keys only 
    dauthors[author]=dauthors.get(author,0)


next_page=data.find(class_="next").a["href"]
#need to stop as soon as next button stops being visible so 
while next_page is not None:
    next_page_url=base_url+data.find(class_="next").a["href"]
    response=requests.get(next_page_url)
    data=soup(response.text,'html.parser')
    for a in range(len(data.find_all(class_="quote"))):
        author=data.find_all(class_="quote")[a].find(class_="author").string
        #add it to dict to keep unique keys only 
        dauthors[author]=dauthors.get(author,0)
    next_page=data.find(class_="next")

    
#need to sort in dict name 

sorted_keys = sorted(dauthors.keys())
for i in sorted_keys:
    print(i)


# **Birth Date of authors**
# 
# Find the birth date of authors whose name start with 'J' from this website
# Note : Print a dictionary containing the name as key and the birth date as value.The Names of authors should be alphabetically sorted.
# Output Format :
# {'author_1': 'month day, year', 'author_2': 'month day, year', ....}
# 
# link:https://quotes.toscrape.com/  
# 

# In[20]:


#need to first check if name start with a then go to their about page to extract the birth date 
#to get author birth date
link="https://quotes.toscrape.com/author/"+"Albert-Einstein/"
response=requests.get(link)
data=soup(response.text,'html.parser')
data.find(class_="author-born-date").string


# In[22]:


s="abjbj"
s.lower().startswith('a')  #using this string function to find start with j


# In[71]:


#full code 
import requests 
from bs4 import BeautifulSoup as soup 


author_details={}
base_url="https://quotes.toscrape.com/"
#for fist page or homepage
response=requests.get(base_url)
data=soup(response.text,'html.parser')
#to find authors
for a in range(len(data.find_all(class_="quote"))):
    author=data.find_all(class_="quote")[a].find(class_="author").string
    if author.lower().startswith('j'):
        ref_url=data.find_all(class_="quote")[a].a["href"]
        about_url= base_url+ref_url
        responseabout=requests.get(about_url)
        databout=soup(responseabout.text,'html.parser')
        date=databout.find(class_="author-born-date").string
        author_details[author]=date
        print(about_url)
        print(author,date)
        
#for other pages 

    
next_page=data.find(class_="next").a["href"]
#need to stop as soon as next button stops being visible so 
while next_page is not None:
    next_page_url=base_url+data.find(class_="next").a["href"]
    response=requests.get(next_page_url)
    data=soup(response.text,'html.parser')
    for a in range(len(data.find_all(class_="quote"))):
        author=data.find_all(class_="quote")[a].find(class_="author").string
        if author.lower().startswith('j'):
            ref_url=data.find_all(class_="quote")[a].a["href"]
            about_url= base_url+ref_url
            responseabout=requests.get(about_url)
            databout=soup(responseabout.text,'html.parser')
            date=databout.find(class_="author-born-date").string
           
            author_details[author]=date
            print(about_url)
            print(author,date)

    next_page=data.find(class_="next")


author_details   


# In[73]:


#need to sort in dict name 

sorted_keys = sorted(author_details.keys())
sorted_dict = {key:author_details[key] for key in sorted_keys}

# Print the sorted dictionary
print(sorted_dict)


# **Quotes by Albert Einstein**
# 
# Find all the quotes by Albert Einstein(in the order they appear on the page) from this website
# Note : Fetch data from all the pages.
# 
# Output Format :
# quote1
# quote2
# quote3
# .
# .
# .
# 
# link:https://quotes.toscrape.com/

# In[79]:


import requests 
from bs4 import BeautifulSoup as soup 
#for one
base_url="https://quotes.toscrape.com/"
#for fist page or homepage
response=requests.get(base_url)
data=soup(response.text,'html.parser')

author=data.find_all(class_="quote")[0].find(class_="author").string
if author=='Albert Einstein':
    print(data.find(class_="text").string)


# In[90]:


#full code for all pages 
import requests 
from bs4 import BeautifulSoup as soup 

response=requests.get(base_url)
data=soup(response.text,'html.parser')
base_url="https://quotes.toscrape.com/"
list_of_quotes=data.find_all(class_="quote")
for i in range(len(list_of_quotes)):
    author=list_of_quotes[i].find(class_="author").string
    if author=='Albert Einstein':
        print(list_of_quotes[i].find(class_="text").string)

#for all pages 
next_page=data.find(class_="next").a["href"]
#need to stop as soon as next button stops being visible so 
while next_page is not None:
    next_page_url=base_url+data.find(class_="next").a["href"]
    response=requests.get(next_page_url)
    data=soup(response.text,'html.parser')
    list_of_quotes=data.find_all(class_="quote")
    for i in range(len(list_of_quotes)):
        author=list_of_quotes[i].find(class_="author").string
        if author=='Albert Einstein':
            print(list_of_quotes[i].find(class_="text").string)
            
    next_page=data.find(class_="next")

    

    

