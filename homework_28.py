# import math
#
# class Triangle:
#     def __init__(self, a, b, c):
#         if a + b <= c or c + a <= b or c + b <= a:
#             raise ValueError("Non-existent triangle")
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def sides(self):
#         return self.a, self.b, self.c
#
#     def perimeter(self):
#         return self.a + self.b + self.c
#
#     def area(self):
#         p = self.perimeter() / 2
#         return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5
#
#     def type(self):
#         if self.a == self.b == self.c:
#             return "Equilateral triangle"
#         elif self.a == self.b or self.c == self.b or self.c == self.a:
#             return "Isosceles triangle"
#         else:
#             return "Irregular triangle"
#
#     def right_triangle(self):
#         return  self.a ** 2 + self.b ** 2 == self.c ** 2 or \
#                 self.c ** 2 + self.b ** 2 == self.a ** 2 or \
#                 self.c ** 2 + self.a ** 2 == self.b ** 2
#
#     def angles(self):
#         angle_a = math.degrees(math.acos((self.b ** 2 + self.c ** 2 - self.a ** 2) / (2 * self.b * self.c)))
#         angle_b = math.degrees(math.acos((self.a ** 2 + self.c ** 2 - self.b ** 2) / (2 * self.a * self.c)))
#         angle_c = math.degrees(math.acos((self.a ** 2 + self.b ** 2 - self.c ** 2) / (2 * self.a * self.b)))
#         return angle_a, angle_b, angle_c
#
#     def inscribed_circle(self):
#         r = 2 * self.area() / self.perimeter()
#         return r
#
#     def circumscribed_circle(self):
#         R = (self.a * self.b * self.c) / (4 * self.area())
#         return R
#
#     def __str__(self):
#         return f"Sides: {self.sides()}\n"\
#                f"Perimeter: {self.perimeter()}\n"\
#                f"Area: {self.area()}\n"\
#                f"Type: {self.type()}\n"\
#                f"Is a right Triangle?: {self.right_triangle()}\n"\
#                f"Angles: {self.angles()}\n"\
#                f"Inscribed circle: {self.inscribed_circle()}\n"\
#                f"Circumscribed circle: {self.circumscribed_circle()}"\
#
#
# # e = Triangle(10, 17, 18)
# # print(e)

"""
1․ Գրել BankUser class, որը․
   - __init__() -ում կընդունի մարդու անունը, ազգանունը, տարիքը, հաշվեհամարը, գումարը հաշվեհամարի վրա, գաղտնաբառը,
   - մինչ ինիցիալիզացնելը, կստուգի, որ ընդունված արգումենտները ճիշտ են մուտքագրված՝
     -- անունը և ազգանունը - տառերից բաղկացած,
     -- տարիքը - բնական թիվ,
     -- հաշվեհամարը - 16 թվանշանից բաղկացած (xxxx xxxx xxxx xxxx կամ xxxxxxxxxxxxxxxx ֆորմատով),
     -- գումարը - դրական թիվ,
     -- գաղտնաբառը - ամենաքիչը 8 սիմվոլից բաղկացած տեքստ,
   - անունը, ազգանունը և տարիքը կլինեն այնպիսի ատրիբուտներ, որոնց ուղիղ հասանելիությունը կլինի պաշտպանված,
   - հաշվեհամարը, գումարը և գաղտնաբառը կլինեն այնպիսի ատրիբուտներ, որոնց ուղիղ հասանելիությունը կլինի արգելված,
   - կունենա մեթոդ, որը կվերադարձնի մարդու անունը, ազգանունը և տարիքը,
   - կունենա մեթոդ, որը կվերադարձնի հաշվեհամարը և գումարը, բայց միայն ճիշտ գաղտնաբառ հավաքելուց հետո,
   - կունենա մեթոդ, որը կավելացնի գումար հաշվին,
   - կունենա մեթոդ, որը կհանի գումար հաշվից, հաշվի առեք, որ գումարը բացասական չի կարող լինել,
   - 3 անգամ սխալ գաղտնաբառ հավաքելուց հետո տվյալ user-ի համար հասանելիությունը class-ի ամբողջ ֆունկցիոնալությանը կլինի արգելված,
   - կունենա մեթոդ, որի միջոցով կվերականգնվի հասանելիությունը անունը, ազգանունը և հաշվեհամարի վերջին 4 թվանշանները մուտքագրելուց հետո։
"""
from curses.ascii import isalpha
from operator import truediv


import smtplib
import random
from email.mime.text import MIMEText

class BankUser:
    def __init__(self, name, surname, age, account_number, balance, password, email):
        if not name.isalpha() or not surname.isalpha():
            raise ValueError("Անունն ու ազգանունը պետք է պարունակեն միայն տառեր։")
        if not isinstance(age, int) or age <= 0:
            raise ValueError("Տարիքը պետք է լինի դրական թիվ։")
        acc = account_number.replace(" ", "")
        if not acc.isdigit() or len(acc) != 16:
            raise ValueError("Հաշիվը պետք է պարունակի正 16 թվանշան։")
        if not isinstance(balance, (int, float)) or balance < 0:
            raise ValueError("Գումարը պետք է դրական լինի։")
        if not isinstance(password, str) or len(password) < 8:
            raise ValueError("Գաղտնաբառը պետք է առնվազն 8 նիշ լինի։")
        if "@" not in email:
            raise ValueError("Սխալ էլ․ փոստի հասցե։")

        self._name = name
        self._surname = surname
        self._age = age
        self.__account_number = acc
        self.__balance = balance
        self.__password = password
        self.__email = email
        self.__active = True
        self.__wrong_attempts = 0
        self.__verification_code = None

    def send_email(self, subject, body):
        sender_email = "youremail@example.com"
        sender_password = "yourapppassword"
        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = sender_email
        msg["To"] = self.__email

        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
                smtp.login(sender_email, sender_password)
                smtp.send_message(msg)
            return True
        except Exception as e:
            print(f"Email error: {e}")
            return False

    def forgot_password(self):
        code = str(random.randint(100000, 999999))
        self.__verification_code = code
        subject = "Գաղտնաբառի վերականգնման կոդ"
        body = f"{self._name}, ձեր վերականգնման կոդն է՝ {code}"
        if self.send_email(subject, body):
            return "Վերականգնման կոդը ուղարկվել է ձեր էլ․ փոստին։"
        else:
            return "Չհաջողվեց ուղարկել նամակը։"

    def restore_password_with_code(self, code, new_password):
        if self.__verification_code is None:
            return "Չկա ակտիվ վերականգնման կոդ։"
        if code != self.__verification_code:
            return "Սխալ կոդ։"
        if len(new_password) < 8:
            return "Նոր գաղտնաբառը պետք է առնվազն 8 նիշ լինի։"
        self.__password = new_password
        self.__verification_code = None
        self.__wrong_attempts = 0
        self.__active = True
        return "Գաղտնաբառը հաջողությամբ փոխվել է և մուտքը վերականգնվել է։"

    def get_account_info(self, password):
        if not self.__active:
            return "Հաշիվը արգելափակված է։"
        if password != self.__password:
            self.__wrong_attempts += 1
            if self.__wrong_attempts >= 3:
                self.__active = False
                self.send_email("Հաշիվը արգելափակվեց", "Ձեր հաշիվը 3 սխալ գաղտնաբառից հետո արգելափակվել է։")
                return "Սխալ գաղտնաբառ։ Հաշիվը արգելափակվեց։"
            return "Սխալ գաղտնաբառ։"
        self.__wrong_attempts = 0
        return f"Հաշիվ՝ {self.__account_number}, Մնացորդ՝ {self.__balance} դրամ"
