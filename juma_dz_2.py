# 2. Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения,город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.


def user_info(name, surname, age, city, email, phone):
    return ' '.join([name.title(), surname.title(), age, city.capitalize(), email, phone])


print(user_info(name='juma', surname='abduhalikov', age='40', city='karakuly', email='error@mail.com', phone='123894'))
print(user_info('juma', 'abduhalikov', '39', 'karakuly', 'error@mail.com', '1234567890'))

"""Вариант"""


def my_info():
    try:
        user_name = str(input("Ваше имя:").capitalize())
        user_surname = str(input("Ваше фамилия:").capitalize())
        user_age = int(input("Ваш возраст:"))
        user_city = str(input("Ваш город проживания:").capitalize())
        user_email = str(input("Ваша эл.почта:").lower())
        user_phone = int(input("Ваш номер телефона:"))
        info = user_name, user_surname, user_age, user_city, user_email, user_phone
    except ValueError:
        return "ValueError"
    return info


print(*my_info())
