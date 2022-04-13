import requests

from bs4 import BeautifulSoup

res = requests.get("http://rahul-agrawal.me/site")   
  
# print(res.content)    # Prints the HTML content

# print(res.text)       # Prints the HTML content in plain text and formatted

# print(res.url)        # Prints the URL of the page

# print(res.status_code) # Prints the status code of the page

# print(res.headers)     # Prints the headers of the page

source = res.content

soup = BeautifulSoup(source, 'html.parser')    # same as res.text
# print(soup)

#  get a specific element e.g. all the links

links = soup.find_all('a') # returns a list of all the links if only "find" then it returns the first link

print(len(links)) # total links in the page

# for i in links:
#     # print(i.text)
 
#     print(f"{i.text} = " , i.get('href'))   # filter the links and print them

div = soup.find_all('div', class_='card')   # returns a list of all the divs with class card

for i in div:
    print(i.string)   # get the text inside of the divs

