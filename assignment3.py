def triangle(s1, s2, s3):
    if s1*2 + s2*2 == s3*2:
        print("Right angle triangle")
    elif s2*2 + s3*2 == s1*2:
        print("Right angle triangle")
    elif s3*2 + s1*2 == s2*2:
        print("Right angle triangle")
    else:
        print("Not a Right angle triangle!")

s1 = int(input("Enter the length of first side: "))
s2 = int(input("Enter the length of second side: "))
s3 = int(input("Enter the length of third side: "))

triangle(s1, s2, s3)