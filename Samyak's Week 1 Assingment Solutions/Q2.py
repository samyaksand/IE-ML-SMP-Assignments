sub1=int(input("First subject marks = "))
sub2=int(input("Second subject marks = "))
sub3=int(input("Third subject marks = "))
sub4=int(input("Fourth subject marks = "))
sub5=int(input("Fifth subject marks = "))
total = sub1+sub2+sub3+sub4+sub4
print(total)
print()

print("Total Marks : ",total)
per = total/5
print("Percentage = " , per)

if(per < 50 ):
        print("Your Grade is C")
elif per>=50 and per<80:
    print("Your Grade is B")
elif avg>=80:
    print("Your Grade is A")
else:
    print("Invalid Input!")