a = 1
l = []
stopexercising = False
if stopexercising == False:
    while True:
        reps = input(f'Enter the number of reps in the approach №{a} or enter "stop" to stop: ')
        try:
            reps = int(reps)
            l.append(reps)
            a += 1
        except:
            if reps == 'stop':
                stopexercising = True
                break
            else:
                print('You entered a wrong value')
if a == 1 and reps == 'stop':
    a = 0
print(f'The number of approaches: {a}')
b = 0
for i in l:
    b += i
if len(l)!= 0:
    print(f'The overall number of reps: {b}')
    print(f'The max number of reps: {max(l)}')
    print(f'The min number of reps: {min(l)}')
    print(f'The average number of reps: {b/len(l)}')
