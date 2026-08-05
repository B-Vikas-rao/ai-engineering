import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
data=np.random.normal(loc=50,scale=10,size=1000)
print(data)
sns.histplot(data,kde=True)
plt.show()