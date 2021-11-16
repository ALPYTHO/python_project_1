import ssl
import httpx

URL = 'https://pax.ulaval.ca/squadro/api2/'


def lister_les_parties(iduls):
    rep = httpx.get(URL+'parties', params={'iduls': iduls})

    if rep.status_code == 200:
        return rep.json()

    if rep.status_code == 406:
        raise RuntimeError(rep.json()["message"])

def récupérer_une_partie(id_partie):

    rep = httpx.get(URL + 'partie', params={'id': id_partie})

    if rep.status_code == 200:

        rep = rep.json()

        print(rep)
        return(rep["id"], rep["prochain_joueur"], rep["état"], rep["gagnant"])

    if rep.status_code == 406:
        raise RuntimeError(rep.json()["message"])


def créer_une_partie(iduls):

    rep = httpx.post(URL+'partie', json={'iduls': iduls})

    if rep.status_code == 200:

        rep = rep.json()
        return(rep["id"], rep["prochain_joueur"], rep["état"], rep["gagnant"])




def jouer_le_coup(id_partie, idul, pion):

    rep = httpx.put(URL+'jouer', json= {"id": id_partie, "idul": idul, "pion": pion})

    if rep.status_code == 200:
    
        rep = rep.json()

        if rep["gagnant"] is not None:

            raise StopIteration(rep["gagnant"])

        return(rep["id"], rep["prochain_joueur"], rep["état"], rep["gagnant"])

    if rep.status_code == 406:
    
        raise RuntimeError(rep.json()["message"])
