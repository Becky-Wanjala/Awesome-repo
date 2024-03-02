my_list=[]
print("1.my_list:",my_list)
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("2.After append:",my_list)
my_list.insert(1,15)
print("3.After inserting 15:",my_list)
my_list=[10,20,30,40]
my_list.extend([50,60,70])
print("4.Extend:",my_list)
my_list =['10','20','30','40']
my_list.remove('40')
print("5.Afterbremoving 40:",my_list)
my_list =[10,20,30,40]
my_list.sort()
print("6.list in Ascending order:",my_list)
index_of_30= my_list.index(30)
print("7.Index of 30:",index_of_30)