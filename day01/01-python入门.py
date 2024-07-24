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

for i in range(1,6):
    if i == 3:
        print('吃饱了')
        break
    print(f'正在吃{i}个苹果')