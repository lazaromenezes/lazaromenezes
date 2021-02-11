import requests
import xml.etree.ElementTree as et

def from_items(pt_item, en_item):

    title_pt = pt_item.find('title').text
    title_en = en_item.find('title').text
    url_pt = pt_item.find('link').text
    url_en = en_item.find('link').text

    return "| [{0}]({1}) | [{2}]({3}) |".format(title_pt, url_pt, title_en, url_en)

def load_rss_items(url):
    data = requests.get(url)
    data.encoding = 'utf-8'

    root = et.fromstring(data.text)

    return root.findall('./channel/item')

if __name__ == '__main__':
    with open('README.md.template', 'r') as template_file:
        template = template_file.read()

    rss_pt = 'http://www.lazarodm.com.br/index.xml'
    rss_en = 'http://www.lazarodm.com.br/en/index.xml'

    pt_items = load_rss_items(rss_pt)
    en_items = load_rss_items(rss_en)

    posts = []

    for i in range(len(pt_items)):
        posts.append(from_items(pt_items[i], en_items[i]))

    result = "\n".join(posts)
    print(template.replace("{{POSTS}}", result))


