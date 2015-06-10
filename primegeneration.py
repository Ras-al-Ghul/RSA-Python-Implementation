@@ -0,0 +1,108 @@
#To generate random primes in the range CONST_MIN to CONST_MAX
#The generated primes are 8 digits in length here because max value of message string for 
#CONST_BYTE=4 is 1874160 
import random
CONST_MIN=21272296
CONST_MAX=23242658

def rand_prime():
     if CONST_MIN%2==0:
     	CONST_MINSS=CONST_MIN+1
     else:
	CONST_MINSS=CONST_MIN
     while True:
        p = random.randrange(CONST_MINSS, CONST_MAX,2)
	if ((p-1) % 6)!=0 and ((p+1)%6)!=0:
		continue
        if all(p % n != 0 for n in range(3, int(p**0.5)+1,2)):
            return p
	else:
		continue

p=rand_prime()
q=rand_prime()

#p to be greater than q

if p < q:
	p,q=q,p

print "\nThe primes are ",p," ",q,"\n"

#Calculate modulus and totient

def calculatetotient(a,b):
	n=a*b
	totient=(a-1)*(b-1)
	return n,totient

modulus,totient=calculatetotient(p,q)
print "The modulus and totient are ",modulus," ",totient,"\n"


CONST_MIN=65537
CONST_MAX=100000

def gcd(a, b):
        while b != 0:
            (a, b) = (b, a%b)
        return a

newkey=65537
while True:
	if gcd(totient,newkey)!=1:
		newkey=rand_prime
		continue
	else:
		break


print "The default public encryption key is 65537 (FOR FAST ENCRYPTION). \nDo you still want to change it?(Y/N)"
choice=raw_input()
#Also have to check that GCD of Totient and Encryption key is 1 else have to recalculate key
if choice == 'y' or choice == 'Y':
	while True:	
		print "Is this acceptable?(Y/N)"
		while True:
			newkey=rand_prime()
			if gcd(totient,newkey) != 1:
				continue
			else:
				break
		print newkey
		choice=raw_input()
		if choice == 'y' or choice == 'Y':
			break
		else:
			continue

ekey=newkey
print "\nThe public encryption key is (e,n) ",ekey,modulus,"\n"

#Calculate Decryption key

def calcdkey(x,y):
	temp=x
	oldolds=1
	olds=0
	oldoldt=0
	oldt=1
	while (y!=0):
		q,r=divmod(x,y)
		x=y
		y=r
		s=oldolds-(q*olds)
		t=oldoldt-(q*oldt)
		oldolds=olds
		oldoldt=oldt
		olds=s
		oldt=t
	return oldoldt+temp

dkey=calcdkey(totient,ekey)
print "The private decryption key is (d,n) ",dkey,modulus,"\n"
print "The private decryption key is (d%totient,n) ",dkey%totient,modulus,"\n"
print "The dkey can be d or d%totient but d%totient is faster because it might be smaller\n"
print "Paste the relevant data wherever necessary"

