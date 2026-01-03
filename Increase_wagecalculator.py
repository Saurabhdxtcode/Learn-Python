hrs=float(input("Enter Hours:"))
rate=float(input("Enter Rate:"))
if hrs>40:
    hrs=(40)+((hrs-40)*1.5) #hrs is converted to adjust increase 
print(hrs*rate)