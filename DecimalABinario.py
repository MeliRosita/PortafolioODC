def DecBin(n):
    d=[]
    print('El número',n,end='')
    while(n>=1):
        d.append(n%2);
        n=int(n/2)
    
    S=d[::-1]
        
    print(' corresponde al binario ',end='')
    [print(k,end='')for k in S]
    
DecBin(100)