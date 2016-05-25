import requests
import shutil # for downloading images
import uuid # unique id
import base64
from proTemplate import *
import sys

def downloadImage(url, outName):
	imageRequest = requests.get(url, stream=True)
	with open(outName, 'wb') as out_file:
		shutil.copyfileobj(imageRequest.raw, out_file)
	del imageRequest
	return outName

imageDirectory = '/Users/kevindoveton/Desktop/instaPro5/cache/' # include leading and trailing slashes (/)
fileName = '../feed.pro5'


fileName = imageDirectory+fileName
accessToken = "344498719.d00b769.b32fd02b60ae4882b8f0d686f8cd20e2"
accessTokenPublic = '344498719.d00b769.b32fd02b60ae4882b8f0d686f8cd20e2'
clientSecret = "b4cb2e71cdcd4164895eadf8e2231954"
clientId = "d00b769d8f054964b7a2b9cfca3ded59"

baseUrl = 'https://api.instagram.com/v1/'

tag = sys.argv[1]
fullUrl= baseUrl+'tags/'+tag+'/media/recent/?&access_token='+accessToken
r = requests.get(fullUrl)
jsonData = r.json()

imageContent = list()
count = 0
for data in jsonData['data']:
	count += 1

if count != 1:
	print "Found " + str(count) + " photos with tag " + str(sys.argv[1])
else:
	print "Found " + str(count) + " photo " + str(sys.argv[1])


curCount = 0
for data in jsonData['data']:
	curCount +=1
	print "Download "+ str(curCount) +" of "+ str(count)
	image = data['images']['standard_resolution']['url']
	user = data['user']['username']
	userImage = data['user']['profile_picture']
	caption = data['caption']['text']
	imagePath = downloadImage(image, imageDirectory+str(uuid.uuid4())+'.jpg')
	userImagePath = downloadImage(userImage, imageDirectory+str(uuid.uuid4())+'.jpg')
	imageContent.append({'user':user, 'imagePath':imagePath, 'userImagePath':userImagePath, 'caption':caption})






f = open(fileName, 'w')

# add header
f.write(headerTemplate())

for slide in imageContent:
	captionText = '''{\\rtf1\\ansi\\ansicpg1252\\cocoartf1348\\cocoasubrtf170\n\\cocoascreenfonts1{\\fonttbl\\f0\\fswiss\\fcharset0 Helvetica-Light;}\n
{\\colortbl;\\red255\\green255\\blue255;}\n\\pard\\tx560\\tx1120\\tx1680\\tx2240\\tx2800\\tx3360\\tx3920\\tx4480\\tx5040\\tx5600\\tx6160\\tx6720
\\pardirnatural\n\n\\f0\\fs96 \\cf1 \\expnd0\\expndtw0\\kerning0\n\\outl0\\strokewidth-20 \\strokec0 ''' + slide['caption'] + '}'

	usernameText = '''{\\rtf1\\ansi\\ansicpg1252\\cocoartf1348\\cocoasubrtf170\n\\cocoascreenfonts1{\\fonttbl\\f0\\fswiss\\fcharset0 Helvetica;}
\n{\\colortbl;\\red255\\green255\\blue255;}\n\\pard\\tx560\\tx1120\\tx1680\\tx2240\\tx2800\\tx3360\\tx3920\\tx4480\\tx5040\\tx5600\\tx6160\\tx6720
\\pardirnatural\n\n\\f0\\fs112 \\cf1 \\expnd0\\expndtw0\\kerning0\n\\outl0\\strokewidth-20 \\strokec0 '''+ slide['user'] + '}'
	
	# write slide
	# slideTemplate(userName, captionText, imagePath, userImagePath):
	f.write(slideTemplate(base64.b64encode(usernameText), base64.b64encode(captionText), slide['imagePath'], slide['userImagePath']))

f.write(footerTemplate())

f.close()






# https://api.instagram.com/v1//{tag-name}/media/recent?access_token=ACCESS-TOKEN
