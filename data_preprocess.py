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

        self.concat_y()


    def concat_y(self):

        print(np.unique(self.y))

        # 0对应无，1为使用，2为弃用，-1后得到0为无启用，1为弃用，则总的y只要有一项弃用就视为弃用
        self.y =(self.y - 1)

        self.y[self.y is np.nan] =0
        self.y = self.y.astype(np.int32)
        print(np.unique(self.y))
        self.total_y = self.y.any(axis=1)

    def split_dataset(self, r):
        train_set = []
        test_set = []
        return train_set,test_set




def main():

    d = MyDataset('./data.xls')

if __name__ == '__main__':
    main()