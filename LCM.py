Alpha = 6
Beta = 8
Gamma = 9

first_year = 1980
last_year = 3000

for i in range(first_year, last_year, Alpha):
    for j in range(first_year, last_year, Beta):
        for k in range(first_year, last_year, Gamma):
            if (i == j) & (j == k):
                print(i)