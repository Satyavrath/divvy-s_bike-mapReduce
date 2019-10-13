x = open("Mapperoutput.txt","r")
#open file, read-only raw data
y = open("reduceroutput.txt","w")
# open file, write - just our key, value pairs

k = []
for line in x:
    # parses for line starting with quotes
    data = line.strip().split("\t")
    # splits the line separated by comma
    usertype,tripduration = data
    if(data[0] == "Subscriber"):
            k.append(int(float(data[1])))
def minTripDuration(l):
    low = l[0]
    for find_min in l:
        if low > find_min:
            low = find_min
    return low  
print(minTripDuration(k))      
y.write("{0}\t{1}\n".format(usertype,minTripDuration(k)))            

        