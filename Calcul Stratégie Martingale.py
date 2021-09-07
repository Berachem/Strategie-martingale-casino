def martingale(**kwargs):
    """
    Fonction qui conseil pour la stratégie de la Martingale :
        PARAMETRE:
        - s_dep OU s_totale
        - marge (marge qu'on s'autorise à loose)
        RENVOIE :
        - S_dep : la somme de départ à déposer (Arguments à donner : marge et s_totale)
        - S_totale : la somme totale à avoir (Arguments à donner : marge et S_dep)

    """

    assert "marge" in kwargs.keys(), "Vous avez oubliez de mentionner la marge d'erreur à l'aide du 'range' !"
    if "s_dep" in kwargs.keys() and not ("s_totale" in kwargs.keys()):
        return "La somme totale à avoir est de : " + str( kwargs["s_dep"]* sum([2**i for i in range(kwargs["marge"])]) ) + " euros."
    elif "s_totale" in kwargs.keys() and not ("s_dep" in kwargs.keys()):
        return "La somme de départ à avoir est de : " + str( kwargs["s_totale"]/sum([2**i for i in range(kwargs["marge"])]) ) + " euros."
    else:
        return " [FAIL] : s_totale et s_dep ont été eux deux renseigné..."

print(martingale(s_totale=400,marge=10))
print(martingale(s_dep=0.1,marge=10))
