list = input().split()
lists = []
modus_value = 0
modus = ''


for i in range(1,10):
    count = list.count(str(i))
    if count>0:
        lists.append([i, count])

for i in lists:
    if i[1]> modus_value:
        modus_value=i[1]
        modus = i[0]

print(modus)