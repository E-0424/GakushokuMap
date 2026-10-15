# maps/OzawaGakushoku.py
from maps.AbstractGakushoku import AbstractGakushoku

class OzawaGakushoku(AbstractGakushoku):
    def get_menu(self):
        return "かつカレー"

    def get_summary(self):
        return "おいしい"

    def get_author(self):
        return "小澤蒼空"