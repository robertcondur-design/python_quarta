n = int (input("Inserisci qaunti numeri di fibonacci vuoi? -> " ))
a, b = 1, 1

if n>2:
    
    for i in range(n):

        print(a, end = " - ")
        a, b = b, a+b
        
if n==2:
    print(a, end = " - ")
    print (b)
elif n == 1:
    print (a)
elif n == 0:
    print("Non ci sono numeri da inserire")

