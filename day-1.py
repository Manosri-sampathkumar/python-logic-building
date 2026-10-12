1.Meghna=input()
if(Meghna=="Died"):
  print("Surya weds Priya")
else:
  print("Surya weds Meghna")

2.Mark=int(input())
if(Mark >35):
  print("Pass")
else:
  print("Fail")

3.income=int(input())
if(income>7000):
  print("Eligible for Scholarship")
else:
  print("Not eligible")

4.a=10
   print(a/2)=====> for printing quetent

5. a=10
   print(a%2)======> for printing remainder

6.a=int(input())
b=int(input())
op=str(input("ADD/SUB/MUL/DIV: "))
match op:
    case "ADD":
        print(a+b)
    case "SUB":
        print(a-b)
    case "MUL":
        print(a*b)
    case "DIV":
        print(a/b)

7.score = int(input("Enter your score: "))
if(score > 70):
    print("Congratulation!..You are eligible.")
    print("Enter your details to get more info..")
    name=str(input("Your Name: "))
    dept=str(input("Your dept: "))
    location=str(input("Your location: "))

    print("Thats all!..go ahead!...")
else:
    print("You are not eligible!...")
