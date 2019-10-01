readInput = open("mapperOutput.txt","r") # open file, read-only raw data
reducerOutput = open("ReducerOutput.txt","w") # open file, writes final output value
count = 0
# print(len(fo))
for line in readInput:
    # splits the line separated by tab space
    data = line.strip().split('\t')
    # assign list to each variable
    usertype,gender = data
    # check the condition for usertype and gender
    if(usertype == "Subscriber" and gender == "Male"):
        count+= 1
# writes file into new reducerOutput.txt file
reducerOutput.write("The maximum male count of subscriber is: "+ str(count))
print(count)

