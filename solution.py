from enum import Enum #Импорт класса Enum для работы с перечислениями из модуля enum

class Positions(Enum):
    JUNIOR = 10 #name=JUNIOR, value=10  
    MIDDLE = 12  
    SENIOR = 20  


class Programmer: 
    def __init__(self, name: str, position: Positions) -> None:  
        self.__name = name  
        self.__position = position
        self.__hour_price = self.__position.value


    def work(self, time: int) -> None:
        self.__times = 0 #Перенес инициализацию времени для срабатывания в методе work и для сброса в ноль для нового расчета (типо месяца)
        self.__times += time
  

    def rise(self) -> str:  
        if self.__position.name == 'JUNIOR':  
            self.__position = Positions.MIDDLE
            self.__hour_price = Positions.MIDDLE.value #Добавил расчет новой ставки
  
        elif self.__position.name == 'MIDDLE':  
            self.__position = Positions.SENIOR
            self.__hour_price = Positions.SENIOR.value
  
        else:  
            self.__hour_price += 2 
  

    def info(self) -> str:  
        return f'{self.__name}: {self.__times} ч. {self.__give_salary()} тгр.'  

  
    def __give_salary(self) -> int:  
        salary = self.__hour_price * self.__times #Заменил расчет ЗП ставка умножить на время
        return salary



#Сбил все обращения под функцию
def main():
    batashev = Programmer(name='Alexey', position=Positions.JUNIOR)#Закидываем в Programmer Position с атрибутами Джуна
    batashev.work(150)
    print(batashev.info())#ЗП Джуна

    batashev.rise()
    batashev.work(150)
    print(batashev.info())#ЗП Мидла

    batashev.rise()
    batashev.work(150)
    print(batashev.info())#ЗП Сеньера

    batashev.rise()
    batashev.work(150)
    print(batashev.info())#ЗП Сеньера+
if __name__ == '__main__':
    main()