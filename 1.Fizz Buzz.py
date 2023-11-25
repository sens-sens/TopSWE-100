class Solution:
    
    # If n=5, return ["1","2","Fizz","4","Buzz"]
    
    def getResult(self,num):
    
        if num%3==0 and num%5==0:
            return "FizzBuzz"
        elif num%3==0:
            return "Fizz"
        elif num%5==0:
            return "Buzz"
        else:
            return str(num)
        
    def fizzBuzz(self, n: int) -> List[str]:
    
            ans=[]
    
            for i in range(1,n+1):
                ans.append(self.getResult(i))
            return ans