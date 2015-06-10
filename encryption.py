@@ -0,0 +1,94 @@
#Only modulus and public key given
modulus=500249844670447
ekey=65537

CONST_BYTE=4
CONST_MAX=37

#Do not change CONST_MAX if chartable remains same...

charmap={' ':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'0':10,'a':11,'b':12,'c':13,'d':14,'e':15
	 ,'f':16,'g':17,'h':18,'i':19,'j':20,'k':21,'l':22,'m':23,'n':24,'o':25,'p':26,'q':27
	,'r':28,'s':29,'t':30,'u':31,'v':32,'w':33,'x':34,'y':35,'z':36}

def collectstring():
	c=raw_input("\nEnter the message to be encrypted (SPACES,LETTERS (not case sensitive) ,DIGITS only)\n")
	print "\n",c," - Is the input message \n"
	return c

m=collectstring()
m=m.lower()

def padding(s):
	finalcat=CONST_BYTE-(len(s)%CONST_BYTE)
	for i in range(0,finalcat):
		s=s+" "
	return s

#Padding to prevent from certain types of attacks
m=padding(m)
lists=list(m)

def conversion(duplist):
	for i in range(0,len(duplist)):
		duplist[i]=charmap[duplist[i]]
	return duplist

lists=conversion(lists)

def getnibble(duplists):
	nibbles=[]
	for i in range(0,len(duplists),CONST_BYTE):
		temp=0		
		for j in range(i,i+CONST_BYTE):
			temp=temp+(duplists[j]*(CONST_MAX**(CONST_BYTE-(j%CONST_BYTE)-1)))
		nibbles.append(temp)
	return nibbles

nibblelist=getnibble(lists)

def encodings(dupnibblelist):
	for i in range(0,len(dupnibblelist)):
		temp=dupnibblelist[i]
		temps=1
		for j in range(1,ekey+1):
			temps=(temps*temp)%(modulus)
		dupnibblelist[i]=int(temps)
	return dupnibblelist

nibblelist=encodings(nibblelist)

hexmap={0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'A',
	11:'B',12:'C',13:'D',14:'E',15:'F'}
CONST_HEX=16

def hexencoding(dupnibblelist):
	strlist=[]
	for i in range(0,len(dupnibblelist)):
		temp=dupnibblelist[i]
		strings=""
		while temp != 0:
			quo=temp/CONST_HEX
			rem=temp%CONST_HEX
			temp=quo
			strings=strings+hexmap[rem]
		strings=strings[::-1]
		strlist.append(strings)
	return strlist


nibblelist=hexencoding(nibblelist)

def finalprint(dupnibblelist):
	print "The final encoded message in hexa is\n"
	newstr=""
	for i in range(0,len(dupnibblelist)):
		if i == 0:
			newstr=newstr+dupnibblelist[i]
			continue
		newstr=newstr+" "+dupnibblelist[i]
	print newstr

finalprint(nibblelist)

