import requests
from typing import List

class CatService:
    def __init__(self):
        self.endpoint = 'https://api.thecatapi.com/v1/breeds'

    def get_cats(self) -> List[any]:
        res = requests.get(self.endpoint)
        return res.json()

    def get_cat(self, id: str) -> any:
        path = "{}/{}".format(self.endpoint, id)
        return requests.get(path).json()
