# Установлен googletrans
from googletrans import Translator, constants
import inspect

def introspection_info(obj):
    print('Тип объекта (Type): ', type(obj))
    print('Атрибуты объекта (__dict__): ', obj.__dict__)
    print('Методы объекта (__init__): ', obj.__init__)
    print('Модуль, к которму принадлежит объект (inspect.getmodule): ', inspect.getmodule(obj))

translator = Translator()

introspection_info(translator)

print()
print('==================== Другие интересные свойства объекта =======================')

print('Посмотрим "help" ', '='*80)
print(help(translator))
"""
Видим описание класса. Как он вызывается и с какими параметрами.
Дальше следует описание параметров.
Дальше идет описание методов 
    __init__
    detect
    translate 
с описаниями их параметров.
И даже приводятся примеры.
"""

print('Посмотрим "dir" ', '='*80)
print(dir(translator))
# Видим унаследованные свойства и методы и в конце наши 'detect' и 'translate'.

print('Посмотрим "__name__" ', '='*80)
# print(dir(translator.__name__))  Нет у него такого свойства
print(dir(Translator.__name__))  # А у класса есть

print('=========== Попробуем, как это работает ===============')
print('Язык определяется автоматически и по умолчанию переводится на английский')
translation = translator.translate("Привет, мои друзья")
print(f"Результат : {translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")
print('Оригинальный текст: ', translation.origin)  # Оригинальный текст
print('Язык с которого переводим: ', translation.src)  # Язык с которого переводим
print('Переведенный текст: ', translation.text)  # Переведенный текст
print('Язык на который перевели: ', translation.dest)  # Язык на который перевели

print('Переведем на арабский')
translation = translator.translate("Привет, мои друзья", dest='ar')
print(translation.text)
