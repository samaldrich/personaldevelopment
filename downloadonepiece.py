# This is a program to find and download one piece comic from https://onepiecechapters.com
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
pathNameStr='C:\\Users\\'+os.getlogin()+'\\Downloads\\'+pathlib.PurePosixPath(url).name
pathName=pathlib.Path(pathNameStr)
pathName.mkdir(parents=True,exist_ok=True)


# get the webpage
pageTemp=requests.get(url)
pageTemp.raise_for_status()
page=bs4.BeautifulSoup(pageTemp.text,'lxml')

# find all imgs on the webpage and download them

pageElem=page.select('div center img')
# set a num for images, name them from 0.png to 99.png
num=0
for i in pageElem:
    

    # add 1 to the image name
    num=num+1
    # get url of images and download them
    picURL=i.get('src')
    print(f'Downloading {pathlib.PurePosixPath(picURL).name} ...')
    downloadTemp=requests.get(picURL)
    downloadTemp.raise_for_status()
    fileImage=open(pathName / (str(num) + pathlib.PurePosixPath(picURL).suffix),'wb')

    for chunk in downloadTemp.iter_content(10000):
        fileImage.write(chunk)
