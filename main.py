from SerialRead import Arduino
import time
buf1 = []
buf2 = []
buf3 = []
#Clear file contents if exists
open("neck.txt", "w").close()
open("back.txt", "w").close()
open("textile.txt", "w").close()
start = time.time()
#Ayrı thread'den datalar bu fonksiyona düşecekler.
#Data geldikçe kullanabilirsiniz.
def ReadValues(val):
    #print(val)
    
    f1 = open("neck.txt", "a")
    f2 = open("back.txt", "a")
    f3 = open("textile.txt", "a")
    
    if(val[0:4] == "neck"):
        buf1.append(val[4:] + '\n')
        
        #print(val)       
        
    elif val[0:4] == "back":
        buf2.append(val[4:] + '\n')
        #print(val)   
        #print("Adding to buf2")
    else:
        val = val[7:]
        val = val.replace(';', ',')
        buf3.append(val + '\n')

    if len(buf1) >= 50:
        f1.writelines(buf1)
        end = time.time()
        f1.write("time: " + str(end - start)+ '\n')
        buf1.clear()
        print("Written to file1")
    if len(buf2) >= 50:
        f2.writelines(buf2)
        end = time.time()
        f2.write("time: " + str(end - start) + '\n')
        buf2.clear()
        print("Written to file2")
    if len(buf3) >= 50:
        f3.writelines(buf3)
        end = time.time()
        f3.write("time: " + str(end - start) + '\n')
        buf3.clear()
        print("Written to file3")

    


arduino1 = Arduino(ReadValues, "COM5")
arduino2 = Arduino(ReadValues, "COM6")
time.sleep(1.8)
arduino3 = Arduino(ReadValues, "COM7")


#Kapatmak için
#carduino1.run = false