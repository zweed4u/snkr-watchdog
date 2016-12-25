#!/usr/bin/python3
import json, time, datetime, requests
session=requests.session()
items={}
url='https://api.nike.com/commerce/productfeed/products/snkrs/threads?country=US&limit=20&locale=en_US&withCards=true'
counter=0
while 1:
	try:
		r=session.get(url)
		itemsCaptured=0
		previousCapture=0
		for card in r.json()['threads']:
			try:
				cardAttribs=[]
				title=str(card['product']['title'])
				launchDate=str(card['product']['estimatedLaunchDate'])
				imageUrl=str(card['product']['imageUrl'])
				styleCode=str(card['product']['style']+'-'+card['product']['colorCode'])
				cardAttribs.append(title)
				cardAttribs.append(launchDate)
				cardAttribs.append(imageUrl)
				if styleCode not in items.keys():
					items[styleCode]=cardAttribs
					print('')
					print(str(datetime.datetime.now()) + ' :: '+ styleCode+' FOUND!')
					print(items[styleCode])
					print('')
					itemsCaptured+=1
					if counter != 0:
						#stub - item is new and found on subsequent pass
						pass
				else:
					pass
			except:
				continue
		if previousCapture==itemsCaptured:
			print(str(datetime.datetime.now()) + ' :: '+'No new items found this pass!')
		else:
			#New items found/deleted! Should be outputted via line 21
			previousCapture=itemsCaptured
		counter+=1
		time.sleep(60)
	except Exception as e:
		print e 