#suma cifre ale numerelor din fisier
def write_sum(in_file, out_file):
    #your code here
    try:
        li=[]
        f1=open(in_file, 'r')
        text=f1.read()
        f1.close()
        li=text.split()
        suma=0
        for i in li:
            i=int(i)
            while i!=0:
                suma=suma+i%10
                i=i//10
        f2=open(out_file,'w')
        f2.write(str(suma))
        print(suma)
        f2.close()
    except:
        print(0)
        f2=open(out_file,'w')
        f2.write('0')
        f2.close()

write_sum("in.txt","out.txt")
