# n = int(input("enter the number: "))

def fizz_buzz(n):
        for i in range(1,n+1):
            if (i%5==0) and (i%3==0):
                print("fizz buzz")
            elif (i%3==0):
                print("fizz")
            elif (i%5==0):
                print("buzz")
            else:
                print(i)
fizz_buzz(100)
