import pandas as pd
import matplotlib.pyplot as plt

file = "پروژه 3.xlsx"
excel = pd.read_excel(file)
size = excel.iloc[:,0]
alg1 = excel.iloc[:,1]
alg2 = excel.iloc[:,2]
alg3 = excel.iloc[:,3]

plt.figure(figsize=(12,8))
width = 0.25
x = range(len(size))
plt.bar([i-width for i in x],alg1,width,label="algorithm 1")
plt.bar(x,alg2,width,label="algorithm 2")
plt.bar([i+width for i in x],alg3,width,label="algorithm 3")
plt.xticks(x,size)
plt.xlabel("Size")
plt.ylabel("Time")
plt.title("Bar Chart")
plt.legend()
plt.show()

plt.figure(figsize=(12,8))
plt.plot(size,alg1,marker="o",label="algorithm 1")
plt.plot(size,alg2,marker="o",label="algorithm 2")
plt.plot(size,alg3,marker="o",label="algorithm 3")
plt.xlabel("Size")
plt.ylabel("Time")
plt.title("Line Chart")
plt.legend()
plt.show()

plt.figure(figsize=(12,8))
plt.boxplot([alg1,alg2,alg3],labels=["algorithm 1","algorithm 2","algorithm 3"])
plt.title("Box Plot")
plt.ylabel("Time")
plt.show()

print("Average Algorithm 2 =",alg2.mean())