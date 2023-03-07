int1 = int(input())
int2 = int(input())
int3 = int(input())
int4 = int(input())

myTuple = (int1, int2, int3, int4)

print(myTuple)
print(type(myTuple))

result = 0
for i in myTuple:
    result += i

print(result)