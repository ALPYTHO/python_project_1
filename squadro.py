import argparse

def traiter_la_ligne_de_commande():

    parser = argparse.ArgumentParser(description='Squadro')

    parser.add_argument('IDUL', nargs='+', metavar='IDUL', help='IDUL du ou des joueur(s)')  
    parser.add_argument('-p', '--parties', help='Lister les 20 dernières parties', action='store_true')
    
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
                
  current_board = board

  # remplacement des 2 colones lors du changement de pions verticaux c et d utilisé pour inverser
  def change_char_verti(current_board, c, d, b):

      current_board = current_board[:b + d] + "█" + current_board[b + d + 1:]
      current_board = current_board[:b + c] + "●" + current_board[b + c + 1:]

      return current_board

  # remplacer les pions horyzontaux le caractère est déjà inverser si le pion > 6
  def change_char_hory(current_board, character, b):
      current_board = current_board[:b] + character + current_board[b + 4:]

      return current_board

  for i in range(5):

    # dictionaire utilisé pour les valeurs qui ne marche pas avec la logique utilisé plus bas afin de réduire le nombre de for
    # vertical:position du caractère rectangulaire à remplacer, c, et d (addition nécessaire pour le point incluant s'il y a inversion ou pas)
    # bignum: chiffre qui causait des problèmes dans la logique plus bas, valeur de colonne 
      character_for_0_6 = {"vertical": {"0": [38, 35, 0], "6": [661, 0, 42], "12": [38, 0, 35]}, "horyzontal": {"0": 5, "6": 36, "12": 5}, "bignum": { "8": 4, "9": 3, "10": 2, "12": 12}}
      
      # Joueur vertical pour les cas sauf 0,6,12

      joueur2 = état[1]["pions"][i]
      rectangle, rond = 42, 0

      # Inversion des pions et cas problèmes
      if joueur2 > 6:

          joueur2 = character_for_0_6["bignum"][str(joueur2)]
          rectangle, rond = rond, rectangle

      #Logique régulière
      if (joueur2 % 6) != 0:

          b = ((joueur2 - 1) * 126) + 124 + (i * 6)  

          current_board = change_char_verti(current_board, rectangle, rond, b)

      #Joueur horyzontal pour les cas sauf 0,6,12
          
      joueur1 = état[0]["pions"][i]
      character = "□□ ○"

      # Cas problèmes et inversion
      if joueur1 > 6:

          joueur1 = character_for_0_6["bignum"][str(joueur1)]

          character = "○ □□"

      # logique normale horyzontale
      if (joueur1 % 6) != 0:

          b = (i * 126) + 123 + (6 * (joueur1 - 1))

          current_board = change_char_hory(current_board, character, b)

      # Cas 0,6,12 vertical
      if (joueur2 % 6) == 0:

        b = (character_for_0_6["vertical"][str(joueur2)][0] + 9 + (i * 6))
        
        current_board = change_char_verti(current_board, character_for_0_6["vertical"][str(joueur2)][1], character_for_0_6["vertical"][str(joueur2)][2], b)

      # Cas 0,6,12 horyzontal
      if (joueur1 % 6) == 0:

        b = (i * 126) + 114 + character_for_0_6["horyzontal"][str(joueur1)]

        current_board = change_char_hory(current_board, character, b)

  # Affichage complet en remplaçant les noms des joueurs
  print(f"""Légende:\n  □ = {état[0]["nom"]}\n  ■ = {état[1]["nom"]}\n""", current_board)
  pass


def formatter_les_parties(liste):
    
    for parties in range(len(liste)):

        print(f'{parties} : {liste[parties]["date"]}, {liste[parties]["joueurs"][0]} vs {liste[parties]["joueurs"][1]}, gagnant: {liste[parties]["gagnant"]}')
    pass
