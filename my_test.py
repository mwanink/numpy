import numpy as np
np.random.seed(0)

a = np.array([np.datetime64('2005-02-25'), np.datetime64(365,'D')]) #np.datetime64(1, 'Y')])
print(np.median(a))

a = np.array([np.datetime64('2005-02-25'), np.datetime64(1,'Y')]) #np.datetime64(1, 'Y')])
print(np.median(a))

a = np.array([np.datetime64('2005-02-25'), np.datetime64(366,'D')]) #np.datetime64(1, 'Y')])
print(np.median(a))

a = np.array([np.datetime64('2005-02-25'), np.datetime64(367,'D')]) #np.datetime64(1, 'Y')])
print(np.median(a))

a = np.array([np.datetime64('2005-02-25'), np.datetime64(13,'M')]) #np.datetime64(1, 'Y')])
print(np.median(a))

a = np.array([np.datetime64('2005-02-25'), np.datetime64(1,'Y'), np.datetime64(11,'M')]) #np.datetime64(1, 'Y')])
print(np.median(a))

month_arr = np.random.randint(1, 13, 10)
day_arr = np.random.randint(1,29, 5)



a = []
for month in month_arr:
    month = format(month, "02d")
    for day in day_arr:
        day = format(day, "02d")
        date = f"2000-{month}-{day}"
        a.append(np.datetime64(date))

a = np.array(a)
print(np.median(a))

a = np.append(a, [np.datetime64(3, "M")])

print(np.median(a))

