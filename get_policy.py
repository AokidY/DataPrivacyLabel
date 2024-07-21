from bs4 import BeautifulSoup
import requests
import json
import os

if __name__  == "__main__":
    #need to change
    url_1 = 'https://flightyapp.com/privacy/'
    url_2 = 'https://smartgymapp.com/privacy/'
    url_3 = 'https://www.getstoic.com/privacy-policy/'

    #need to change
    response = requests.get(url = url_3)
    page_text = response.text

    #need to change
    app_name = 'stoic'
    
    #filename = './' + app_name + '.html'
    #classname = 'support-all'
    #classname = 'cont-2'
    classname = 'div-block-15'


    path_html = '/Users/zachary/Documents/uci/221dataPriva/project/work/health/file_html/'
    path_txt = '/Users/zachary/Documents/uci/221dataPriva/project/work/health/file_txt/'

    
    
    html_name = app_name + '_content' + '.html'
    filename = app_name + '_content' + '.txt'

    filepath_html = os.path.join(path_html, html_name)
    filepath_txt = os.path.join(path_txt, filename)



    with open(filepath_html, 'w', encoding = 'utf-8') as fp:
        fp.write(page_text)

    with open(filepath_html, 'r', encoding='utf-8') as fp:
        html_data = fp.read()


    soup = BeautifulSoup(html_data, 'html.parser')
    content_element = soup.find('div', class_ = classname)


    if content_element is not None:
        content_text = content_element.get_text()
    else:
        content_text = ""


    with open(filepath_txt, 'w', encoding='utf-8') as fp:
        fp.write(content_text)

    print("End!")




