input_reducer = open("output_mapper.txt","r")# open file, read-only raw data
output_reducer = open("output_reducer.txt", "w") # open file, writes final output value
lines = input_reducer.readlines()#reading each line from data and storing it in array
lines.sort()#sorting the array
total = 0
length = 0
for line in lines:
     # splits the line separated by comma
    data = line.strip().split(',')
    usertype = data[0]#Assigning data to sex
    try:
        birthyear = float(data[1])
        length = length + 1
        total = total + birthyear
    except ValueError:
        continue

#finding average
average = total/length
# writes usertype and average files into new output_reducer.txt file
output_reducer.write(usertype+","+str(average)+"\n")
#writing usertype and average to console input
print(usertype+","+str(average)+"\n")
#closing files
input_reducer.close()
output_reducer.close()