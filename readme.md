# Лабораторная работа №1

В данной лабораторной работе было использовано 5 созидательных паттернов (creational patterns):
1. Получение ресурса есть инициализация (RAII)
2. Отложенная инициализация (Lazy initialization)
3. Фабричный метод (Factory method)
4. Строитель (Builder)
5. Одиночка (Singleton)
Данные шаблоны были выбраны случайно.

## RAII & Lazy initialization
Данные паттерны были совмещены в классе ``FileHandler``. Данный класс предназначен для хранения дескриптора открытого файла. Фаил открывается при инициализации экземпляра данного класса, при вызове метода ``\_init()``. Сама инициализация является отложенной и происходит при попытке считать или записать информацию в фаил. При удалении объекта фаил закрывается, тем самым выделение и освобождение ресурса связывается с временем жизни объекта ``FileHandler``.

## Factory method
Как известно, фаилы могут быть открыты на чтение или запись, поэтому для удобства были созданы классы ``ReadFileHandler`` и ``WriteFileHandler``, которые инкапсулируют в себе дескриптор на фаил, открытого для чтения и записи соответственно. Классы ``ReadFileHandlerFactory`` и ``WriteFileHandlerFactory`` позволяют создать соответствующий ``FileHandler`` помощью фабричного метода ``create()`` класса ``FileHandlerFactory``.

## Builder & Singleton
При открытии фаила нужно указать множество опций, некоторыми из которых являются путь и режим доступа. Для облегчения создания соответствующего ``FileHandler`` существует класс ``FileBuilder``, который содержит 2 метода: ``setPath()`` и ``setMode()``. Поскольку я посчитал, что в нескольких классах-строителях нет нужды, данный класс также реализует шаблон "Одиночка". При вызове статического метода ``get()``, класс ``FileBuilder`` возвращает существующий экземпляр стоителя, или сперва создаёт его если нужно.
