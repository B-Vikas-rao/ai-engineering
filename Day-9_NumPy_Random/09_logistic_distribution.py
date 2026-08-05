import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
data=np.random.logistic(loc=0,scale=1,size=1000)
print(data)
sns.histplot(data,kde=True)
plt.show()