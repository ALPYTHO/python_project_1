# -*- coding: utf-8 -*-
"""Module d'interface utilisateur de Squadro

Ce module permet d'interagir avec le joueur
en offrant un interface en ligne de commande.

Functions:
    * analyser_commande - Génère un analyseur de ligne de commande.
    * afficher_damier_ascii - Affiche la représentation graphique
                              du damier en ligne de commande.
    * afficher_parties - Affiche la liste des 20 dernières parties.
"""
from argparse import ArgumentParser


def traiter_la_ligne_de_commande():

    
    """Génère un évaluateur de ligne de commande

    En utilisant le module argparse, génère un évaluateur de ligne de commande.

    L'analyseur offre (1) argument positionnel:
        IDUL: IDUL du ou des joueurs.

    Ainsi que les (2) arguments optionnel:
        help: show this help message and exit
        parties: Lister les 20 dernières parties.

    Returns:
        Namespace: Retourne un objet de type Namespace possédant
            les clef «IDUL» et «parties».
    """
    # TODO: Insérer ici les bons appels à la méthode add_argument,
    #       Modifier ArgumentParser pour produire le résultat attendu,
    #       retirer le TODO une fois complété.
    parser = ArgumentParser()

    return parser.parse_args()


def afficher_le_plateau_de_jeu(état):
    """Afficher le plateau

    Ne faites preuve d'aucune originalité dans votre «art ascii»,
    car votre fonction sera testée par un programme et celui-ci est
    de nature intolérante (votre affichage doit être identique à
    celui illustré). Notez aussi que votre fonction sera testée
    avec plusieurs états de jeu différents.

    Args:
        état (dict): Dictionnaire représentant l'état du jeu.

    Examples:
        >>> état = [
                {
                    "nom": "jowic42",
                    "pions": [0, 2, 6, 9, 12]
                },
                {
                    "nom": "robot",
                    "pions": [0, 9, 2, 6, 12]
                }
            ]
        >>> afficher_plateau_ascii(état)
            Légende:
              □ = jowic42
              ■ = robot

                   . | . : | : : | : : | : . | .     
                     █   . | .   |   . | .   ●       
              ...    ●     |     |     |     █      .
            1 ──□□ ○─┼─────┼─────┼─────┼─────┼───────
              ...    |     |     |     |     |      .
              .      |     |     |     |     |    ...
            2 ───────┼────□□ ○───█─────┼─────┼───────
              .      |     |     ●     |     |    ...
              ..     |     ●     |     |     |     ..
            3 ───────┼─────█─────┼─────┼─────┼─○ □□──
              ..     |     |     |     |     |     ..
              .      |     |     |     |     |    ...
            4 ───────┼─────┼───○ □□────┼─────┼───────
              .      |     |     |     |     |    ...
              ...    |     |     |     |     |      .
            5 ──○ □□─┼─────┼─────┼─────┼─────┼───────
              ...    |     |     |     ●     |      .
                   . | .   |     |     █   . | .
                   : | : . | . : | : . | . : | :
    """
    # TODO: Complétez cette fonction, retirer le TODO une fois complété.
    pass


def formatter_les_parties(liste):
    
    for parties in range(len(liste)):

        print(f'{parties} : {liste[parties]["date"]}, {liste[parties]["joueurs"][0]} vs {liste[parties]["joueurs"][1]}, gagnant: {liste[parties]["gagnant"]}')
    """Formatter les parties

    Ne faites preuve d'aucune originalité dans votre formattage
    car votre fonction sera testée par un programme et celui-ci est
    de nature intolérante (votre formattage doit être identique à
    celui illustré). Notez aussi que votre fonction sera testée
    avec plusieurs listes de parties différentes.

    Args:
        parties (list): Liste des parties d'un joueur.

    Returns:
        str: Chaîne de caractière représentant votre liste de parties

    Examples:
        >>> parties = [
                {
                    "id": "5559cafd-6966-4465-af6f-67a784016b41",
                    "date": "2021-01-24 11:58:20",
                    "joueurs": ["jowic42", "robot-2"],
                    "gagnant": None
                },
                ...
                {
                    "id": "80a0a0d2-059d-4539-9d53-78b3f6045943",
                    "date": "2021-01-23 14:23:59",
                    "joueurs": ["jowic42", "robot-1"],
                    "gagnant": "jowic42"
                }
            ]
        >>> print(formatter_parties(parties))
            1 : 2021-01-31 15:05:23, jowic42 vs robot-1
            ...
            20: 2021-02-22 17:16:59, jowic42 vs robot-1, gagnant: jowic42
    """
    # TODO: Complétez cette fonction, retirer le TODO une fois complété.
    pass

# TODO: Vous pouvez créer des fonctions additionnels si vous en sentez le besoin,
#       Il ne devrait pas y avoir autre chose que des définitions de fonctions.
#       Retirer le TODO une fois complété.
# TODO: Supprimer le code et les commentaires superflux.
# TODO: Supprimer les TODOs une fois complété.
