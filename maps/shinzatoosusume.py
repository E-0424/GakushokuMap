from maps.AbstractGakushoku import AbstractGakushoku
class GakushokuSample(AbstractGakushoku):
    def get_menu(self):
        return "すき家の高菜明太牛丼"
    def get_summary(self):
        return "ピリ辛の高菜と明太子が絶妙に絡み合った、ボリューム満点の牛丼です。"
    def get_author(self):
        return "新里"