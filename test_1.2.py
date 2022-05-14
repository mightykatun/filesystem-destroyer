import random as rd
import time as tm
from tqdm import tqdm
while True:
    nchoice = input("enter number of files ")
    try:
        ntimes = int(nchoice)
    except ValueError:
        print("must be number")
    else:
        break
while True:
    schoice = input("enter file size ")
    try:
        size = int(schoice)
    except ValueError:
        print("must be number")
    else:
        break
print("")
print("starting process")
print("generating %s files of size %s" % (ntimes, size))
print("")
tm.sleep(0.5)
start = tm.time()
for i in tqdm(range(ntimes)):
    with open("out\\test-{}.txt".format(int(i+1)), "w+") as file:
        for j in range(size):
            text = hex(rd.randint(10**10, 10**11))
            file.write(text)
    file.close()
end = tm.time()
print("")
print("end of process")
print("%s files generated in %s s" % (ntimes, round((end-start), 2)))
input("enter to terminate")
