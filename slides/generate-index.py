import os

indexTextStart = """<!DOCTYPE html>
<html>
<head><title>Index des diaporamas</title>
<link rel="stylesheet" href="../assets/css/style.css?v=55737e59e31450a18a2dbc6e8d4ff07b395949cf">
</head>
<body>
	<div class="container-lg px-3 my-5 markdown-body">
    <h2>Index des diaporamas</h2>
    <ul>
		<li>
			<a href='../'>../</a>
		</li>
"""
indexTextEnd = """
	</ul>
	</div>
</body>
</html>
"""

def index_folder(folderPath):
	print("Indexing: " + folderPath +'/')
	#Getting the content of the folder
	files = sorted(os.listdir(folderPath))
	#If Root folder, correcting folder name
	root = folderPath
	if folderPath == '.':
		root = 'Root'
	indexText = indexTextStart.format(folderPath=root)
	for file in files:
		#Avoiding index.html files
		if file != 'index.html':
			exthtml = file[-4:]
			if exthtml == 'html': 
				indexText += "\t\t<li>\n\t\t\t<a href='" + file + "'>" + file + "</a>\n\t\t</li>\n"
		#Recursive call to continue indexing
		if os.path.isdir(folderPath+'/'+file):
			index_folder(folderPath + '/' + file)
	indexText += indexTextEnd
	#Create or override previous index.html
	index = open(folderPath+'/index.html', "w")
	#Save indexed content to file
	index.write(indexText)

#Indexing root directory (Script position)
index_folder('.')
