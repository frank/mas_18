import numpy as np
triggers = 0
for i in range(1000):
    temp = np.random.normal(0, 0.4)
    if temp > 0.5:
        triggers += 1
print(triggers / float(10))
