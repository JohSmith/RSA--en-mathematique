#!/usr/bin/env python
# -*- coding: utf-8 -*-   

#((77, 37), (77, 13))
     
def bezout(a, b):
    ''' Calcule (u, v, p) tels que a*u + b*v = p et p = pgcd(a, b) '''
    if a == 0 and b == 0: return (0, 0, 0)
    if b == 0: return (a/abs(a), 0, abs(a))
    (u, v, p) = bezout(b, a%b)
    return (v, (u - v*(a/b)), p)
 
def inv_modulo(x, m):
    ''' Calcule y dans [[0, m-1]] tel que x*y % abs(m) = 1 '''
    (u, _, p) = bezout(x, m)
    if p == 1: return u%abs(m)
    else: raise Exception("%s et %s ne sont pas premiers entre eux" % (x, m))
    
    
def creationClee():
	entierAlice1 = int ( raw_input("Entrer un nombre premier: ") )
	entierAlice2 = int ( raw_input("Entrer un autre nombre premier: ") )
	
	moduleDeChiffrement = entierAlice1 * entierAlice2
	indicatriceEuler = (entierAlice1 - 1) * (entierAlice2 - 1)
	
	exposantChiffrement = int ( raw_input("Entrer nombre première et inférieur a {}: ".format(indicatriceEuler)) )
	
	d = inv_modulo(exposantChiffrement, indicatriceEuler)

	print("Clée publique({},{}) et clée privée({},{})".format(moduleDeChiffrement, exposantChiffrement, moduleDeChiffrement, d) )
	
	return ( ( moduleDeChiffrement, exposantChiffrement ), ( moduleDeChiffrement, d ) )
	
def cryptage( donnee, cleePublique ):
	return donnee ** cleePublique[1] % cleePublique[0]
	
def decryptage( donnee, cleePrivee ):
	return donnee ** cleePrivee[1] % cleePrivee[0]


def main():
	clee = ( 77,37 )
	while 1:
		msg = raw_input("Entrer donne a crypter avec la clee {}".format( clee ) )
		msgCompose = ""
		msgEnInt, msgCryInt, msgDecry = [],[],[]

		for i in msg:
			msgCompose += str( ord( i ) )
		
		for i in range( len(msgCompose)/4 ):
			msgEnInt.append( int( msgCompose[i * 4:( i+1 ) * 4] ) )
		finDeChaine = msgCompose[(i+1)*4:]
		if finDeChaine != "": msgEnInt.append(int( msgCompose[(i+1)*4:] ) )

		for i in msgEnInt:
			msgCryInt.append( cryptage( i, clee) )

		for i in msgCryInt:
			msgDecry.append( decryptage( i, (77, 13) ) )
		print msg, msgCompose, msgEnInt, msgCryInt, msgDecry
	return 0

if __name__ == '__main__':
	main()
