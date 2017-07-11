    import numpy as np
    import pandas as pd
    a = pd.DataFrame(np.arange(10,dtype=object).reshape(-1,2))
    print a
    b = pd.DataFrame(a)
    c = a == b
    c_np = c.as_matrix()
    print c_np
    sums = np.sum(c_np.astype(int),axis=1)
    print sums.shape
    print sums
