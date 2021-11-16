'''API'''
import httpx

URL = 'https://pax.ulaval.ca/squadro/api2/'


def lister_les_parties(iduls):
    '''liste les dernières parties'''
    rep = httpx.get(URL+'parties', params={'iduls': iduls})

    if rep.status_code == 200:
        return rep.json()

    raise RuntimeError(rep.json()["message"])

def récupérer_une_partie(id_partie):
    '''récupère une partie'''
    rep = httpx.get(URL + 'partie', params={'id': id_partie})

    if rep.status_code == 200:

        rep = rep.json()

        return(rep["id"], rep["prochain_joueur"], rep["état"], rep["gagnant"])

    raise RuntimeError(rep.json()["message"])


def créer_une_partie(iduls):
    '''crer une partie'''
    rep = httpx.post(URL+'partie', json={'iduls': iduls})

    if rep.status_code == 200:

        rep = rep.json()
        return(rep["id"], rep["prochain_joueur"], rep["état"], rep["gagnant"])

    raise RuntimeError(rep.json()["message"])




def jouer_un_coup(id_partie, idul, pion):
    '''joue un coup'''
    rep = httpx.put(URL+'jouer', json= {"id": id_partie, "idul": idul, "pion": pion})

    if rep.status_code == 200:
        rep = rep.json()

        if rep["gagnant"] is not None:

            raise StopIteration(rep["gagnant"])

        return(rep["id"], rep["prochain_joueur"], rep["état"], rep["gagnant"])

    else:
        raise RuntimeError(rep.json()["message"])
