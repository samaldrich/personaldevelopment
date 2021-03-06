# This is a program to find and download all PNG pics from a url
# It'll automatically download all PNG pics to this folder: C:\Users\USERNAME\Downloads\PICFOLDER

import re
import requests
import pathlib
import bs4
import lxml
import os



# replace this url with your url, keep the quotes('') . Don't leave any "/" at the end of the url
url='https://onepiecechapters.com/manga/one-piece-chapter-1004'

print(f'Start Downloading {url}')

# generate PICFOLDER name and create this folder
pathNameStr='C:\\Users\\'+os.getlogin()+'\\Downloads\\'+os.path.basename(url)
pathName=pathlib.Path(pathNameStr)
pathName.mkdir(parents=True,exist_ok=True)

# Regular Expression to find all PNG files
imageRegex=re.compile('''

https\:\/\/.*png

''',re.VERBOSE)

# get the webpage
res=requests.get(url)
res.raise_for_status()
page=bs4.BeautifulSoup(res.text,'lxml')

# find all PNG pics on the webpage and download them
result=imageRegex.findall(str(page))
a=0
for i in result:
    fileName=str(a)+'.png'
    a=a+1
    print(f'Downloading {fileName} ...')
    resImage=requests.get(i)
    resImage.raise_for_status()
    fileImage=open(pathName / fileName,'wb')
    for chunk in resImage.iter_content(100000):
        fileImage.write(chunk)
