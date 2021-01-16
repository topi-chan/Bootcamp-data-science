#Napisz funkcję, która wypisze wszystkie liczby pierwsze mniejsze od
#liczby będącej argumentem funkcji.

def prime_check(a):
    prime_list = []
    for num in range(2,a+1):
       if num > 1:
           for i in range(2,num):
               if (num % i) == 0:
                   break
           else:
               prime_list.append(num)
    if prime_list[-1] == a:
        print(prime_list[:-1])
    else:
        print(prime_list)

prime_check(59)
