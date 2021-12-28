from bs4 import BeautifulSoup

dokumen = '''
<html>
<head>
    <title>Modul BeautifulSoup</title>
</head>
<body>
    <p class="judul">Menggunakan Modul BeautifulSoup</p>
    <p class="paragraf">Belajar Pemrograman Python Menyenangkan</p>
</body>
</html>
'''

html_soup = BeautifulSoup(dokumen, 'html.perser')
judul = html_soup.find('p',class_='judul')
paragraf = html_soup.find('p',class_='paragraf')
judul_saja = html_soup.find('p',class_='judul').text
print(judul)
print(paragraf)
print(judul_saja)
all_paragraf = html_soup.find_all('p')
print(all_paragraf)

