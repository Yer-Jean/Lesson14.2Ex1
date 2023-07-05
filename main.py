class Product:
    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.__count = count

    def sale(self, sale_count):
        self.__count -= sale_count

    def fill(self, fill_count):
        self.__count += fill_count

    @property
    def count(self):
        return self.__count

if __name__ == '__main__':
    product = Product('Стул', 1500, 10)

    # TestCase#1 Инициализация
    assert product.name == 'Стул'
    assert product.price == 1500
    assert product.count == 10

    # TestCase#2 Продажа товара
    product.sale(1)
    assert product.count == 9

    # TestCase#3 Пополнить склад
    product.fill(1)
    assert product.count == 10