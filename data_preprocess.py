import pandas as pd
import numpy as np

class dataset:
    def __init__(self,s):
        self.data = pd.read_excel(s)
        heads = self.data.columns
        num_columns = self.data.shape[1]
        x=[]
        y=[]
        xx = []
        for i in range(num_columns):
            if 'X' in heads[i]:
                x.append(self.data.iloc[:,i])
            elif 'Y' in heads[i]:
                y.append(self.data.iloc[:,i])
                xx.append(self.data.iloc[:, i + 1])
                xx.append(self.data.iloc[:, i + 2])
                xx.append(self.data.iloc[:, i + 3])
                xx.append(self.data.iloc[:, i + 4])
        return x,y,xx

    def split_dataset(r):
        train_set = []
        test_set = []
        return train_set,test_set




def main():

    read_excel('./data.xls')

if __name__ == '__main__':
    main()