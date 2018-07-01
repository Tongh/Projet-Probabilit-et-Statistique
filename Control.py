import matplotlib.pyplot as plt
from numpy import pi, exp, linspace


class Control:

    def __init__(self):
        self.verre = list()

    def add_verre(self, verre):
        self.verre.append(verre)

    def get_delta_data(self, string, arg=None):
        res = None
        if not arg:
            if string == "sphere":
                res = [it.sphere_delta for it in self.verre if it.sphere_delta]
            elif string == "cylindre":
                res = [it.cylindre_delta for it in self.verre if it.cylindre_delta]
            elif string == "axe":
                res = [it.axe_delta for it in self.verre if it.axe_delta]
            elif string == "addition":
                res = [it.addition_delta for it in self.verre if it.addition_delta]
            elif string == "epais.centre":
                res = [it.epais_centre_delta for it in self.verre if it.epais_centre_delta]
        else:
            para, valeur = arg.split(".")
            if string == "sphere":
                res = [it.sphere_delta for it in self.verre if it.sphere_delta and it.get(para).count(valeur)]
            elif string == "cylindre":
                res = [it.cylindre_delta for it in self.verre if it.cylindre_delta and it.get(para).count(valeur)]
            elif string == "axe":
                res = [it.axe_delta for it in self.verre if it.axe_delta and it.get(para).count(valeur)]
            elif string == "addition":
                res = [it.addition_delta for it in self.verre if it.addition_delta and it.get(para).count(valeur)]
            elif string == "epais.centre":
                res = [it.epais_centre_delta for it in self.verre if it.epais_centre_delta and it.get(para).count(valeur)]
        return res

    def get_etendue(self, string, arg=None):
        tmp = self.get_delta_data(string, arg)
        if not tmp:
            return "Pas de données"
        return max(tmp) - min(tmp)

    def get_median(self, string, arg=None):
        tmp = self.get_delta_data(string, arg)
        if not tmp:
            return "Pas de données"
        sorted(tmp)
        if len(tmp) % 2 == 1:
            i = len(tmp) // 2 + 1
            return tmp[i]
        else:
            i = len(tmp) // 2
            median = (tmp[i] + tmp[i+1]) / 2
            return median

    def get_esperance_delta_moyenne(self, string, arg=None):
        data = self.get_delta_data(string, arg)
        if not data:
            return "Pas de données"
        tmp = list(set(data))
        pob = [data.count(it)/len(data) for it in tmp]
        res = [tmp[it]*pob[it] for it in range(len(tmp))]
        return sum(res)

    def get_esperance_delta_variance(self, string, arg=None):
        data = self.get_delta_data(string, arg)
        if not data:
            return "Pas de données"
        tmp = list(set(data))
        pob = [data.count(it)/len(data) for it in tmp]
        moy = self.get_esperance_delta_moyenne(string)
        res = [(tmp[i]-moy)**2 * pob[i] for i in range(len(tmp))]
        return sum(res)

    def get_esperance_delta_ecart_type(self, string, arg=None):
        v = self.get_esperance_delta_variance(string, arg)
        return pow(v, 1.0/2) if v != "Pas de données" else "Pas de données"

    def plot_delta(self, string, arg=None):
        data = self.get_delta_data(string, arg)
        if not data:
            return "Pas de données"
        plt.figure()
        plt.title(string)
        plt.plot(data)
        plt.show()

    def get_intervalle_de_confiance(self, it, a, arg=None):
        data = self.get_delta_data(it, arg)
        if not data:
            return "Pas de données"
        z = 1.96 if a == 0.5 else 2.576
        sigma = self.get_esperance_delta_ecart_type(it, arg)
        mu = self.get_esperance_delta_moyenne(it, arg)
        n = len(data)
        min = mu - z * (sigma)
        max = mu + z * (sigma)
        return min, max

    def plot_delta_prob(self, string, arg=None):
        data = self.get_delta_data(string, arg)
        if not data:
            return "Pas de données"
        tmp = set(data)
        tmp = sorted(tmp)
        t = [data.count(it) for it in tmp]
        plt.figure()
        plt.title(string.capitalize())
        plt.plot(tmp, t)
        xlab = "Delta" + string.capitalize()
        plt.ylabel("Nombres")
        plt.xlabel(xlab)
        plt.show()

    def get_comparaison_moyenne(self, it, a, b):
        m1 = self.get_esperance_delta_moyenne(it, a)
        m2 = self.get_esperance_delta_moyenne(it, b)
        if m1 == "Pas de données" or m2 == "Pas de données":
            return m1
        return m1 - m2

    def get_comparaison_variance(self, it, a, b):
        sigma1 = self.get_esperance_delta_variance(it, a)
        sigma2 = self.get_esperance_delta_variance(it, b)
        if sigma1 == "Pas de données" or sigma2 == "Pas de données":
            return sigma1
        n1 = len(self.get_delta_data(it, a))
        n2 = len(self.get_delta_data(it, b))
        res = sigma1 / n1 + sigma2 / n2
        return pow(res, 1.0/2)

    def get_Z_(self, x=0):
        x = linspace(-4, 4, 1000)
        sigma = self.get_esperance_delta_ecart_type("sphere")
        mu = self.get_esperance_delta_moyenne("sphere")
        f = (1 / (sigma * pow(2*pi, 1.0/2))) * exp(-1/2*((x-mu)/sigma)**2)
        plt.figure()
        plt.title("Loi de normal")
        s = '$\mu=%f,\ \sigma=%s$' % (mu, sigma)
        plt.text(-0.2, 7, s)
        plt.xlabel(r"$\theta$")
        plt.plot(x, f)
        plt.xlim((-0.25, 0.25))
        plt.show()

    def inter_verifier(self, string, arg=None):
        data = self.get_delta_data(string, arg)
        if not data:
            print("Pas de Données")
            return "Pas de Données"
        al = [0.5, 0.1]
        for alpha in al:
            inter = self.get_intervalle_de_confiance(string, alpha, arg)
            print("[%f]" % alpha)
            num = 0
            for it in data:
                if it <= inter[1] and it >= inter[0]:
                    num += 1
            per = num / len(data)
            print("Poucentage : %f" % per, end=" \t")
            x = "V" if per > (1 - alpha) else "X"
            print(x)

    def get_hypothese(self, it, arg=None):
        data = self.get_delta_data(it, arg)
        return data.count(0)/len(data)


