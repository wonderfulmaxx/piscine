from cryptography.fernet import Fernet
import base64
import hashlib
import sys



def parsing(nb_args):
	silent = False
	reverse = False
	passwd = None
	counter = 1
	while counter < nb_args:
		if nb_args < 2:
			print("Invalid args, type stockolm -h to get help")
			sys.exit(0)
		if sys.argv[counter] == "-h" or sys.argv[counter] == "-help":
			print("\n\n-h for display the help\n\
-v to show the version of the program\n\
-r followed by the [passwd] entered as an argument to reverse the infection\n\
-s for silent mode\n\n\
By default, to use the program, enter \"stockolm [16 characters long passwd]\" to encrypt the infection file.\n\n" )
			sys.exit(1)
		if sys.argv[counter] == "-s" or sys.argv[counter] == "-silent":
			silent = True
		if sys.argv[counter] == "-v" or sys.argv[counter] == "-version":
			print("version: 1.0.0")
			sys.exit(0)
		if sys.argv[counter] == "-r" or sys.argv[counter] == "-reverse":
			reverse = True
		if not (sys.argv[counter].startswith("-")):
			if passwd is None:
				passwd = sys.argv[counter]
				if len(passwd) < 16:
					print("Passwd must be at least 16 characters long")
					sys.exit(1)
			else:
				print("Bad arguments")
				sys.exit(1)
		counter += 1
	if passwd == None:
		print("Enter a passwd")
		sys.exit(1)
	return(silent,reverse,passwd)
		
		






nb_args = len(sys.argv)
silent,reverse,passwd=parsing(nb_args)


if not reverse:
	# Générer une clé à partir du mot de passe
	cle = base64.urlsafe_b64encode(hashlib.sha256(passwd.encode()).digest())
	# Créer un objet Fernet avec la clé
	fernet = Fernet(cle)



	# Encrypter les données
	donnees_a_chiffrer = "Ma mami fait des films pour adulte"
	donnees_chiffrees = fernet.encrypt(donnees_a_chiffrer.encode())
	# Afficher les données chiffrées
	print("Données chiffrées :", donnees_chiffrees)


if reverse:

	donnees_chiffrees = b'gAAAAABkZjDnodKwPXt5tZxEBI8DC8CycEzX_hU8WT4vxo7bVJcQyWHyT3arbBQ08o9PSNt-mc5qgtjiQXBBzX7roCzC45YTkNDcjffYoLhJXPPAPhfyPPwyhmZZaSwl1PUPDpxbCw-K'

	cle2 = base64.urlsafe_b64encode(hashlib.sha256(passwd.encode()).digest())
	fernet2 = Fernet(cle2)
	
	try:
		donnees_dechiffrer = fernet2.decrypt(donnees_chiffrees)
		print("donnees dechifrees :",donnees_dechiffrer.decode())
	except:
		print("Not this time, looser")
		sys.exit(1)