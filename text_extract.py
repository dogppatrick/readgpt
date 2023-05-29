import re

from bs4 import BeautifulSoup


def pre_proc(txt):
    txt = re.sub(r"<script>(.*?)script>", "", txt)
    txt = re.sub(r"<(.*?)>","",txt)
    remove_list = ['\n','\r','\t']
    for icon in remove_list:
        txt = txt.replace(icon,' ')
    while '  'in txt:
        txt = txt.replace('  ',' ')
    return txt

def res_to_file(s:str):
    with open('./tmp.txt','w') as f:
        f.write(s)

def res_to_file(s:str):
    with open('./tmp.txt','w') as f:
        f.write(s)

def sf_article_extract(resp_text):
    soup = BeautifulSoup(resp_text, 'html.parser')
    paragraphs = soup.find_all('p')
    text_content = ' '.join([p.get_text() for p in paragraphs])
    text_content = pre_proc(text_content)
    # res_to_file(text_content)
    return text_content
