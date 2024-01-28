def martingale(s_dep=None, s_totale=None, marge=None):
    """
    Fonction qui conseille pour la stratégie de la Martingale :
        PARAMETRE:
        - s_dep OU s_totale
        - marge (marge qu'on s'autorise à perdre)
        RENVOIE :
        - S_dep : la somme de départ à déposer (Arguments à donner : marge et s_totale)
        - S_totale : la somme totale à avoir (Arguments à donner : marge et S_dep)
    """

    # Vérification des arguments
    assert marge is not None, "Vous avez oublié de mentionner la marge d'erreur !"
    assert s_dep is not None or s_totale is not None, "Vous devez spécifier soit 's_dep', soit 's_totale'."

    # Calcul de la somme totale ou de départ en fonction des arguments
    if s_dep is not None and s_totale is None:
        return f"La somme totale à avoir est de : {s_dep * sum([2**i for i in range(marge)])} euros."
    elif s_totale is not None and s_dep is None:
        return f"La somme de départ à avoir est de : {s_totale / sum([2**i for i in range(marge)])} euros."
    else:
        return "[FAIL] : s_totale et s_dep ont été tous deux renseignés..."

#EXEMPLES
print(martingale(s_totale=400, marge=10))
print(martingale(s_dep=0.1, marge=10))
