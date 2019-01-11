from bs4 import BeautifulSoup
import bs4
html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
soup = BeautifulSoup(html,"lxml")

#soup = BeautifulSoup(open('index.html'))
print soup.prettify()
print soup.ar
print soup.a.string
print type(soup.a.string)
if type(soup.a.string)==bs4.element.Comment:
    print soup.a.string

for child in soup.descendants:
    print child
for string in soup.strings:
    print(repr(string))
for string in soup.stripped_strings:
    print(repr(string))
content = soup.head.title.string
print content.parent.name



content = soup.head.title.string
for parent in  content.parents:
    print parent.name