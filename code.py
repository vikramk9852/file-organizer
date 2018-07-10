import os
import shutil
dir = os.getcwd()
check = [False]*9
files = ['']*10
files[0] = ['aif', 'cda', 'mid', 'midi', 'mp3', 'mpa', 'ogg', 'wav', 'wma', 'wpl', 'mp4a']
files[1] = ['7z', 'arj', 'deb', 'pkg', 'rar', 'rpm', 'gz', 'z', 'zip']
files[2] = ['apk']
files[3] = ['bat', 'bin', 'cgi', 'pl', 'com', 'exe', 'jar', 'wsf']
files[4] = ['ai', 'bmp', 'gif', 'ico', 'jpeg', 'jpg', 'png', 'ps', 'psd', 'svg', 'tif']
files[5] = ['bak', 'cab', 'cfg', 'cpl', 'cur', 'dll', 'dmp', 'drv', 'ico', 'ini', 'lnk', 'msi', 'sys', 'tmp']
files[6] = ['3g2', '3gp', 'avi', 'flv', 'h264', 'm4v', 'mkv', 'mov', 'mp4', 'mpg', 'mpeg', 'rm', 'swf', 'vob', 'swf', 'vob', 'wmv']
files[7] = ['doc', 'docx', 'odt', 'pdf', 'rtf', 'tex', 'txt', 'wks', 'wps', 'wpd']
files[8] = ['c', 'cpp', 'html', 'css', 'py', 'cs', 'd', 'db', 'lisp', 'r', 'pyw', 'java', 'js', 'rb', 'xml', 'aspx', 'rss', 'htm', 'xhtml', 'cgi']
extension = ['audio', 'compressed', 'android', 'executable', 'image', 'system', 'video', 'docs', 'programming']
try:
	os.mkdir('others')
except:
	print('can not create')
for i in os.listdir():
	temp = i.split('.')
	last = len(temp)-1
	found = False
	if temp[0] == 'sorter':
		continue;
	if os.path.isfile(i):
		print(temp)
		for j in range(9):
			if temp[last] in files[j]:
				if check[j] == False:
					check[j] = True
					try:
						os.mkdir(extension[j])
					except:
						print('can not create')
				shutil.move(os.path.join(dir, i), os.path.join(dir, extension[j]))
				found = True
				break
		if found == False:
			shutil.move(os.path.join(dir, i), os.path.join(dir, 'others'))