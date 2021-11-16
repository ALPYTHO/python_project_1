# -*- coding: utf-8 -*-

import httpx

URL = 'https://pax.ulaval.ca/squadro/api2/'


def lister_les_parties(iduls):
        
    rep = httpx.get(URL+'parties', params={'iduls': iduls})

    if rep.status_code == 200:
        return(rep.json())

    elif rep.status_code == 406:
        raise RuntimeError(rep.json())

    else:
        raise RuntimeError(rep.json())
    


def récupérer_une_partie(id_partie):

    rep = httpx.get(URL + 'partie', params={'id': id_partie})

    if rep.status_code == 200:

        rep = rep.json()
        return(rep["id"], rep["prochain_joueur"], rep["état"], rep["gagnant"])

    if rep.status_code == 406:
        raise RuntimeError("Erreur levée lorsque le serveur retourne un code 406.")
    else:
        raise RuntimeError(rep.json())


def créer_une_partie(iduls):
    """Débuter une nouvelle partie.

    Débute une partie en effectuant une requête à l'URL cible
    squadro/api2/partie/

    Cette requête est de type POST, contrairement à lister_parties,
    car elle modifie l'état interne du serveur en créant une nouvelle partie.
    
    Elle s'attend en entrée à recevoir une liste composé de 1 ou de 2 iduls.
    En cas de succès (code `200`), elle retourne en JSON 
    un dictionnaire contenant les clés suivantes:

        id: identifiant de la partie en cours;
        prochain_joueur: identifiant du prochain joueur à jouer;
        état: l'état actuel du jeu;
        gagnant: le nom du joueur gagnant, None s'il n'y a pas encore de gagnant.

    En cas d'erreur (code `406`), elle retourne en JSON
    un dictionnaire contenant la clé suivante:

        message: un message en cas d'erreur.

    Args:
        iduls (list): Liste de string représentant le ou les identifiant(s) du ou des joueur(s).

    Returns:
        tuple: Tuple constitué de l'identifiant de la partie en cours,
            du prochain joueur à jouer et de l'état courant du jeu,
            après avoir décodé le JSON de sa réponse.

    Raises:
        RuntimeError: Erreur levée lorsque le serveur retourne un code 406.

    Examples:
        >>> iduls = ['jowic42', 'keree13']
        >>> partie = commencer_partie(iduls)
        >>> print(partie)
        ('c1493454-1f7f-446f-9c61-bd7a9d66c92d', 'keree13, [{'nom': ..., 'pions': ...}, ..])
    """
    # TODO: Complétez cette fonction, retirer le TODO une fois complété.
    pass


def jouer_le_coup(id_partie, idul, pion):
    """Jouer votre coup dans une partie en cours

    Joue un coup en effectuant une requête à l'URL cible
    squadro/api2/jouer/

    Cette requête est de type PUT, contrairement à lister_parties,
    car elle modifie l'état interne du serveur en modifiant une partie existante.

    Elle s'attend à recevoir en entrée trois (3) paramètres associés au PUT:

        id: l'identifiant de la partie;
        idul: IDUL jouant un coup;
        pion: Numéro du pion à déplacer.

    En cas de succès (code 200), elle retourne en JSON
    un dictionnaire pouvant contenir les clés suivantes:

        id: identifiant de la partie en cours;
        prochain_joueur: identifiant du prochain joueur à jouer;
        état: l'état actuel du jeu;
        gagnant: le nom du joueur gagnant, None s'il n'y a pas encore de gagnant.

    En cas d'erreur (code 406), elle retourne en JSON
    un dictionnaire contenant la clé suivante:

        message: un message en cas d'erreur.

    Args:
        id_partie (str): identifiant de la partie;
        idul (str): IDUL jouant un coup;
        pion (int): Numéro du pion à déplacer.

    Returns:
        tuple: Tuple constitué de l'identifiant de la partie en cours,
            du prochain joueur à jouer et de l'état courant du jeu,
            après avoir décodé le JSON de sa réponse.

    Raises:
        RuntimeError: Erreur levée lorsque le serveur retourne un code 406.
        StopIteration: Erreur levée lorsqu'il y a un gagnant dans la réponse du serveur.

    Examples:
        >>> id_partie = 'c1493454-1f7f-446f-9c61-bd7a9d66c92d'
        >>> idul = 'jowic42'
        >>> pion = 3
        >>> partie = jouer_coup(id_partie, idul, pion)
        >>> print(partie)
        ('c1493454-1f7f-446f-9c61-bd7a9d66c92d', 'keree13, [{'nom': ..., 'pions': ...}, ..])
    """
    # TODO: Complétez cette fonction, retirer le TODO une fois complété.
    pass

# TODO: Ne pas mettre de code en dehors des fonctions.
# TODO: Supprimer le code et les commentaires superflux.
# TODO: Supprimer les TODO une fois complété.
