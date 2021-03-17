import pandas as pd
from scipy.stats import pareto 
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import rcParams

############################clean 
############################loads xlsx
############################returns 3 column DF

df = pd.read_excel('/home/vivek/Documents/sales/sales.xlsx')
df = df.head(600)
df =df[['State', 'Sub Category', 'Cost', 'Revenue']]
df['profit'] = df['Revenue']-df['Cost']
df.rename(columns = {'Sub Category':'category', 'State': 'state', 'Revenue': 'revenue'}, inplace = True) 
df =df[['state', 'category', 'profit']]

############################loss makers
############################takes the unsummarized df
############################returns the percentage of orders making loss
lossmakers = 100*len(df[df.profit<0])/len(df)


############################summarize 
############################ltakes 3 column df from clean
############################returns 3 column DF
product_list_1 = []
states = df.state.unique()
for state in states:
    df_1 = df[df.state == state]
    categories = df_1.category.unique()
    for category in categories:
        df_2 = df_1[df_1.category == category]
        profit = df_2.profit.sum()
        result_item = {
            'customer' : state,
            'product': category,
            'profit' : profit
        }
        product_list_1.append(result_item)
        
df = pd.DataFrame(product_list_1)
df = df.sort_values(by = 'profit')


###########################loss_scatter_plot
###########################Takes 3 column df from summarize
###########################returns a scatter plot
sns.set(font_scale=3)
df = df[df.profit<0] 
print(df)
df.profit = df.profit*-1
plt.scatter(x = df['product'], y = df['customer'], s = df['profit']*10 )
plt.xticks(rotation=45)


###########################loss_scatter_plot
###########################Takes 3 column df from summarize
###########################returns a scatter plot
sns.set(font_scale=3)
df = df[df.profit >= 0] 
print(df)
plt.scatter(x = df['product'], y = df['customer'], s = df['profit']*10 )
plt.xticks(rotation=45)      

