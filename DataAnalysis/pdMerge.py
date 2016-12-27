import pandas as pd 

df1 = pd.DataFrame({'Temp':[75,73,72,68],
					'Humidity':[55,60,72,58],
					'Precip':[0,0,0,25]})

df2 = pd.DataFrame({'Temp':[75,73,72,68],
					'Humidity':[35,40,42,37],
					'Precip':[2,0,5,2]})

print(pd.merge(df1, df2, on='Temp'))

main_users = pd.DataFrame({'Username':['Michael','Jessica','John','Samir'],
						   'Password':['P@ssw0rd','1234','pass','pw'],
						   'Join_Date':['Jan','Feb','Jan','March']})
forum_users = pd.DataFrame({'Username':['Michael','Jessica','John','Samir'],
						   'Post_Count':[500, 521, 76, 888],
						   'User_Status':[0, 1, 0, 2]})

print(pd.merge(main_users, forum_users, on='Username'))