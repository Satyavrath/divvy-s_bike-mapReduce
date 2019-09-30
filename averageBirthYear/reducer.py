input_reducer = open("output_mapper.txt","r")
output_reducer = open("output_reducer.txt", "w")
lines = input_reducer.readlines()
lines.sort()
total = 0
length = 0
for line in lines:
    data = line.strip().split(',')
    usertype = data[0]
    try:
        birthyear = float(data[1])
        length = length + 1
        total = total + birthyear
    except ValueError:
        continue


average = total/length
output_reducer.write(usertype+","+str(average)+"\n")
print(usertype+","+str(average)+"\n")
input_reducer.close()
output_reducer.close()