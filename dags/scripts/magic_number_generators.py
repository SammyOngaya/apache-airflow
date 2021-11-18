import random
from datetime import datetime

def generate_magic_numbers():
    data=[]
    
    data.append(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    numbers = [random.randrange(1, 50, 1) for i in range(10)]
    data.append(numbers)

    f = open("/c/Users/soongaya/AirflowHome/dags/scripts/magic_numbers.txt", "a")
    f.writelines(str(data)+"\n")
    f.close()
    print(data)
    return data

generate_magic_numbers()