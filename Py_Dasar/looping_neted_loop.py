# Nested Loop 1
print('Nested Looping')
for i in range(5):
    for j in range(i+1):
        print('*', end='')
    print('')

# Nested Loop 2
string = ""
bar = 1
# Looping Baris
while bar <= 5:
    kol = bar
    # Looping Kolom
    while kol > 0:
        string += "*"
        kol = kol - 1
    string += "\n"
    bar = bar + 1
print (string)

# Nested Loop 3
a = 6
for i in range(0, a):
    for j in range(0, a - 1):
        print('*', end= '')
    a -= 1
    print('')

# Nested Loop 4
a = 5
s = a - 1 #for spaces
for i in range(0, a):
    for j in range(0, s):
        print(' ', end='')
    s -= 1
    for j in range(0, i + 1):
        print('* ', end='')
    print('')
