In [1]: f = plt.imread('flower.jpg'
                      )

In [2]: t = 0.2

In [3]: epst = 0.01

In [4]:
while 1:
    ...: mL = f[f <= t].mean()
    ...: mH = f[f > t].mean()
    ...: t_new = (mL + mH) / 2
    ...:
    if abs(t - t_new) < epst:
        ...:
    break
    ...: t = t_new
    ...: print(t)
    ...:
