@@ -0,0 +1,105 @@
#Decryption is pretty much similar to encryption
import math
CONST_BYTE=4
CONST_MAX=37
#dkey=561833567663513
dkey=61583767731937
modulus=500249844670447

p=22746029
q=21992843
#p and q are necessary because we are using Chinese Remainder Theorem in decryption
CONST_HEX=16

mainstr=raw_input("\nEnter the encrypted message \n")
mainstr.upper()
mainstr=mainstr+" "
print "\n The entered message is \n",mainstr,"\n"

def puttolist(dupstr):
	duplist=[]
	temp=""
	for i in range(0,len(dupstr)):
		chars=dupstr[i]
		if chars == ' ':
			duplist.append(temp)
			temp=""
			continue
		temp=temp+chars
	return duplist

strlist=puttolist(mainstr)

hextable={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'A':10,'B':11,
	'C':12,'D':13,'E':14,'F':15}

def convertfromhexa(duplist):
	templist=[]
	for i in range(0,len(duplist)):
		temp=0
		tempstr=duplist[i]
		count=0
		for j in range(len(tempstr)-1,-1,-1):
			temp=temp+hextable[tempstr[j]]*(CONST_HEX**count)
			count=count+1
		templist.append(temp)
	return templist

strlist=convertfromhexa(strlist)

def modulardecrypt(dupstrlist):
	templist=[]
	dP=(dkey)%(p-1)
	dQ=(dkey)%(q-1)
	qInv=(25573965)
	for j in range(0,len(dupstrlist)):
		num=dupstrlist[j]
		temp1=1
		temp2=1
		for i in range(1,dP+1):
			temp1=(temp1*num)%(p)
		for i in range(1,dQ+1):
			temp2=(temp2*num)%(q)
		h=((qInv*(temp1+p-temp2))%p)
		dec=temp2+(h*q)
		templist.append(int(dec))
	return templist

strlist=modulardecrypt(strlist)

def converttonumlist(dupstrlist):
	templist=[]
	for i in range(0,len(dupstrlist)):
		temp=dupstrlist[i]
		rem=0
		quo=0
		for j in range(CONST_BYTE-1,-1,-1):
			quo,temp=divmod(temp,(CONST_MAX**j))
			templist.append(quo)
	return templist

strlist=converttonumlist(strlist)

revmap={0:' ',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'0',11:'a',12:'b',13:'c',14:'d',15:'e',16:'f',
	17:'g',18:'h',19:'i',20:'j',21:'k',22:'l',23:'m',24:'n',25:'o',26:'p',27:'q',28:'r',
	29:'s',30:'t',31:'u',32:'v',33:'w',34:'x',35:'y',36:'z'}

def converttostr(dupstrlist):
	for i in range(0,len(dupstrlist)):
		dupstrlist[i]=revmap[dupstrlist[i]]
	return dupstrlist

strlist=converttostr(strlist)

def removepad(dupstrlist):
	i=len(dupstrlist)-1
	while dupstrlist[i] == ' ':
		dupstrlist.pop()
		i=i-1
	strs=""
	for i in range(0,len(dupstrlist)):	
		strs=strs+dupstrlist[i]
	return strs
final=removepad(strlist)
print "The decoded message is\n",final
