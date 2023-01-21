__all__ = ['help']


def help():
    print(
        """
        ==================================================================
        *     SCRIPT DE COLLECTE DE DONNEES ET ENVOIE DES PASSKIT F1     *
        ==================================================================

        Ce Script permet de lire les info client d'un fichier excel "xlsx"
        (prenom, nom, email, date de naissance, n°de tel, carte vip, NL, 
        numero de catre, numero de pdv, nom du pdv,code pays) et d'envoyer
        un passkit pour chaque entrée, et retourne un nouveau fichier csv
        avec le statut de chaque envoie (success ou echec) 

        USAGE:

        1. -h/--help
        permet d'afficher l'aide

        2. 
                                                 *
                                                * *
                                               * | *
                                              *  |  *       
                                             *   o   *      
                                            ***********  
    - le fichier xlsx doit contenir les carte dans une colonne nommée : "numéro"  
    - si les identifiants ( usr, pwd ) ne sont pas valides , les données de la carte en question ne seront pas collectées
        """
    )