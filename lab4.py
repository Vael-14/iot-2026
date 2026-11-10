class Pool:
 
    def __init__(self, address="Невідомо", water_volume=0.0, max_visitors=0,
                 name="Без назви", lanes_count=0):

 
        self.__address = address
        self.__water_volume = water_volume
        self.__max_visitors = max_visitors
 
        self.name = name
        self.lanes_count = lanes_count
 

    def get_address(self):
        return self.__address
 
    def get_water_volume(self):
        return self.__water_volume
 
    def get_max_visitors(self):
        return self.__max_visitors
 
    def set_address(self, address):
        self.__address = address
 
    def set_water_volume(self, water_volume):
        if water_volume < 0:
            raise ValueError("Об'єм води не може бути від'ємним")
        self.__water_volume = water_volume
 
    def set_max_visitors(self, max_visitors):
        if max_visitors < 0:
            raise ValueError("Кількість відвідувачів не може бути від'ємною")
        self.__max_visitors = max_visitors
 
    def __str__(self):
        return (f"Басейн «{self.name}»\n"
                f"  Адреса: {self.__address}\n"
                f"  Об'єм води: {self.__water_volume} л\n"
                f"  Макс. одночасних відвідувачів: {self.__max_visitors}\n"
                f"  Кількість доріжок: {self.lanes_count}")
 
    def __repr__(self):
        return (f"Pool(address={self.__address!r}, "
                f"water_volume={self.__water_volume!r}, "
                f"max_visitors={self.__max_visitors!r}, "
                f"name={self.name!r}, lanes_count={self.lanes_count!r})")
 
    def __del__(self):
        print(f"Деструктор: об'єкт «{self.name}» видаляється")

    def __add__(self, other):
            if not isinstance(other, Pool):
                return NotImplemented
            return Pool(self.__address + " / " + other.__address,
                    self.__water_volume + other.__water_volume,
                    self.__max_visitors + other.__max_visitors,
                    self.name + " + " + other.name,
                    self.lanes_count + other.lanes_count)    
 
 
def main():
    pool1 = Pool()

    pool2 = Pool("м. Львів, вул. Стрийська, 10", 750000, 150, "Олімпійський", 8)
    pool3 = Pool("м. Київ, пр. Перемоги, 25", 300000.5, 80, "Дельфін", 5)
 
    for i, pool in enumerate((pool1, pool2, pool3), start=1):
        print(f"--- Об'єкт {i} ---")
        print("Адреса:", pool.get_address())
        print("Об'єм води (л):", pool.get_water_volume())
        print("Макс. відвідувачів:", pool.get_max_visitors())
        print("Назва (публічне):", pool.name)
        print("Доріжок (публічне):", pool.lanes_count)
        print(pool)
        print(repr(pool))
        print()
    

    pool4 = pool2 +pool3

    del pool
    del pool3     # тепер деструктор спрацює тут
    print("після del pool3")

    print(pool4)

    
    
    pool1.set_water_volume(1000)
    print("Після set_water_volume:", pool1.get_water_volume())


    try:
        print(pool2.__address)
    except AttributeError as e:
        print("Помилка прямого доступу:", e)
    print("Через _Pool__address:", pool2._Pool__address)
 
    print("\nКінець main()")
 
 
if __name__ == "__main__":
    main()
