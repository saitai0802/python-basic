import  datetime
import time #It is useful when you wanna delay some operation

current_time = datetime.datetime.now()
twoDaysAfter = current_time + datetime.timedelta(days=2)
filename = current_time.strftime("%Y-%m-%d")  + ".txt"

specific_time = datetime.datetime(2017, 2, 5, 18, 00)
delta = current_time - specific_time


def create_file():
    print("Current time:" + str(current_time))
    print("Specific  time:" + str(specific_time))
    print("Two days after :" + str(twoDaysAfter))
    print("------------------------" )
    print(delta)
    print(delta.total_seconds())

    with open(str(filename), "w") as file:
        file.write("Sai is testing")

def testing_delay():
    lst = []
    for i in range(5):
        lst.append(datetime.datetime.now())
        print(lst[i])
        time.sleep(2) # 2 second


create_file()
print("=========================" )
testing_delay()