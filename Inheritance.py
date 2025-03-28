class parent:
     def play(self):
         print("move forward")
         print("move backward")
    
class child(parent): # Here we have inherited the child class with parent class.
    
     def newbutton(self):
         print("move left side")
         print("move right side")
if __name__=='__main__':
    
    c=child()
    c.newbutton()
    c.play()
    p=parent()
    p.play()
   
    

     
