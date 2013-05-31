import gspreadwrapper

user = 'your gdoc username here'
id = 'your gdoc unique id here'
pw = 'your gdoc password here'
column =2

try:
	gSpreadsheet = gspreadwrapper.GspreadsheetUtil(user, pw, id, column)
	#get a set without column header
	column_set=set(gSpreadsheet.returnSingleColumnFirstWorksheet()[1:])
except gspreadwrapper.WrapperError as err:
	print str(err)
	exit()
for cell in column_set:
	print cell