x = open("PreethamMapperOutput.txt",'r')
y=open("PreethamReducerOutput.txt",'w')
a = {}
s = []
for line in x:
    data = line.strip().split("\t")
    if(data[0] == "Subscriber"):
             s.append(int(data[1]))

y.write("{0}\t{1}\n".format("Subscriber",max(s)))
print(max(s))
