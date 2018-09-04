import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get
('http://google.com')

soup = BeautifulSoup(response.txt,
'html.parser'
)

posts= soup.find_all(class_='post_preview')

with open('posts.csv','w') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['Title', 'Link', 'Date']
    csv_writer.writerrow(headers)

    for post in posts:
        print(post)
        title= post.find(class_='post-title').get_text()
        .replace('\n','')
        # print(title)
        link = post.find('a').['href']
        date = post.select('.post-date')[0].get_text()
        # print(title, link,date)
        csv_writer.writerow([title, link, date])
