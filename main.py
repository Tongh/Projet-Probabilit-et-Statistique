from Control import Control
from Verre import Verre


def main():
    control = Control()
    with open('data.txt') as dataFile:
        for it in range(1007):
            ligne = dataFile.readline().split("\t")
            if it == 0:
                continue
            verre = Verre(ligne)
            control.add_verre(verre)
    name = ["sphere", "cylindre", "axe", "addition", "epais.centre"]
    for it in name:
        print(" ==> [%s]" % it)
        print("\tEtendue    :", control.get_etendue(it))
        print("\tMedian     :", control.get_median(it))
        print()
        print("\tMoyenne    :", control.get_esperance_delta_moyenne(it))
        print()
        print("\tVariance   :", control.get_esperance_delta_variance(it))
        print()
        print("\tEcart type :", control.get_esperance_delta_ecart_type(it))
        print("\tHypothèse 0:", control.get_hypothese(it))
        print()
        inter = control.get_intervalle_de_confiance(it, 0.5)
        print("\t [alpha = 0.5]")
        print("\t Intervalle de confiance: [%f, %f]" % (inter[0], inter[1]))
        inter = control.get_intervalle_de_confiance(it, 0.1)
        print("\t [alpha = 0.1]")
        print("\t Intervalle de confiance: [%f, %f]" % (inter[0], inter[1]))
        #control.inter_verifier(it)
        print()
        print(" ==> [OXL]: ")
        print(" \t==> Moyenne : ", control.get_esperance_delta_moyenne(it, "type.OXL"))
        print(" \t==> Variance: ", control.get_esperance_delta_variance(it, "type.OXL"))
        print(" ==> [ORG]: ")
        print(" \t==> Moyenne : ", control.get_esperance_delta_moyenne(it, "type.ORG"))
        print(" \t==> Variance: ", control.get_esperance_delta_variance(it, "type.ORG"))
        print()
        print(" \t==> E(T)     =", control.get_comparaison_moyenne(it, "type.ORG", "type.OXL"))
        print(" \t==> sigma(T) =", control.get_comparaison_variance(it, "type.ORG", "type.OXL"))
        print()
        print(" ==> [T5]: ")
        print(" \t==> Moyenne : ", control.get_esperance_delta_moyenne(it, "matiere.T5"))
        print(" \t==> Variance: ", control.get_esperance_delta_variance(it, "matiere.T5"))
        print(" ==> [BL]: ")
        print(" \t==> Moyenne : ", control.get_esperance_delta_moyenne(it, "matiere.BL"))
        print(" \t==> Variance: ", control.get_esperance_delta_variance(it, "matiere.BL"))
        print()
        print(" \t==> E(T)     =", control.get_comparaison_moyenne(it, "matiere.T5", "matiere.BL"))
        print(" \t==> sigma(T) =", control.get_comparaison_variance(it, "matiere.T5", "matiere.BL"))
        print("*"*40)
        #control.plot_delta_prob(it)
    #control.get_Z_()


if __name__ == "__main__":
    main()
