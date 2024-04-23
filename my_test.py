import numpy as np
np.random.seed(0)

print("Even Array Test Suite:")
print()
a = np.array([np.datetime64('2005-02-25'), np.datetime64(365,'D')]) #np.datetime64(1, 'Y')])
print("Expected: 1988-01-29, Actual:", np.median(a))
print()

a = np.array([np.datetime64('2005-02-25'), np.datetime64(1,'Y')]) #np.datetime64(1, 'Y')])
print("Expected: 1988-01-29, Actual:", np.median(a))
print()

a = np.array([np.datetime64('2005-02-25'), np.datetime64(366,'D')]) #np.datetime64(1, 'Y')])
print("Expected: 1988-01-29, Actual:", np.median(a))
print()

a = np.array([np.datetime64('2005-02-25'), np.datetime64(367,'D')]) #np.datetime64(1, 'Y')])
print("Expected: 1988-01-30, Actual:", np.median(a))
print()

a = np.array([np.datetime64('2005-02-25'), np.datetime64(13,'M')]) #np.datetime64(1, 'Y')])
print("Expected: 1988-02-13, Actual:", np.median(a))
print()

print("Additional Tests:")
print()
a = np.array([np.datetime64('2005-02-25'), np.datetime64(1,'Y'), np.datetime64(11,'M')]) #np.datetime64(1, 'Y')])
print("Expected from odd: 1971-01-01, Actual:", np.median(a))
print()

month_arr = np.random.randint(1, 13, 10)
day_arr = np.random.randint(1,29, 5)
year_arr = np.random.randint(1975, 2024, 10)


a = []
for year in year_arr:
    for month in month_arr:
        month = format(month, "02d")
        for day in day_arr:
            day = format(day, "02d")
            date = f"{year}-{month}-{day}"
            a.append(np.datetime64(date))

a = np.array(a)
print("Expected from random seed 0: 1999-12-30, Actual:", np.median(a))
print()

a = np.append(a, [np.datetime64(3, "M")])

print("Expected with append: 1999-12-25, Actual:", np.median(a))
print()

