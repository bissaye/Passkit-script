# Programme de Collecte de Données et envoie de PASSKIT F1

**Ce Script permet de lire les info client d'un fichier excel "xlsx"
(prenom, nom, email, date de naissance, n°de tel, carte vip, NL, 
numero de catre, numero de pdv, nom du pdv,code pays) et d'envoyer
un passkit pour chaque entrée, et retourne un nouveau fichier csv
avec le statut de chaque envoie (success ou echec)**

##INSTALLATION
1. cloner le repos
2. installer les paquets avec la commande:
   1. `python -m pip install -r requirements.txt`

## USAGE:
**1.` -h/--help`** <br>
permet d'afficher l'aide
<br>
<br>
**2.` -p/--path`** <br>
permet de spécifier le chemin vers le fichier excel à utiliser
<br>
<br>
**3.` -n/--name`** <br>
permet de spécifier le nom du fichier excel en sortie <br>
> NB: si aucun nom de fichier n'est spécifié, le nom par defaut sera: result.xlsx
> 
<br>
<br>

