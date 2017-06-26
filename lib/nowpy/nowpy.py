# -*- coding: utf-8 -*-
"""
Pythonでのあれこれ
"""
#----------------------------------
__author__ = "R.Imai"
__version__ = "0.0.0"
__created__ = "2017/06/26"
__date__ = "2017/06/26"
#----------------------------------

class mean_std_collector:
    def __init__(self, arr = []):
        if len(arr) == 0:
            self.mean = 0
            self.std = 1
            self.n = 0
            self.sum = 0
        else:
            self.mean = np.mean(arr)
            self.std = np.std(arr)
            self.n = len(arr)
            self.sum = sum(arr)

    def __call__(self):
        print("mean: {0}\nstd: {1}\nsum: {2}\nlength: {3}".format(self.mean, self.std, self.sum, self.n))

    def _calc_new_mean(self, arr):
        return (self.mean*self.n + sum(arr))/(self.n + len(arr))

    def _calc_new_std(self, arr, new_mean):
        y = lambda d: -2*self.sum*d + (new_mean-self.mean)*(new_mean+self.mean)*self.n
        d = new_mean - self.mean
        sig = self.std*self.std*self.n
        return ((sig + y(d) + sum((np.array(arr)-new_mean)**2))/(self.n + len(arr)))**0.5

    def append(self,arr):
        new_mean = self._calc_new_mean(arr)
        new_std = self._calc_new_std(arr, new_mean)

        self.mean = new_mean
        self.std = new_std
        self.n += len(arr)
        self.sum += sum(arr)

    def savetxt(self, path):
        pd.DataFrame([[self.mean,self.std,self.n,self.sum]], columns = ["mean_", "std_", "n_", "sum_"]).to_csv(path, index = None)

    def load(self, path):
        df = pd.read_csv(path)
        self.mean = float(df.mean_)
        self.std = float(df.std_)
        self.n = int(df.n_)
        self.sum = float(df.sum_)

if __name__ == '__main__':
    pass
