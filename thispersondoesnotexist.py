import aiohttp
from bs4 import BeautifulSoup


class ThisPersonDoesNotExist:
    def __init__(self,url):
        self.url = url
    
    async def link(self):
        session = aiohttp.ClientSession()
        r = await session.get(self.url)
        r_t = await r.text()
        soup = BeautifulSoup(r_t,features='html.parser')
        link = soup.find('img', {'id':'avatar'})
        link = str(link)
        link = link[41:77]
        lins = f'https://this-person-does-not-exist.com/img/avatar-{link}'
        await session.close()            
        return lins 

# Use this code to generate images from "https://this-person-does-not-exist.com/en", very interesting website in my opinion
