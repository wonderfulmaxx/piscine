from cryptography.fernet import Fernet
import base64
import hashlib
import sys



def parsing(nb_args):
	silent = False
	reverse = False
	passwd = None
	counter = 1
	while counter < nb_args - 1:
		if nb_args < 2:
			print("Invalid args, type stockolm -h to get help")
			sys.exit(0)
		if sys.argv[counter] is "-h" or "-help":
			print("\n\n-h for display the help\n\
			-v to show the version of the program\n\
			-r followed by the [passwd] entered as an argument to reverse the infection\n\
			-s for silent mode\n\n\
			By default, to use the program, enter \"stockolm [16 characters long passwd]\" to encrypt the infection file.\n" )
			sys.exit(1)
		if sys.arg[counter] is "-s" or "-silent":
			silent = True
		if sys.argv[counter] is "-v" or "-version":
			print("version: 1.0.0")
			sys.exit(0)
		if sys.argv[counter] is "-r" or "-reverse":
			reverse = True
		if not sys.argv[counter].startwith("-"):
			if passwd is None:
				passwd = sys.argv[counter]
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




# Définir le mot de passe
mot_de_passe = b"MonMotDePasseSecret"





# Générer une clé à partir du mot de passe
cle = base64.urlsafe_b64encode(hashlib.sha256(mot_de_passe).digest())

# Créer un objet Fernet avec la clé
fernet = Fernet(cle)

# Encrypter les données
donnees_a_chiffrer = "Les données à chiffrer"
donnees_chiffrees = fernet.encrypt(donnees_a_chiffrer.encode())

# Afficher les données chiffrées
print("Données chiffrées :", donnees_chiffrees)






good_passwd = b"MonMotDePasseSecret"

cle2 = base64.urlsafe_b64encode(hashlib.sha256(good_passwd).digest())

fernet2 = Fernet(cle2)
donnees_dechiffrer = fernet2.decrypt(donnees_chiffrees)

print("donnees dechifrees :",donnees_dechiffrer.decode())