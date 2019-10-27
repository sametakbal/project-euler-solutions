first = 1
second = 1
total = 0
term = 2

while(term<4000000):
    term=first+second
    if(term%2==0):
        total+=term
    first=second
    second=term
print(total)