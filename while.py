counter = 9
while counter > 0:
     print(counter)
     counter = counter -2


parol = (input('Введите пароль '))
while parol != 'admin':
     print('Неверный пароль, попробуйте ище раз!')
     parol = (input('Введите пароль '))
if parol == 'admin':
     print('Доступ Разрешен')

parol = (input())
while parol != 'end':
     parol = (input())

list = ["Windows", "Macos", "ios", "android", "linux"]
user_input = input("Введите слов ")
while user_input not in list:
     print('Слово не найдено')
     user_input = input("Введите слов ")
if user_input in list:
     print('Слово найдено')



while True:
    login = (input('Введите логин '))
    if login == 'admin':
        break
    print('Неправильный логин, попробуйте ище раз')

while True:
    parol = (input('Введите пароль '))
    if parol == '1234':
        print('Добро пожаловать')
        break
    print('Неправильный пароль, попробуйте ище раз')


login = input('Введите логин: ')
while login != 'admin':
    print('Неправильный логин, попробуйте еще раз')
    login = input('Введите логин: ')

password = input('Введите пароль: ')
while password != '1234':
    print('Неправильный пароль, попробуйте еще раз')
    password = input('Введите пароль: ')

print('Все правильно')
