#numbers=[12,34,54,45,450,454]
#print(numbers[5])
#data=[
 #   [1,2,3,4,5],
  #  [6,7,8,9,10,[[[45]]]]
#]    
#print(data[1][5][0][0][0])
#data=[
 #   [1,2,3,4,5,6,7,8,9,10,11,12,13],
  #  [10,15,20,25,30],
   # [35,40,45,50.75,55],
#]
#print(data[2][2])
#data=[1]
#data.append(45)
#data.append(79)
#data.append(100)
#print(data)
#print(dir(Data))
#fruits = ['apple', 'banana', 'cherry']
#fruits.append('guava')
#print(fruits)
# a=["chelsea", "liverpool", "arsenal"]
# b=["bayern munich", "psg", "spurs"]
# a.append(b)
# print(a)

# Football_Clubs=['chelsea','manutd','ac milan']
# print(Football_Clubs)
# Football_Clubs.append('liverpool')
# print(Football_Clubs)
# Football_Clubs.clear()
# print(Football_Clubs)

# console=[]
# console.append('ps')
# print(console)

data = [12,78,55,66,44,12,12,12]
data1=[45,55,6]
# data.clear()
print(data)
print(data.count(12))
data.remove(12)
data.extend(data1)
print(data.pop())
data.sort()
print(data.index(55))
print(len(data))
