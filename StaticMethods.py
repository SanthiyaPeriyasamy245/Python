
''' To access any method of a class we require object of that class to access any method
without creating an object we need to use annotation to mention that this method is static '''

class laptop():
    @ staticmethod 
    def display():
        print("it's static method")
        return
        
if __name__=='__main__':
    obj=laptop()
    obj.display()
    laptop.display() # alternatively we can call like this also.
    

    

     
