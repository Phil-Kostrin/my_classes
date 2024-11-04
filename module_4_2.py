def test_function():
    def inner_function():
        print('Я в области видимости test_function')
    inner_function()

inner_function() #при запуске кода произойдет ошибка, т.к. функция inner_function находится в пространстве имен функции test_function

test_function() #чтобы код заработал, необходимо вызывать именно функцию test_function