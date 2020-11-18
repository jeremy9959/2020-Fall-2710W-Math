f0,f1 = 1,1
for i in range(20):
    print('{}\t\t{}\t\t{:1.9f}'.format(f0,f1,f1/f0))
    f0,f1=f1,f0+f1
    
