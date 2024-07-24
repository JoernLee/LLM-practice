# 这是注释
"""
这是
多行
注释
"""
print('Hello World')

# 定义变量 - 基本类型
name = '乔恩'
age = 23
height = 1.8
address = '北京市昌平区'
isTrue = True
# 打印变量
print(name, age, address)

# 输入
user_input = input('请输入：')
print(user_input)

# 条件结构
age = int(input('请输入你的年龄：'))

if age >= 18:
    print('已成年')
else:
    print('未成年！')

print('-' * 40)

# 循环结构
for i in range(6):
    print(i)

for i in range(1, 6):
    if i == 3:
        print('吃饱了')
        break
    print(f'正在吃{i}个苹果')


# 函数
def great(name):
    print(f"Hello {name}")


great('Joern')


# 使用关键字参数
def greet(first_name, last_name):
    print(f"Hello, {first_name} {last_name}!")


greet(last_name="Smith", first_name="John")

# 定义一个匿名函数并立即调用
result = (lambda x, y: x + y)(3, 5)
print(result)

# 将匿名函数赋值给变量
add = lambda x, y: x + y
print(add(3, 5))


# 面向对象开发
class Person:
    # 类变量
    species = "human"

    # 构造方法（初始化方法）
    def __init__(self, name, age):
        # 实例变量
        self.name = name
        self.age = age

    # 实例方法
    def greet(self):
        return f"Hello, my name is {self.name} and I'm {self.age} years old."

    # 另一个实例方法
    def get_species(self):
        return self.species


# 创建对象
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

# 访问对象的属性和调用方法
print(person1.name)
print(person2.age)
print(person1.greet())
print(person2.get_species())


# 定义一个子类 Student 继承自 Person
class Student(Person):
    def __init__(self, name, age, student_id):
        # 调用父类的构造方法
        super().__init__(name, age)
        # 新的实例变量
        self.student_id = student_id

    # 重写父类方法
    def greet(self):
        return f"Hello, my name is {self.name}, I'm {self.age} years old, and my student ID is {self.student_id}."


# 创建 Student 对象
student1 = Student("Eve", 20, "2023001")

# 调用继承的方法
print(student1.greet())


# 定义一个接口类 Animal
class Animal:
    def sound(self):
        pass


# 定义 Dog 类继承自 Animal
class Dog(Animal):
    def sound(self):
        return "Woof!"


# 定义 Cat 类继承自 Animal
class Cat(Animal):
    def sound(self):
        return "Meow!"


# 调用不同对象的相同方法，得到不同的结果
animals = [Dog(), Cat()]

for animal in animals:
    print(animal.sound())
