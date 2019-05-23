# _*_ coding=utf-8 _*_


import csv

# with open('data.csv', 'w') as f:
#     writer = csv.writer(f)
#     writer.writerow(['id', 'name', 'age'])
#     writer.writerow(['1', 'rain', '20'])
#     writer.writerow(['2', 'godric', '22'])
#     writer.writerow(['3', 'tony', '25'])

# 修改分隔符
# with open('data.csv', 'w') as f:
#     writer = csv.writer(f, delimiter="-")
#     writer.writerow(['id', 'name', 'age'])
#     writer.writerow(['1', 'rain', '20'])
#     writer.writerow(['2', 'godric', '22'])
#     writer.writerow(['3', 'tony', '25'])

# 字典写入,newline去掉空行
# with open('data.csv', 'w', newline='') as f:
#     field_name = ['id', 'name', 'age']
#     writer = csv.DictWriter(f, fieldnames=field_name)
#     writer.writeheader()
#     writer.writerow({'id': '1', 'name': 'rain', 'age': '20'})
#     writer.writerow({'id': '2', 'name': 'godric', 'age': '22'})
#     writer.writerow({'id': '3', 'name': 'tony', 'age': '25'})

# 追加
# with open('data.csv', 'a') as f:
#     field_name = ['id', 'name', 'age']
#     writer = csv.DictWriter(f, fieldnames=field_name)
#     writer.writeheader()
#     writer.writerow({'id': '4', 'name': 'thor', 'age': '1000'})


# 中文需要指定编码
# with open('data.csv', 'a', encoding='utf-8') as f:
#     field_name = ['id', 'name', 'age']
#     writer = csv.DictWriter(f, fieldnames=field_name)
#     writer.writeheader()
#     writer.writerow({'id': '5', 'name': '王翔', 'age': '22'})

# 文件读取
with open('data.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

import pandas as pd

data = pd.read_csv('data.csv')
print(data)
