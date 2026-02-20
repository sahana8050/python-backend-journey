arr=[7,1,5,6,4]                       # from this comment lines we can understand easyly 
smallest=arr[0]
profit=0                               #x=7 done             #x=1 done                                  #x=5                                        #x=6
for x in arr:
    if x<smallest:                    #7<7 no then           #x=1,smallest=7 then x<smallest 1<7 true  # x=5,smallest=1 then x<smallest =5<1 false  #x=6,smallest=1 then x<smallest=6<1 false
        smallest=x                    #smallest=7            #smallest=x  smallest=1                   # then elif x-smallest>profit 5-1>0=4 true   # then elif x-smallest>profit  6-1>4 true
    elif x-smallest>profit:           # x-smallest 7-7=0 >0                                            #profit=x-smallest 5-1=4                     #profit=x smallest 6-1=5
        profit=x-smallest             #profit=0                                                        #profit=4                                     #profit=5  same as this loop continues untill end of arr index
        print(profit)                 #profit=0