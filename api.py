# -*- coding: utf-8 -*-
"""Module d'API du jeu Squadro

Ce module permet d'interagir avec le serveur
afin de pouvoir jouer contre un adversaire robotisé.

Attributes:
    URL (str): Constante représentant le début de l'url du serveur de jeu.

Functions:
    * récupérer_parties - Récupérer la liste des parties reçus du serveur.
    * retrouver_partie - Retrouver l'état d'une partie spécifique.
    * commencer_partie - Créer une nouvelle partie et retourne l'état de cette dernière.
    * executer_coup - Exécute un coup et retourne le nouvel état de jeu.
"""
import httpx

URL = "https://pax.ulaval.ca/"


def lister_les_parties(iduls):
    """Récupérer les identifiants de vos parties les plus récentes.

    Récupère les parties en effectuant une requête à l'URL cible
    squadro/api2/parties/

    Cette requête de type GET s'attend en entrée à recevoir un seul paramètre,
    sous forme de liste, nommé `iduls` qui identifie le ou les idul(s) des joueurs.
    En cas de succès (code `200`), elle retourne en JSON
    un dictionnaire contenant la clé suivante:

        parties: une liste des (max) 20 parties les plus récentes de l'usager;

    où chaque partie dans la liste est elle-même un dictionnaire
    contenant les clés suivantes:

        id: l'identifiant de la partie;
        date: la date de création de la partie;
        joueurs: la liste ordonnée des joueurs;
        gagnant: le nom du gagnant si existant (défaut: None).

    En cas d'erreur, si le code de votre réponse est 406,
    elle retourne en JSON un dictionnaire contenant la clé suivante:

        message: un message en cas d'erreur;

    Args:
        iduls (list): Liste des identifiant des joueurs.

    Returns:
        list: Liste des parties reçues du serveur,
             après avoir décodé le JSON de sa réponse.

    Raises:
        RuntimeError: Erreur levée lorsqu'il y a présence d'un message
            dans la réponse du serveur.

    Examples:
        >>> iduls = ["josmi42"]
        >>> parties = lister_les_parties(iduls)
        >>> print(parties)
        [{ 'id': 'c1493454-1f7f-446f-9c61-bd7a9d66c92d', 'date': '2021-01-23 19:23:59', ... ]
    """
    # TODO: Complétez cette fonction, retirer le TODO une fois complété.
    pass


def récupérer_une_partie(id_partie):
    """Retrouver une partie depuis son identifiant.

    Récupère une partie depuis son identifiant en effectuant une requête à l'URL cible
    squadro/api2/partie/

    Cette requête de type GET s'attend en entrée à recevoir
    un seul paramètre nommé `id` qui identifie la partie.
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
        id_partie (str): Identifiant de la partie à récupérer.

    Returns:
        tuple: Tuple constitué de l'identifiant de la partie en cours,
            du prochain joueur à jouer et de l'état courant du jeu,
            après avoir décodé le JSON de sa réponse.

    Raises:
        RuntimeError: Erreur levée lorsque le serveur retourne un code 406.

    Examples:
        >>> id_partie = 'c1493454-1f7f-446f-9c61-bd7a9d66c92d'
        >>> partie = retrouver_partie(id_partie)
        >>> print(partie)
        ('c1493454-1f7f-446f-9c61-bd7a9d66c92d', 'keree13, [{'nom': ..., 'pions': ...}, ..])
    """
    # TODO: Complétez cette fonction, retirer le TODO une fois complété.
    pass


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
