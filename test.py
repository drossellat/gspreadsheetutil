import gspreadwrapper

user = 'david.rossellat@gmail.com'
id = '0AoaX3_6iySVKdE10blRXaU1JZENGTUdjN0F5TVMzVUE'
pw = '8000Zurich$'
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