import os

a = 'C:/Users/YJK/Desktop/meng/'
x = 0
for i in os.listdir(a):
    os.rename(a + i, a + str(x) + os.path.splitext(a + i)[1])
    x += 1
