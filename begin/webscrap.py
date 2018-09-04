finad_all()
el = soup.find_all('div')
el = soup.find(id='section-1')
el = soup.find(class_='items')
el = soup.select('.item')[0]
#class item 의 text들을 보여준다
for item in soup.select('.item'):
    print(item.get_text())
print(el)
#next line must be 1 a cause de /n
el = soup.body.content[1].contents[1]
el = soup.find(calss_='item').find_parent()
el = soup.find('h3').find_next_sibling('p')
