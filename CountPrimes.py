import math
class Solution(object):
          

     def countPrimes(self, n):
        if n==0 or n==1 or n==2:
            return 0
        count=0
        
        list_boolean=[True]*n
        

        for i in range (2,len(list_boolean)):
            if (list_boolean[i]):
                for j in range(i+i,len(list_boolean),i):
                    list_boolean[j]=False


        for i in range(2,len(list_boolean)):
            if(list_boolean[i]):
                count+=1            
             
            
               
        return count
      
        