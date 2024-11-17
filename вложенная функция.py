def test_function():
    print('Я главная функция')
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function() 
test_function()


def test_function():
    print('Я главная функция')
    def inner_function():
        print('Я в области видимости функции test_function')
    
test_function() # Если в блоке кода главной функции не вызвать вложенную, сработает только главная


def test_function():
    print('Я главная функция')
    def inner_function():
        print('Я в области видимости функции test_function')
inner_function()  # отдельно от главной функции, вложенная не сработает