
 # polymorphism
 
class version1:
    def func1(self):
        print("hi welcome")
 
 
class version2(version1):
    def func1(self):
        print("hi , this is new version")

if __name__=='__main__':
    newgame=version2() 
    newgame.func1()
    newgame.func1()