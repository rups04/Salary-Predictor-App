import pandas as pd
ds=pd.read_csv('/home/SALARY.csv')
x=ds['YearsExperience'].values.reshape(-1,1)
y=ds['Salary']
from sklearn.linear_model import LinearRegression
mind=LinearRegression()
model=mind.fit(x,y)
print("""        ---------------------------------
           ||||  Welcome to Salary Predictor App  ||||
               ---------------------------------- \n
                  ***************************
         Note: !!  Press -1 to exit this app  !!
                  ***************************   \n  """)
while(True):
  p=input('Enter no of year : ')
  s=float(p)
  if int(s) < 0 :
     exit()
  o=model.predict([[s]])
  print("Predicted Salary is :", o , "\n")
