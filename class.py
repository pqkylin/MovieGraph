# encoding:utf-8
a = 9
b = 2
a, b = b, a
print a, b

print [1,2,3] * 2
aString = "hello,world"
listString = str(range(4))
print aString[1]
print listString
numList =[8,2,1,5]
print sorted(numList)
# 元组（不可变）为了安全


# 字典
# items = [('name','Mike'),('age','20')]
# itemDict = dict(items)
# print items
# fDict ={}.fromkeys(('id','score'))
# print  fDict
# for keys in items.keys():
    # print key

# 1
dict = {'name':'shabi','age':20}
print "I have a friend named %(name)s,he is %(age)s"%dict

# 集合
firstSet = set([1,2,3])
secondSet = set([3,4,5])
print firstSet & secondSet
print firstSet | secondSet
print firstSet - secondSet

for num in range(5):
    print num,
print
print[x*x for x in range(4)]
# 跳出循环
for k in range(5):
    if k == 2:
        break
    else:
        print k,
        k = k-1
print

print abs(-2)
print cmp(1,2),cmp(2,1),cmp(3,3)
print int("123")

def my(n):
     s = n * n
     return s
m = my(5)
print m

# 类
class man():
    def __init__(self,hair, height,name):
        self.hair = hair
        self.height = height
        self.name =name
    def printName(self):
            print 'my name is',self.name
class boy(man):
    def printName(self):
        print "I have a name which is",self.name
Mike = boy('short','tall','Mike')
Mike.printName()
key = man('1','2','3')
key.printName()

# def division():
#    try:
#     x = input('Enter the first number:')
#       y = input('the second one:')
#       print x/y
#    except ZeroDivisionError:


with open('/home/pengqin/桌面/1','r')as file:
    for line in file.readlines():
        print line.strip()
with open('/home/pengqin/桌面/1','a')as writeFile:
    writeFile.write('success')
print 'he said\"nice to




