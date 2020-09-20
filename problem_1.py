import numpy as np
list_num = np.array([x for x in range(1,1000) if (x%3==0 or x%5==0)])
print(np.sum(list_num))