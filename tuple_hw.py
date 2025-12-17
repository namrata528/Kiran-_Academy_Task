 # add list in tuple and process that tuple
list_1=[400,500,"hello",50.8,True]
t=(10,20,30,list_1,40,50 ,"welcome")
print(t)
print(id(t))  

# Iterate welcome from the given tuple 
print(t[-1]) 

# using for loop iterate list from tuple 
for element in t:
    if type(element)==list:
        for item in element:
            print(item)        # 400 500 hello 50.8 True

 # add a tuple on list and process your list
tuple_1=("python " ,"java " ,"c","c++")
list_2=["SQl","html","css",tuple_1,"js"]
print(list_2)
print(type(list_1))  

 # using for loop iterate tuple from list 


for ele in list_2:
     if type(ele)==tuple:
        for items in ele:
         
         print(items,end=" ")   # python  java  c  c++

# append 60 in tuple 
t=(10,20,30,40) 
list_a=list(t) 
list_a.append(60) 
t=tuple(list_a) 
print(t)          # (10, 20, 30, 40, 60)
print(min(t))    # 10
print(max(t))    #60 
print(sum(t))  # 160  

# swap two variable using tuple 
a=10 
b=20 
a,b=b,a 
print(a) #20 
print(b) #10  

# print only subtuple elements ignore non tuple 
t=(1,(2,4,),(8,9),5,"hello", (10,12,14)) 
for item in t:
    if isinstance(item,tuple):    # isinstance() is a built-in Python function used to check the data type of a variable or object.
        print(item)     # (2, 4)  (8, 9)  (10, 12, 14) 


# Remove empty typle from tuple
t1=(1,(2,4,),(),(8,9),())  
list_b=list(t1) 
print(id(t1))
print(list_b)
for item in list_b: 
    if item==():
        list_b.remove(item)  
print(list_b)   
t1=tuple(list_b)  
print(t1)                   # (1, (2, 4), (8, 9)) 
print(id(t1))   

# t1=(1,(2,4,),(),(8,9),())   

# for item in t1: 
#     if item==():
#         t1.remove(item)     # AttributeError: 'tuple' object has no attribute 'remove'
# print(t1)   

 
