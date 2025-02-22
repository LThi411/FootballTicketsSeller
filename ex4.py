#%% - import lib
import requests as rq
from bs4 import BeautifulSoup as bs
#%%
url='https://tuoitre.vn/lan-song-sa-thai-am-tham-tang-cao-dip-cuoi-nam-20250124100524156.htm'
reponse=rq.get(url)
#%% Display data
if reponse.status_code == 200:
    returned_data = reponse.text
    # print(returned_data)
    soup=bs(returned_data, 'html.parser')
    title=soup.find('title').text
    print(title)
    #sub title
    sub_title=soup.find('h2',{'class': 'contentcomment'}).text
    comment=soup.find('span',{'class':'contentcomment'}).text
    print(comment)