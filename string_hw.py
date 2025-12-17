name="Namrata Shinde"
 # Slicing 
print(name[0:7])  # Namrata
print(name[8:14]) # Shinde 
print(name[0:14]) # Namrata Shinde
# reverse slicing
print(name[: :-1]) # ednihS atarmaN 

print(name[:7]) # Namrata 
print(name[8:]) # Shinde
print(name[:])  # Namrata Shinde  
print(name[-14:-7]) # Namrata
print(name[-14:-7:2]) # Nmr a

print(name[0:14:2]) # NmaaSid 

# iterate string using for loop 
for char in name:
    print(char) 
# iterate string in reverse order using for loop
for char in name[::-1]:
    print(char)
# iterate namrata by slicing
for char in name[0:7]:
    print(char)    

# count a from given string   
count=0 
for char in name:
    if char =="a":
        count=count+1 
print("Count of a:",count)  

# iterate even index string 
for char in name[::2]:
    print(char)
    

