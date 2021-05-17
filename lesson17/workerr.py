import json
import re

class Worker:
    def __init__(self, name, rank, phone_number, email):
        self.name = name
        self.rank = rank
        self.phone_number = phone_number
        self.email = email
        self.n = 0

    def __str__(self):
        self.n += 1
        return f'name : {self.name}\nrank : {self.rank}\nphone_number : {self.phone_number}\nemail : {self.email}'

while True:
    workers_name = input("Enter worker's name: ")
    if re.match('[A-Za-z]{2,25}\s[A-Za-z]{2,25}', workers_name):
        pass
    else:
        print("Enter name in the proper format (name and surname using uppercase without numbers and other characters")
        break

    workers_rank = input("Enter worker's rank: ")
    if re.match('[A-Za-z]{2,25}', workers_rank):
        pass
    else:
        print("Enter rank in the proper format")
        break
    workers_phone_number = input("Enter worker's phone number: ")
    if re.match("\w{3}-\w{3}-\w{4}", workers_phone_number):
        pass
    else:
        print("Enter worker's phone number in the proper format")
        break

    workers_email = input("Enter worker's email: ")
    if re.match('^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$', workers_email):
        pass
    else:
        print("Enter email in the proper format")
        break

worker = Worker(workers_name, workers_rank, workers_phone_number, workers_email)
with open("workerdatabase.json", "+a") as f:
    json.dumps(str(worker))
    f.write(str(worker))
