![alt text](https://i.imgur.com/2EavnFs.png)

````
pip install requests
pip install bs4
pip install Obhavo
````

````
from weather.ob_havo import Obhavo

data = Obhavo(city='toshkent').main()
print(data)
````
````
{'city': 'Toshkent', 'day': 'Bugun, 24 yanvar', 'info': 'Ochiq havo', 'description': '\n\nNamlik: 68%\nShamol: Janubiy-janubi-sharqiy, 0 m/s\nBosim: 774 mm sim. us
t.\n\n\nOy: Qisqarayotgan oy\nQuyosh chiqishi: 07:41\nQuyosh botishi: 17:28\n\n\n', 'degree': '+9°-1°'}
````
````
print(data['city'])
>>> Toshkent
````

````
data = Obhavo().all()
print(data)
````
# Shaharlarni ro'yhati
**Toshkent**
**Samarqand**
**Andjion**
**Buxoro**
**Jizzax**
**Qarshi**
**Navoi**
**Namangan**
**Nukus**
**Termiz**
**Urganch**
**Fargona**
**Xiva**
