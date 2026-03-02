#6-misol
def max_min(a, b, c):
    return max(a, b, c)

res = max_min(2, 7, 6)
print(res)

#7-misol
def teskari(matn):
    return matn[::-1]

print(teskari("salom"))
print(teskari("Dunyo"))

#8-misol
def unlilar_soni(matn):
    sanoq = 0
    for harf in matn:
        if harf in "aeiouAEIOU":
            sanoq += 1
    return sanoq

print(unlilar_soni("salom"))

#9-misol
def palindrommi(soz):
    soz = soz.lower()
    return soz == soz[::-1]

# Sinov
print(palindrommi("alla"))
print(palindrommi("kitob"))

#10-mosol
def ortacha(royxat):
    if len(royxat) == 0:
        return 0
    return sum(royxat) / len(royxat)

print(ortacha([1, 2, 3, 4, 5]))
print(ortacha([10, 20, 30]))

#11-misol
def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        a, b = b, a + b
    return a

print(fibonacci(1))
print(fibonacci(5))
print(fibonacci(7))
