import requests
import time
import os
def score():
	a=requests.get("https://www.cricbuzz.com/live-cricket-scores/22775/nz-vs-ind-3rd-t20i-india-tour-of-new-zealand-2020")
	k=(a.text).split('<div class="cb-min-bat-rw"> <span class="cb-font-20 text-bold">')

	score = k[1].split('</span>')[0]
	print (score)
	wicket = (score.split('/')[1].split(" ")[0])
	return (score,wicket)

wicket=0


def score_ajax():
	a=requests.get("https://www.cricbuzz.com/api/html/cricket-scorecard/24184")
	k=(a.text.split('<span class="pull-right">')[1].split("</span>")[0].replace("&nbsp;",''))
	score = k
	print(score)
	wicket = (score.split('-')[1].split("(")[0])
	#print(wicket)
	return (score,wicket)


while True:
	
	#wicket2=int((score()[1]))
	wicket2=int((score_ajax()[1]))
	# print (wicket)
	# print (wicket2)
	if wicket2>wicket:
		wicket=wicket2
		
		os.system("say 'Wicket, opening hotstar'")
		os.system("open https://www.hotstar.com/in/sports/cricket/under19s-world-cup/india-under19s-vs-pakistan-under19s-m600880/live-streaming/1440006445")

	time.sleep(3)

