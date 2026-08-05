import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
data=np.random.binomial(n=10,p=0.5,size=1000)
print(data)
sns.histplot(data,kde=True)
plt.show()