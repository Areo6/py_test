class Numbers(object):
    def __init__(self,num = 13):
        if not isinstance(num,int):
            raise ValueError("Illigal argument,integers only allowed")
        else:
            self.num = num

    def fuzzbuzz(self):
        "Numbers divisble by 3,5 or both"
  
        #if Number divisible by 3 and 5, return FuzzBuzz
        if self.num % 3 == 0 and self.num % 5 == 0:
            return "FuzzBuzz"
    
        #If Number divisile by 3, return Fuzz  
        elif self.num % 3 == 0:
            return "Fuzz"
    
        #If Number divisible by 5, return Buzz
        elif self.num % 5 == 0:
            return "Buzz"
        else:
            return "Number not divisible by 3 or 5"


    def factorial(self):
        "Return the factorial of a given number"
  
        factorial = 1
        if isinstance(self.num,int):
            #multiplies the number with all the preceding ones up to 1.
            for i in range(1,self.num+1):
                factorial *= i
            return factorial
        else:
            return 'Illigal argument'


    def fibonacci(self):
        "Return true if a numer is in the fibonacci sequence. False other wise."
  
        fibo = []
        a,b = 0,1
        for i in range(self.num+1):
            fibo.append(b)
            a,b = b,a+b
        if self.num in fibo:
            return True
        else:
            return False

if __name__ == "__main__":
    num = Numbers(13)
    print(num.fibonacci())