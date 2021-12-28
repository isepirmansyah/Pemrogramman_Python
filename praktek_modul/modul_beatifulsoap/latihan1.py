from bs4 import BeautifulSoup

# soup = BeautifulSoup("<html><p>Ini Paragraf di Halaman Web</p></html>","html.persen")
# print(soup)
# <html><p>Ini Paragraf di Halaman Web</p></html>

soup = BeautifulSoup("<html><p>Ini Paragraf di Halaman Web</p></html>","lxml")
print(soup)
# <html><body><p>Ini Paragraf di Halaman Web</p></body></html>

soup = BeautifulSoup("<html><p>Ini Paragraf di Halaman Web</p></html>","xml")
print(soup)
# <?xml version="1.0" encoding="utf-8"?>
# <html><p>Ini Paragraf di Halaman Web</p></html>

soup = BeautifulSoup("<html><p>Ini Paragraf di Halaman Web</p></html>","html5lib")
print(soup)
# <html><head></head><body><p>Ini Paragraf di Halaman Web</p></body></html>
