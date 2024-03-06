from modules.book import Book
from modules.magazine import Magazine
from modules.cd import Cd
from modules.dvd import Dvd


class Catalog():
    def __init__(self, catalog):
        self.catalog = catalog

    def search(self, input_Search):
        list_result = []
        for catalog_item in self.catalog:
            for item in catalog_item:
                if input_Search.lower() in item.title.lower():
                    if type(item) is Magazine:
                        list_result.append('Title: ' + item.title +
                                           ', volume: ' + str(item.volume) +
                                           ', Type Catalog: Magazine')
                    elif type(item) is Book:
                        list_result.append(f'Title: {item.title}, DDS Number: {item.dds_number}, Type Catalog: Book')
                    elif type(item) is Dvd:
                        list_result.append(f'Title: {item.title}, genre: {item.genre}, Type Catalog: DVD')
                    elif type(item) is Cd:
                        list_result.append('Title: ' + str(item.title) +
                                           ', artist: ' + str(item.artist) +
                                           ', Type Catalog: Cd')
        return list_result
