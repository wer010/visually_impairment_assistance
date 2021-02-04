import pandas as pd
import numpy as np

class MyDataset:
    def __init__(self,s):
        self.data = pd.read_excel(s)
        heads = self.data.columns
        num_columns = self.data.shape[1]
        self.x=[]
        self.y=[]
        self.extra_x = []
        for i in range(num_columns):
            if 'X' in heads[i]:
                self.x.append(np.array(self.data.iloc[:,i]))
            elif 'Y' in heads[i]:
                self.y.append(np.array(self.data.iloc[:,i]))
                self.extra_x.append(np.array(self.data.iloc[:, i + 1]))
                self.extra_x.append(np.array(self.data.iloc[:, i + 2]))
                self.extra_x.append(np.array(self.data.iloc[:, i + 3]))
                self.extra_x.append(np.array(self.data.iloc[:, i + 4]))
        self.x = np.stack(self.x).transpose()
        self.y = np.stack(self.y).transpose()
        self.extra_x = np.stack(self.extra_x).transpose()

    def get_data(self, op = 1, normalization = True):
        if op == 1:
            ret_x, ret_y = self.op_1st
        else:
            ret_x, ret_y = self.op_2nd
        if normalization:
            ret_x = self.data_normalize(ret_x)
        return ret_x,ret_y

    @property
    def op_1st(self):
        # 149 data samples corresponding to the 149 subjects, which concat the 19 y into a single value.
        # print(np.unique(self.y))
        # 0对应无，1为使用，2为弃用，-1后得到 0为无弃用，1为弃用，则总的y只要有一项弃用就视为弃用
        res_y = (self.y - 1)
        res_y[np.isnan(res_y)] = 0
        res_y = res_y.astype(np.int32)
        # print(np.unique(res_y))
        ret_y = res_y.any(axis=1).astype(np.int8)
        ret_x = self.x
        return ret_x,ret_y

    @property
    def op_2nd(self):
        # n data samples from 149 subjects, for single item in 19 y, we consider each y situation as a new samples
        num_y = self.y.shape[1]
        res_x = []
        res_y = []
        for i in range(num_y):
            res = self.y[:,i]
            mask = ~np.isnan(res)
            res_x.append(np.concatenate([self.x[mask],self.extra_x[mask,i*4:i*4+4]],axis=1))
            res_y.append(self.y[mask,i])
        ret_x = np.concatenate(res_x)
        ret_y = np.concatenate(res_y)
        ret_y = (ret_y-1).astype(np.int32)
        assert ~np.any(np.isnan(ret_x))
        return ret_x,ret_y

    def data_normalize(self, data):
        lower_bound = np.min(data,axis=0)
        upper_bound = np.max(data,axis=0)
        ret = (data - lower_bound)/(upper_bound - lower_bound)
        return ret

    def split_dataset(self, r):
        train_set = []
        test_set = []
        return train_set,test_set




def main():
    d = MyDataset('./data.xls')

if __name__ == '__main__':
    main()