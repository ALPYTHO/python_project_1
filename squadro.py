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
  board = """
       . | . : | : : | : : | : . | .
         |   . | .   |   . | .   |
  ...    |     |     |     |     |      .
1 ───────┼─────┼─────┼─────┼─────┼───────
  ...    |     |     |     |     |      .
  .      |     |     |     |     |    ...
2 ───────┼─────┼─────|─────┼─────┼───────
  .      |     |     |     |     |    ...
  ..     |     |     |     |     |     ..
3 ───────┼─────┼─────┼─────┼─────┼───────
  ..     |     |     |     |     |     ..
  .      |     |     |     |     |    ...
4 ───────┼─────┼─────┼─────┼─────┼───────
  .      |     |     |     |     |    ...
  ...    |     |     |     |     |      .
5 ───────┼─────┼─────┼─────┼─────┼───────
  ...    |     |     |     |     |      .
       . | .   |     |     |   . | .
       : | : . | . : | : . | . : | :"""
                

  #pour réduire le nombre de code on remplace ici


  current_board = board

  #pour réutiliser du code

  def change_char_verti(current_board, c, d, b):

      current_board = current_board[:b + d] + "█" + current_board[b + d + 1:]
      current_board = current_board[:b + c] + "●" + current_board[b + c + 1:]

      return current_board

  def change_char_hory(current_board, character, b):  
      current_board = current_board[:b] + character + current_board[b + 4:]

      return current_board

  for i in range(5):

      character_for_0_6 = {"vertical": {"0": [38, 35, 0], "6": [661, 0, 42], "12": [38, 0, 35]}, "horyzontal": {"0": 5, "6": 36, "12": 5}, "bignum": { "8": 4, "9": 3, "10": 2, "12": 12}}
      
      #Joueur vertical pour les cas sauf 0,6,12
      joueur2 = état[1]["pions"][i]
      rectangle, rond = 42, 0

      if joueur2 > 6 and joueur2 != 12:

          joueur2 = character_for_0_6["bignum"][str(joueur2)]
          rectangle, rond = rond, rectangle

      
      if (joueur2 % 6) != 0:

          b = ((joueur2 - 1) * 42 * 3) + 115 + (i * 6) + 9  

          current_board = change_char_verti(current_board, rectangle, rond, b)

      #Joueur horyzontal pour les cas sauf 0,6,12
          
      joueur1 = état[0]["pions"][i]
      character = "□□ ○"

      if joueur1 > 6:

          joueur1 = character_for_0_6["bignum"][str(joueur1)]

          character = "○ □□"


      if (joueur1 % 6) != 0:

          b = (i * 42 * 3) + 114 + 9 + (6 * (joueur1 - 1))

          current_board = change_char_hory(current_board, character, b)

      #Cas 0,6,12 vertical
      if (joueur2 % 6) == 0:

        b = (character_for_0_6["vertical"][str(joueur2)][0] + 9 + (i * 6))
        
        c = character_for_0_6["vertical"][str(joueur2)][1]
        d = character_for_0_6["vertical"][str(joueur2)][2]

        current_board = change_char_verti(current_board, c, d, b)

      #Cas 0,6,12 horyzontal
      if (joueur1 % 6) == 0:

        b = (i * 42 * 3) + 114 + character_for_0_6["horyzontal"][str(joueur1)]

        current_board = change_char_hory(current_board, character, b)

  print(f"""Légende:\n  □ = {état[0]["nom"]}\n  ■ = {état[1]["nom"]}\n""", current_board)
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
