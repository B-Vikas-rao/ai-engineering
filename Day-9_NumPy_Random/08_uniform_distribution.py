import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
data=np.random.uniform(low=10,high=20,size=1000)
print(data)
sns.histplot(data,kde=True)
plt.show()