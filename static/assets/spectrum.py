import matplotlib.pyplot as plt
import numpy as np
T = np.arange(0,10,0.01)
Sds = float(input("SDS değerini gir:"))
Sd1 = float(input("SD1 değerini gir:"))
T_B = Sd1 / Sds

T_A = 0.2 * T_B
T_L = 6

spectrum = list()
period = list()

for i in T:
    if 0 <= i <= T_A:
        Sae = (0.4 + 0.6 * i / T_A)* Sds
        spectrum.append(Sae)
        period.append(i)

    elif T_A <= i <= T_B:
        Sae = Sds
        spectrum.append(Sae)
        period.append(i)

    elif T_B <= i <= T_L:
        Sae = Sd1 / i
        spectrum.append(Sae)
        period.append(i)

    else:
        Sae = Sd1 * T_L / (i ** 2)
        spectrum.append(Sae)
        period.append(i)

plt.plot(period, spectrum, "blue")
plt.xlabel("Periyot")
plt.ylabel("Yatay elastik tasarım spektral ivmesi")
plt.show()
