import requests
import json


class Cat():
    def __init__(self, number):
        self.number = number

    def nth_cat(self):

        number = self.number

        if number <= 0:
            raise ValueError("Number not large enough")

        page_number = 1
        result = requests.get(f'https://catfact.ninja/breeds?page={page_number}')
        text = json.loads(result.text)
        breeds = len(text['data'])

        while number > breeds:
            if breeds == 0:
                raise ValueError("Cat Breeds Exceeded: Number Too Large")

            page_number += 1
            result = requests.get(f'https://catfact.ninja/breeds?page={page_number}')
            text = json.loads(result.text)
            number -= breeds
            breeds = len(text['data'])

        print(text['data'][number - 1]['breed'])


if __name__ == '__main__':
    breed_number: int = int(input("Cat Breed Number: "))
    cat = Cat(breed_number)
    cat.nth_cat()