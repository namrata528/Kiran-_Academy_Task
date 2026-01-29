try:
   with open("source.txt","r") as src:
    
      with open("destination.txt","w") as dest:
         dest.write(src.read()) 
   print("file copied sucessfully")  


except FileNotFoundError:
    print("source file not found")
    

       
       