# Step 3.2

with open('result\word-assignments.dat','r') as word:
    for line in word:
        linespl=line.split(' ')
        collect=[i.split(':') for i in linespl[1:]] # [['100', '00'], ['101', '02'], ['11456', '02'], ['189', '04']]
        for num in range(5):
            wordn=[i for i,j in collect if int(j)==num]
            if len(wordn)>0:
                with open('topic-'+str(num)+'.txt','a') as topicf:
                    topicf.write(' '.join(wordn)+'\n')
