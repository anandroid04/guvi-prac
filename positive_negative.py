
def check():
    try:
        n=int(input())
           if n>0:
                print("Positive")
            elif n==0:
                print("Zero")
            else:
                print("Negative")
       exccept ValueError:
         print("Invalid")
check()
