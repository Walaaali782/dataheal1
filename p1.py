

# class Account:
#     def __init__(self, name, account_number, initial_amount):
#         self.name = name
#         self.no = account_number
#         self.balance = initial_amount

#     def deposit(self, amount):
#         self.balance += amount
#     def withdraw(self, amount):
#         self.balance -= amount
#     def show(self):
#         s = '%s, %s, balance: %s' %(self.name, self.no, self.balance)
#         print(s)

# a1 = Account('John Olsson', '19371554951', 20000)
# a2 = Account('Liz Olsson', '19371564761', 50000)

# print("a1 balance :  " , a1.balance )
# print("a2 no      :  " ,   a2.no)

# a1.deposit(1000)
# a1.withdraw(4000)
# a2.withdraw(10500)
# a1.withdraw(3500)

# print ("a1's balance:", a1.balance)
# print ("a2's balance:", a2.balance)


# a1.show()
# a2.show()





# class Person:
#     def __init__(self, name,mobile_phone=None, office_phone=None,private_phone=None, email=None):
#         self.name = name
#         self.mobile = mobile_phone
#         self.office = office_phone
#         self.private = private_phone
#         self.email = email

#     def add_mobile_phone(self, number):
#         self.mobile = number
#     def add_office_phone(self, number):
#         self.office = number
#     def add_private_phone(self, number):
#         self.private = number
#     def add_email(self, address):
#         self.email = address
#     def dump(self):
#         s = self.name + '\n'
#         if self.mobile is not None:
#             s += 'mobile phone: %s\n' % self.mobile
#         if self.office is not None:
#             s += 'office phone: %s\n' % self.office
#         if self.private is not None:
#             s += 'private phone: %s\n' % self.private
#         if self.email is not None:
#             s += 'email address: %s\n' % self.email
#         print (s)


# p1 = Person('Hans Hanson',office_phone='767828283', email='h@hanshanson.com')
# p2 = Person('Ole Olsen', office_phone='767828292')
# p2.add_email('olsen@somemail.net')

# phone_book = [p1, p2]
# for person in phone_book:

#     person.dump()











import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# تحديد المسار الكامل للملف
file_path = 'C:/Users/MO/Desktop/Gradution Pro/healthcare_dataset.csv'

# قراءة البيانات من ملف CSV
df = pd.read_csv(file_path)

# حساب متوسط القيم لكل عمود عدد
mean_values = df.mean(numeric_only=True)

# رسم بياني للأعمدة (Bar Plot)
plt.figure(figsize=(15, 10))

plt.subplot(3, 1, 1)
sns.barplot(x=mean_values.index, y=mean_values.values)
plt.title('Mean values of each numeric column')
plt.xlabel('Columns')
plt.ylabel('Mean Value')
plt.xticks(rotation=45)

# رسم بياني للخطوط (Line Plot)
plt.subplot(3, 1, 2)
for column in df.select_dtypes(include=['number']).columns:
    plt.plot(df[column], label=column)
plt.title('Line Plot of Numeric Columns')
plt.xlabel('Index')
plt.ylabel('Value')
plt.legend()

# رسم بياني دائري (Pie Chart)
plt.subplot(3, 1, 3)
# استبدل 'ColumnName' باسم العمود الذي تريد استخدامه
column_name = 'Test Results'  # استبدله باسم العمود المطلوب
data = df[column_name].value_counts()
plt.pie(data, labels=data.index, autopct='%1.1f%%', startangle=140)
plt.title(f'Distribution of {column_name}')

# عرض جميع الرسوم البيانية
plt.tight_layout()
plt.show()
