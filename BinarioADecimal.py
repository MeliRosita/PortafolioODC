def BinDec(n):
    S=0
    i=0
    print('El binario',n,end='')
    while(n>=1):
        d=n%10;
        n=int(n/10)
        S=S+d*pow(2,i);
        i=i+1
        
    print(' corresponde al número',S)
    
BinDec(1100100)