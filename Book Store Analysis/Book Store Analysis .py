#!/usr/bin/env python
# coding: utf-8

# # Book Store Analysis Using BeautifulSoup

# BOOKS TO SCRAPE
# 
# link:https://books.toscrape.com/

# In[67]:


#loading libraries
import requests 
from bs4 import BeautifulSoup as soup


# In[68]:


#load the html data 
response=requests.get('https://books.toscrape.com/')
response


# In[70]:


html=response.text
data=soup(html,'html.parser')
print(data.prettify())


# In[71]:


#extracting title 
data.title


# In[74]:


#to get main heading either see through inspect tool it's actually first link
data.a


# In[75]:


#else 
data.header.a.string


# In[77]:


#see on first page 20 books available -> lot of info for each book 
#title,rating,price etc
#let's extract details of this 1st book -> inspect tool ->see under class -> product_prod
b1=data.find(class_='product_pod')
b1.h3.a['title']


# In[78]:


b1.h3.a['href'] #actually relative url 


# In[79]:


#to make complete url 
base_url='https://books.toscrape.com/'
print(base_url+b1.h3.a['href'])


# In[82]:


#let's get hyperlinks for all the book 
books=data.find_all(class_='product_pod')
len(books)


# In[83]:


for i in books:
    print(i.h3.a['href'])


# In[84]:


for i in books:
    print(base_url+i.h3.a['href'])


# **Book Names from First Page**
# 
# Print the title of all 20 books which are present on first page of this website.
# 
#  Book1 Name
#  Book2 Name
#  Book3 Name
#  .
#  .
#  .

# In[87]:


import requests 
from bs4 import BeautifulSoup as soup 
response=requests.get("https://books.toscrape.com/")
html=response.text 
data=soup(html,'html.parser')


# In[101]:


books=data.find_all(class_='product_pod')
for i in books:
    print(i.h3.a['title'])


# Print the name of all categories which are present this website.
# 
# Output Format :
#  Category1 Name
#  Category2 Name
#  Category3 Name
#  .
#  .
#  .

# In[124]:


#using inspect tool div class => side_categories => ul => nav nav-list, li =>ul => then all lists inside it


# In[171]:


import requests 
from bs4 import BeautifulSoup as soup 
response=requests.get("https://books.toscrape.com/")
html=response.text 
data=soup(html,'html.parser')


d={}
for i in list(data.find_all('ul')[1].li.ul.descendants):
    a=list(i.stripped_strings)
    for j in a:
        d[j]=d.get(j,0)
for k in d:
    print(k)


# In[172]:


#or 
categories_container = data.find('ul', class_='nav-list')

# Find all the list items (categories) within the container
categories = categories_container.find_all('li')

# Iterate through the categories and print their names
for category in categories[1:]:  #leaving first one since it will say "BOOKS" giving heading which is not needed
    category_name = category.a.text.strip()
    print(category_name)


# In[1]:


from bs4 import BeautifulSoup as soup 
import requests
response=requests.get("https://books.toscrape.com/")
response.status_code
html=response.text
data=soup(html,'html.parser')
for i in data.find_all(class_='side_categories'):
    print(list(i.stripped_strings)[1:])


# **Links of all the pages** 
# 
# Earlier we extracted data from first page only, this website has data of 1000 books -> available on 50 different pages. To get info about all the books we need to load data from all the pages 
# 
# The browse url should change for every get request, if you inspect the next button you will see the relative url to next pages each time you click on next , 
# for page 2 it has class="next" href= "catalogue/page-2.html"  and after that just /page3.html , /page4.html. 
# so 1st relative url need to have catalogue/ too in the link, other don't -> we can use an if else situation or we can once see what loads for books.toscrape.com/catalogue/page1.html rather than just for books.toscrape.com, page loading is same so better to use former one as base url
# 
# Note: if you think rather than extracting url from next we can just do base url+ page[i] i randing from 2 to 50 then this can only work here since page naming is systematic but what if page 2 has url named xyz and 3 has abc, so in that case better to make base url + relative url extracted from next button.
# 
# Also here we know limit for loop is 50 since total pages are 50 but in case we don't know then we can use while response.status_code= success that is 200

# In[2]:


import requests
from bs4 import BeautifulSoup as soup

#making a list of all urls
all_urls=["https://books.toscrape.com/catalogue/page-1.html"]
current_page='https://books.toscrape.com/catalogue/page-1.html'
base_url='https://books.toscrape.com/catalogue/'
response=requests.get(current_page)
while response.status_code==200:
    data=soup(response.text,'html.parser')
    next_page=data.find(class_='next')
    next_page_url=base_url+next_page.a['href']
    print(next_page_url)
    all_urls.append(next_page_url)
    current_page=next_page_url
    response=requests.get(current_page)
    


# **All Book Names**
# 
# Print the title of all books which are present on first 10 pages of this website.
# Output Format :
#  Book1 Name
#  Book2 Name
#  Book3 Name
#  .
#  .

# In[5]:


allPages = ['http://books.toscrape.com/catalogue/page-1.html',
            'http://books.toscrape.com/catalogue/page-2.html',
            'http://books.toscrape.com/catalogue/page-3.html',
            'http://books.toscrape.com/catalogue/page-4.html',
            'http://books.toscrape.com/catalogue/page-5.html',
            'http://books.toscrape.com/catalogue/page-6.html',
            'http://books.toscrape.com/catalogue/page-7.html',
            'http://books.toscrape.com/catalogue/page-8.html',
            'http://books.toscrape.com/catalogue/page-9.html',
            'http://books.toscrape.com/catalogue/page-10.html']

import requests
from bs4 import BeautifulSoup as soup 
bookstitle=[]
for i in range(10):
    response = requests.get(allPages[i])
    data=soup(response.text,'html.parser')
    booksdata=data.find_all(class_='product_pod')
    for j in booksdata:
        bookstitle.append(j.h3.a['title'])
for d in bookstitle:
    print(d)


# Store Data in CSV
# 
# A dedicated link is present for each book amongs 1000s on website, on going to link we can see more details abt the book like title,qty in stock,price description etc.
# 
# Let's create a dataframe of Links to websites link,title,price and qty in stock (this is not visible on homepage)

# In[4]:


#ecxtracting the details for one book first 
#make a get req to homepage-> extract the book link -> extract data from that link 
#pre req 
import requests
from bs4 import BeautifulSoup as soup 


# In[11]:


response=requests.get('https://books.toscrape.com/')
data=soup(response.text,'html.parser')
base_url='https://books.toscrape.com/'
b1=base_url+data.find(class_='product_pod').h3.a['href']
b1  #dedicated website extracted 


# In[20]:


#now extracting required info from dedicated website 
response=requests.get(b1)
data=soup(response.text,'html.parser')
link=b1
title=data.h1.string
price=data.find(class_='price_color').string
#qty has multiple childs
qtylist=list(data.find(class_='instock availability').stripped_strings)
qty=qtylist[0]


# In[21]:


#printing all 
print(title)
print(link)
print(price)
print(qty)   #need to remove other text from qty and price to just get numbers 


# In[35]:


print(title)
print(link)
print(price)
print(qty)


# In[39]:


#making a 2d list which we can conver to dataframe later
bookdetails=[]
bookdetails.append([title,link,price,qty])
#just two visualize appending twice 
bookdetails.append([title,link,price,qty])
bookdetails


# In[40]:


import pandas as pd 

df=pd.DataFrame(bookdetails,columns=['Title','Link','Price','Quantity In Stock'])
df


# In[43]:


#to extract to csv 
df.to_csv('books.csv',index=False)  #to avoid index getting download


# **Book Details**
# 
# Find and print the details of all books which are present on first 2 pages of this website.
# All details include - Title of the book, book page url, Price (in float, without any currency or extra symbol), and quantity in stock (in integer). Save all the details in a dataframe and print in the required format.
# Note: Remove the Trailing Zeros from price of book.
# 
# Output Format :
#  Book1_Title Book1_Link Book1_Price Book1_Quantity
#  Book2_Title Book2_Link Book2_Price Book2_Quantity
#  Book3_Title Book3_Link Book3_Price Book3_Quantity
#  .
#  .
#  .

# In[2]:


#doing for first two pages 
import requests
from bs4 import BeautifulSoup as soup 
import re 
import pandas as pd

allPages = ['http://books.toscrape.com/catalogue/page-1.html',
            'http://books.toscrape.com/catalogue/page-2.html']

column_names = ['Title', 'Link', 'Price', 'Quantity in Stock']
base_url='https://books.toscrape.com/catalogue/'
book_urls=[]
for i in range(2):
    response=requests.get(allPages[i])
    data=soup(response.text,'html.parser')
    a=data.find_all(class_='product_pod')
    for k in range(len(a)):
        alink=base_url+a[k].h3.a['href']
        book_urls.append(alink)
book_urls


# In[11]:


#now extracting required data 
books_details=[]
for l in book_urls:
    response=requests.get(l)
    
    if response.status_code==200:
        data=soup(response.text,'html.parser')
        link=l
        title=data.h1.string
        price=data.find(class_='price_color').string
    
        qtylist=list(data.find(class_='instock availability').stripped_strings)
        qty=qtylist[0]
        price=float((re.search('[\d.]+',price)).group())
        price = "{:.2f}".format(price)
        qty=int((re.search('\d+',qty)).group())
        

        books_details.append([title,link,price,qty])
books_details
    
    
    


# In[12]:


df=pd.DataFrame(books_details,columns=column_names)
df


# In[13]:


for detail in books_details:
    print(*detail)


# In[20]:


for index, row in df.iterrows():
    for column, value in row.items():
        print(value,end=" ")
    print()


# In[9]:


#saving to csv file 
df.to_csv("Bookdetailsfirsttwopages.csv",index=False) #.csv for proper format 


# In[52]:


#same ans as below but below one worked in codezen 
from bs4 import BeautifulSoup
import pandas as pd
import requests
import re

allPages = ['http://books.toscrape.com/catalogue/page-1.html','http://books.toscrape.com/catalogue/page-2.html']
column_names = ['Title', 'Link', 'Price', 'Quantity in Stock']
base_url = 'http://books.toscrape.com/catalogue/'

allBooks=[]
for i in allPages:
    response = requests.get(i)
    data = BeautifulSoup(response.text, 'html.parser')
    book = data.find_all(class_='product_pod')
    for i in book:
        b_url = base_url + i.h3.a['href']
        allBooks.append(b_url)

        
Book_details=[]
for i in allBooks:
    response = requests.get(i)
    data = BeautifulSoup(response.text, 'html.parser')
    title = data.h1.string
    price = data.find(class_='price_color').string
    qty = data.find(class_='instock availability')
    qty = qty.contents[-1].strip()
    qty = int(re.search('\d+',qty).group())
    price = float(re.search('[\d.]+',price).group())
    Book_details.append([title, i, price, qty])
    
#for i in Book_details:
#print(*i)
df = pd.DataFrame(Book_details,columns=column_names)
for i in range(len(df)):
    print(df['Title'][i],df['Link'][i],df['Price'][i],df['Quantity in Stock'][i])


# All Categories
# 
# Print the name of all categories which are present this website.
# 
# Output Format :
#  Category1 Name
#  Category2 Name
#  Category3 Name
#  .
#  .
#  .
#  
#  link:https://books.toscrape.com/

# In[105]:


import requests 
from bs4 import BeautifulSoup as soup 

response= requests.get("https://books.toscrape.com/")
data=soup(response.text,'html.parser')
catlist=data.find(class_="nav nav-list").ul.find_all("a")
for i in catlist:
    a=i.stripped_strings
    print(list(a)[0])

