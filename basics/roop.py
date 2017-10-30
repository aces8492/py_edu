#while
print("start \"while\" statement ");
i = 0;
name = "Yosuke";
while i < 10:
    if i == 5:
        break
    print ("%d:%s"%(i,name));
    i += 1;
else:
    print("finish");

#for and range
print("\n start \"for\" statement ");
for i in range(0,10):
    if i == 5:
        #break
        #To skip when i=5
        print("skipped");
        continue;
    else:
        print(i);
else:
    print("Finish!");
