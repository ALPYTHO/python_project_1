# -*- coding: utf-8 -*-
"""Jeu Squadro

Ce programme permet de joueur au jeu Squadro.

Examples:
    `> python3 main.py --help`
        usage: main.py [-h] [-p] IDUL [IDUL ...]

        Squadro

        positional arguments:
        IDUL           IDUL du ou des joueur(s)

        optional arguments:
        -h, --help     show this help message and exit
        -p, --parties  Lister les 20 dernières parties

    `> python3 main.py jowic42`
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

        Au tour de jowick42 de jouer
        Choisissez le pion à déplacer: 3
"""
from squadro import traiter_la_ligne_de_commande, afficher_le_plateau_de_jeu, formatter_les_parties
from api import lister_les_parties, récupérer_une_partie, créer_une_partie, jouer_un_coup

# TODO: Vous ne devriez pas avoir de code ici sauf des déclarations de fonction,
#       retirer le TODO une fois complété.

if __name__ == "__main__":
    # TODO: Implémentez votre boucle de jeu ici à CE niveau D'INDENTATION,
    #       retirer le TODO une fois complété.
    pass

# TODO: Vous NE devriez PAS avoir de code à CE niveau d'INDENTATION.
# TODO: Supprimer le code et les commentaires superflux.
# TODO: Supprimer les TODO une fois complété.
