import sqlite3

#Create sqlite db connection object, then cursor on that object

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()


#Removes old Counts table if it exists, and creates a new one

cur.execute('''
	DROP TABLE IF EXISTS Counts''')

cur.execute('''
	CREATE TABLE Counts (org TEXT, count INTEGER)''')

# takes input file name, opens file
fname = input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'mbox-short.txt'
fh = open(fname)

# for line in file takes lines that start with from, splits line, and grabs content after from: that we define as email
for line in fh:
	if not line.startswith('From: ') : continue
	pieces = line.split()
	print(pieces)
	email = pieces[1]
	tempList = email.split('@')
	org = tempList[1]
	#select count where org exists, uses paramater sub instead of string interpolation to avoid SQL injection
	cur.execute('SELECT count FROM Counts WHERE org = ? ', (org, ))
	#grabs email row as a list, updates count field, avoids 0 rows failing
	try:
		count = cur.fetchone() [0]
		cur.execute('UPDATE Counts SET count=count+1 WHERE org = ?', (org, ))
	#if try fails/org doesn't exist already, insert a new row with org and count of 1
	except:
		cur.execute('''INSERT INTO Counts (org, count) VALUES ( ?, 1 )''', (org, ))
	conn.commit()

# selects top 10 orgs and their and counts and print
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
	print(str(row[0]), row[1])
	
cur.close()