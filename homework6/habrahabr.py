import requests
from bs4 import BeautifulSoup


#получаем список всех хабов пользователя
def get_user_hubs(user_name):
    r = requests.get('https://habrahabr.ru/users/{}/'.format(user_name))
    soup = BeautifulSoup(r.content)
    hubs_table = soup.find('dl', {'class','hubs_list'})
    hubs_list = []
    for item in hubs_table.find_all('a'):
        hubs_list.append(item['href'])
    return hubs_list

#получаем список всех постов по конкретному хабу
def parse_hub_posts_content(hub_url):
    r = requests.get('https://habrahabr.ru{}'.format(hub_url))
    soup = BeautifulSoup(r.content)
    post_teasers = soup.find_all('div', {'class','post_teaser'})
    return post_teasers

#собираем необходимую информацию по хабу и складываем в словарь
def parse_post_content(hub_url):
    all_hub_posts = []
    post_dict = {}
    for post_teaser in parse_hub_posts_content(hub_url):
        post_url = post_teaser.find('a', {'class','post__title_link'})
        post_title = post_teaser.find('a', {'class','post__title_link'})
        post_cut = post_teaser.find('div', {'class', 'html_format'})
        post_dict = {'hub_url':'https://habrahabr.ru{}'.format(hub_url), 'hub_name':hub_url[5:-1], 'post_url':post_url['href'], 'post_title':post_title.text, 'post_cut':post_cut.text}
        all_hub_posts.append(post_dict)
    return all_hub_posts

if __name__ == "__main__":
    for hub_url in get_user_hubs('gi4'):
        print('Парсим хаб: ' + hub_url[5:-1])
        print(parse_post_content(hub_url))