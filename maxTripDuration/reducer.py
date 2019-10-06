x = open("PreethamMapperOutput.txt",'r')
#open file, read-only raw data
y = open("PreethamReducerOutput.txt",'w')
# open file, write - just our key, value pairs
s = []
for line in x:
    # parses for line starting with quotes
    data = line.strip().split("\t")
    # splits the line separated by comma
    usertype,tripduration = data
    if(data[0] == "Subscriber"):
             s.append(int(data[1]))

def maxtripduration(l):
    high = l[0]
    for find_max in l:
        if high < find_max:
            high = find_max
    return high
print(maxtripduration(s))
y.write("{0}\t{1}\n".format(usertype,maxtripduration(s)))

