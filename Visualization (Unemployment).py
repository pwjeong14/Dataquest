##### BASICS ######

### Single plot 
import pandas as pd
import matplotlib.pyplot as plt

unrate = pd.read_csv('unrate.csv')
unrate['DATE'] = pd.to_datetime(unrate['DATE']) #converting the DATE column into a Series of datetime values.

first_twelve= unrate[:12] 
plt.plot(first_twelve["DATE"], first_twelve["VALUE"])

plt.xticks(rotation=90)
plt.xlabel("Month")
plt.ylabel("Unemployment Rate")
plt.title("Monthly Unemployment Trends, 1948")

plt.show()

# - - - - - - - - - - - - - 
### Multiple plots
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(12, 5)) #Without the figzie, the labels can be unreadable! 
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)

ax1.plot(unrate[0:12]['DATE'], unrate[0:12]['VALUE'])
ax1.set_title('Monthly Unemployment Rate, 1948')

ax2.plot(unrate[12:24]['DATE'], unrate[12:24]['VALUE'])
ax2.set_title('Monthly Unemployment Rate, 1949')
plt.show()

# - - - - - - - - - - - - - 

### Multiple lines in one plot

## if theres only a few lines
unrate['DATE'] = pd.to_datetime(unrate['DATE'])   #converting the DATE column into a Series of datetime values.
unrate['MONTH'] = unrate['DATE'].dt.month         #Extracting month values from "DATE" column

fig = plt.figure(figsize=(6,3))
plt.plot(unrate[0:12]['MONTH'], unrate[0:12]['VALUE'], c='red')
plt.plot(unrate[12:24]['MONTH'], unrate[12:24]['VALUE'], c='blue')

## FULL, smarter way (if a lot of lines) 
fig = plt.figure(figsize=(10,6))
colors = ['red', 'blue', 'green', 'orange', 'black']
for i in range(5):
    start_index = i*12
    end_index = (i+1)*12
    subset = unrate[start_index:end_index]
    label = str(1948 + i)
    plt.plot(subset['MONTH'], subset['VALUE'], c=colors[i], label=label)

plt.title("Monthly Unemployment Trends, 1948- 1952")    
plt.legend(loc='upper left') #a box of labels for line
plt.xlabel("Month, Integer")
plt.ylabel("Unemployment Rate, Percent")

plt.show()
