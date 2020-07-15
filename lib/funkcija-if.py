var = 11

if var < 10:
    print("yra maziau")
else:
    print("yra daugiau")


def biggest_of_three(num):
    return num

num1 = 130
num2 = 131
num3 = 130

num = num1

if num < num2:
    num = num2
if num < num3:
    num = num3

print(biggest_of_three(num))



#looking_for_name='jonas'
pozicija=1

client_list=['jonas', 'kazys', 'jake']

#for looking_for_name in client_list:
#    print(client_list)

for index in range(len(client_list)):
    #if list_member is 'jake'
    #    break        print('enumerate style of cycling')

    if client_list is 'jonas':
        print(f'Index: {index} list_member: {client_list[index]}')
for index, member in enumerate(client_list):
        print(f'Index: {index} list_member: {member}')

    #if looking_for_name  'jake':
     #   print(f'Index: {index} list_member: {looking_for_name}')
     #   break