import random
def main():
	n=input("Please select a number:\n1.随机输出 \n2.添加\n3.删除\n")
	switch(n)
def switch(n):
	if n=="1":
		w1()
	elif n=="2":
		w2()
	else:
		w3()
def	w1():
  # print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  last=len(quotes)-1
  rnd=random.randint(0,last)
  print(quotes[rnd])
def w2():
	f=open("quotes.txt","a")
	str=input("请输入想要添加的字符串")
	f.write("\n")
	f.write(str)
	f.close()
	f = open("quotes.txt")
	quotes = f.readlines()
	f.close()
	for quote in quotes:
		print(quote)
def w3():
	print("目前所有的如下:")
	f = open("quotes.txt")
	quotes = f.readlines()
	f.close()
	for quote in quotes:
		print(quote)
	num=int(input("请问你想删除哪一条（从1开始计数）:"))
	f=open("quotes.txt",'w')
	for i in range(0,len(quotes)):
		if i==num-1:
			continue
		f.write(quotes[i])
	f.close()
	print("result:")
	
if __name__== "__main__":
  main()
