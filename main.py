from maps.GakushokuSample import GakushokuSample
from maps.KenOsusume import KenOsusume
from maps.shinzatoosusume import ShinzatoOsusume
from maps.OzawaGakushoku import OzawaGakushoku  
from maps.EitoGakusyoku import EitoGakusyoku

# ↓のリストには、メンバーの各オススメ学食が格納されます。
data = [EitoGakusyoku(),OzawaGakushoku(),ShinzatoOsusume(),KenOsusume()]

for rank, d in enumerate(data, start=1):
    print(f"{rank}位: {d.get_menu()}")
    print("---------------------------------")
    print(d.get_summary())
    print(d.get_author())
    print()
