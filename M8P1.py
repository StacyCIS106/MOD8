for count in range(1, 11,2):
    print(count)
for number in range (11):
    print(number)
p = float(input("Enter a principal: "))
r = float(input("Enter interest rate: "))

for count in range (1, 6, ):
    interest = p * r
    ebal = p + interest
    print(count, "  ", p, "  ", ebal)
    p = ebal 
for count in range(1, 6):
    begbal = p
    interest = begbal * r
    ebal = begbal + interest
    tolal_interest =+ interest
print(tolal_interest)