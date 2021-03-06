from math import hypot
from math import sqrt
from itertools import count, islice

def test_even_fucntion():
    """
    Необходимо реализовать функцию even_filter, которая получает неограниченное количество аргументов
    и возвращает из них только четные.
    """

    def even_filter(*args):
        even = [arg for arg in args if arg % 2 == 0]
        return even

    assert even_filter(1, 2, 3, 4, 5, 6) == [2, 4, 6]


def test_increment_decorator():
    """
    Необходимо реализовать декоратор increment_derocator, который увеличивает полученное значение на 1 и передает его в
    декрорируемую функцию.
    """
    def increment_derocator(func):
        def magic(arg1):
            arg2 = arg1 + 1
            return func(arg2)
        return magic

    @increment_derocator
    def returner(value):
        return value

    assert returner(1) == 2

def test_point_segment_class():
    """
    Дано: есть класс Point, описывающий точку на плоскости. Необходимо закончить класс Segment, описывающий отрезок,
    принимающий на вход 2 точки и позволяющий посчитать его длину.
    Модуль с математическими функциями называется math, документация по нему находится здесь:
    https://docs.python.org/3/library/math.html?highlight=math#module-math
    """

    class Point():
        def __init__(self, x, y):
            self.x = x
            self.y = y

    class Segment():
        def __init__(self, p1, p2):
            self.p1 = p1
            self.p2 = p2

        def length(self):
            dist = hypot(self.p2.x - self.p1.x, self.p2.y - self.p1.y)
            return dist

    p1 = Point(0, 0)
    p2 = Point(3, 4)
    assert Segment(p1, p2).length() == 5.0
    assert Segment(p2, p1).length() == 5.0

def test_translate():
    """
    Реализовать функцию-переводчик translate. Она принимает на вход 2 значения: переводимую фразу fraze и словарь dictionary.
    Фраза состоит из слов, написанных в нижнем регистре, разделенных пробелом (знаки препинания в фразе отсутствуют).
    Словарь состоит из пар ключ-значение, где каждый ключ это слово на языке оригинале, значение - перевод этого слова.
    Перевод осуществляется пословно. В словаре переведены все слова, которые встречаются в оригинале.
    Для разделения строки на список слов можно воспользоваться методом split(). Пример:
    >>> s = "My little string"
    >>> s.split()
    ['My', 'little', 'string']
    Документация по этому методу: https://docs.python.org/3/library/stdtypes.html#str.split
    Для объединения списка строк в одну, разделенную пробелами можно воспользоваться методом " ".join(l). Пример:
    >>> l = ["My", "little", "string"]
    >>> " ".join(l)
    'My little string'
    Документация по этому методу: https://docs.python.org/3/library/stdtypes.html#str.join
    """
    def translate(fraze, dictionary):
        l = []
        for word in fraze.split():
            l.append(dictionary[word])
        words = " ".join(l)
        return words

    assert translate("hello world", {"hello": "привет", "world": "мир"}) == "привет мир"
    assert translate("привет мир", {"привет": "hello", "мир": "world"}) == "hello world"
    assert translate("я люблю питон", {"я": "i", "люблю": "love", "питон": "python"}) == "i love python"


def test_is_prime():
    """
    Реализовать функцию is_prime, возвращающую, является ли переданное значение простым.
    Простым числом считается такое число, которое целочисленно делится на 1 и на само себя.
    Подробнее про простые числа: https://ru.wikipedia.org/wiki/Простое_число
    Для решения может понадобиться функция range(), которая может принимать 2 числа, и
    генерировать список чисел от a до b, не включая b. Пример:
    >>> list(range(3, 10))
    [3, 4, 5, 6, 7, 8, 9]
    Документация по функции range: https://docs.python.org/3.5/library/stdtypes.html?highlight=range#range
    """

    def is_prime(n):
        if n < 2: return False
        for number in islice(count(2), int(sqrt(n) - 1)):
            if not n % number:
                return False
        return True

    assert is_prime(2)
    assert is_prime(3)
    assert is_prime(5)
    assert is_prime(7)
    assert not is_prime(4)
    assert not is_prime(15)
    assert not is_prime(21)
