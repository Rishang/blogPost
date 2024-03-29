import requests
import json
import random
import asyncio
import aiohttp

class Unsplash:

    API = "https://unsplash.com/napi/"
    TOKEN = ""
    orientation = 'landscape'
    total = int()
    total_pages = int()
    random = None

    def __init__(self):
        pass

    def query(self, search=None, page:int=1, random_img:bool=False):
        per_page = 20
        
        if search is not None:
            
            q_path = f'search/photos?query={search}'
            query = self.API + q_path + '&' + f'orientation={self.orientation}'            
            
            if type(search) is list:
                q = [
                    self.API + f'search/photos?query={s}&per_page=29&page=1&orientation={self.orientation}' 
                    for s in search
                ]
                
                loop = asyncio.new_event_loop()
                tmp_data = loop.run_until_complete(
                    self._multi_query(q)
                )

                r_img:list = []
                for d in tmp_data:
                    tmp = json.loads(d)
                    r_img = r_img + tmp.get('results')
                del tmp_data

                if len(r_img) != 0 and random_img == True:

                    self.random = random.choice(r_img)
                    return random.choice(r_img)

                return r_img
        else:
            return False

        data = json.loads(requests.get(query).text)
        print(data.keys())
        self.total = data['total']
        self.total_pages = data['total_pages']

        if len(data['results']) != 0 and random_img == True:

            self.random = random.choice(data['results'])
            return random.choice(data['results'])

        return data['results'] or None


    @property
    def any(self):

        query = self.API + 'photos?per_page=29&page=1' + '&' + f'orientation={self.orientation}'
        data = json.loads(requests.get(query).text)
        self.random = random.choice(data)
        return random.choice(data)

    
    async def _multi_query(self, q:list):

        async with aiohttp.ClientSession() as session:
            d = []
            for i in q:
                async with session.get(i) as response:

                    print("Status:", response.status)
                    html = await response.text()
                    d.append(html)
        return d

