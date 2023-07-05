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

class Category:
    def __init__(self, name, products):
        self.name = name
        self.__products = products
        self.__is_active = True  # Этот флаг вводим для скрытия категорий (см. задание - последняя строка)

    @property
    def is_active(self):
        return self.__is_active

    @property
    def products(self):
        return self.__products

    def remove(self, products_index):
        del self.__products[products_index]

    def __add__(self, product_item):
        self.__products.append(product_item)

    class Store:    # Класс создан для скрытия категорий с помощью флага is_active
        def __init__(self, categories):
            self.__categories = categories

        def categories(self):
            tmp = []
            for cat in self.__categories:
                if cat.is_active:
                    tmp.append(cat)
            return tmp


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


    category = Category('Стулья', [product])

    # TestCase#4 Создание категории
    assert category.name == 'Стулья'
    assert category.products == [product]

    # TestCase#5 Удаление товара (категории)
    category.remove(0)
    assert category.products == []

    # TestCase#6 Добавление товара (категории)
    category + product   # Работает метод __add__
    # А можно было сделать традиционно:
    # category.add(product) через метод add (без подчеркиваний), тело метода то же самое
    assert category.products == [product]
