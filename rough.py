'''if  '2' == 2:
    print("true")
else: print("false")

print([(i.upper(), len(i)) for i in 'kiwi'])
print([x*y for x, y in zip([3,4],[5,6])])
class A:
    def __init__(self, a = 5):
        self.a = a

        def f1(self):
            self.a += 10


class B(A):
    def __init__(self, b = 0):
        A.__init__(self, 4)
        self.b = b

    def f1(self):
        self.b += 10

x = B()
x.f1()
print(x.a,'-', x.b)

class class1:
    a = 1

    def f1(self):
        a = 2
        class1.a += 1
        print(class1.a, end=' ')
        print(a, end=' ')

class1().f1()
class1().f1()
print()
print({i:j for i in "abcd" for j in "kiwi"})'''

from yahoo_fin.stock_info import get_data,get_day_losers,tickers_sp500, tickers_nasdaq, tickers_other, get_quote_table,get_balance_sheet,get_income_statement
import pandas as pd
ntflx = get_data("MSFT")
df = pd.DataFrame(ntflx,columns=['open','high','low','adjclose','volume'],dtype=float)
print(ntflx)

print(df.tail(1))
df_js= df.tail(1).to_json()
print(df_js)
print(" ")
df1=df.tail(1)
print(df1['open'])
print(" ")
df2= df1['open'].to_json()
print(df2[17:])
df3=df2[17:]
print(" ")
print(df3[:-1])


loser = get_day_losers()
print(loser)
df = pd.DataFrame(loser,columns=['Symbol','Name','Price (Intraday)','Change','%Change'])
print(df.head(5))
data=[]
df1=df.head(5)
for ind in df1.index:
    dic ={
        'Symbol':df1['Symbol'][ind],
        'Name':df1['Name'][ind],
        'Change':df1['Change'][ind]
    }
    data.append(dic)

print(data)
print(" ")
msft = get_balance_sheet("MSFT")
print(msft)
print("")
print("")
line= get_income_statement("MSFT")
df = pd.DataFrame(line,columns=['Breakdown','ttm','6/30/2019','6/30/2018','6/30/2017'])
print(df)

print("hello world")
print("")
df_js=df.to_json()
print(df_js)
fp = open("test.txt",'w+')
for ind in df.index:
    fp.write("%s %s %s %s %s \n"%df['Breakdown'][ind] %df['ttm'][ind] %df['6/30/2019'][ind] %df['6/30/2018'][ind] %df['6/30/2017'][ind])

