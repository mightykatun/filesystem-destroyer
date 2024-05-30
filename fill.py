import os
import random as rd

def fill(size_mb):
	size_mb_rand = size_mb
	i = 0
	while True:
		i += 1
		a = rd.randint(-size_mb // 50, size_mb // 50)
		size_mb_rand += a
		try:
			with open(f"{i}.tar.gz", "w") as file:
				file.truncate(size_mb_rand * 10 ** 6)
		except:
			print(f"Drive filled with {i} files of {size_mb} MB")
			os.remove(f"{i}.tar.gz")
			break
		else:
			with open(f"{i}.tar.gz", "w") as file:
				file.truncate(size_mb_rand * 10 ** 6)

size_mb = int(input("Enter size (MB): "))

fill(size_mb)
