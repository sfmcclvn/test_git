print('hello aaaa')



#u1 = 1
#u2 = u1 + u1
#u3 = u2 + u1
#u4 = u3 + u4 


u1 = 1
u2 = 1
hasil=[u1,u2]
n = 5

for i in range(n-2):
    u3 = u1 + u2
    hasil.append(u3)
    u1 = u2
    u2 = u3

print(hasil)

