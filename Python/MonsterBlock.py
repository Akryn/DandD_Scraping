# I have a problem that not all monsters found have a challenge rating.
# This means monsterNames and statBlocks are longer than challengeRating.
# I need to detect if it doesn't have a Challenge Rating and then enter NA.

import requests, bs4, re
from pandas import DataFrame as df

d = df({'Name': [], 'STR': [], 'DEX': [], 'CON': [], 'INT': [], 'WIS': [], 'CHA': []})
#d = df({'Name': [], 'STR': [], 'DEX': [], 'CON': [], 'INT': [], 'WIS': [], 'CHA': [], 'Challenge Rating': []})

STRRegex = re.compile(r'\nSTR\n(\d+)\(')
DEXRegex = re.compile(r'\nDEX\n(\d+)\(')
CONRegex = re.compile(r'\nCON\n(\d+)\(')
INTRegex = re.compile(r'\nINT\n(\d+)\(')
WISRegex = re.compile(r'\nWIS\n(\d+)\(')
CHARegex = re.compile(r'\nCHA\n(\d+)\(')
#challengeRatingRegex = re.compile(r'Challenge( |\xa0)(.*) \(')
        
for letter in 'abcdefghijklmnopqrstuvwxyz':
    try:
        res = requests.get('https://www.dndbeyond.com/sources/basic-rules/monster-stat-blocks-' + letter)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        monsterNames = soup.find_all(class_='Stat-Block-Styles_Stat-Block-Title')
        statBlocks = soup.find_all(class_='stat-block-ability-scores')
        #challengeRating = soup.find_all(class_='Stat-Block-Styles_Stat-Block-Data-Last')

        for i in range(len(monsterNames)):
                STRMatch = STRRegex.search(statBlocks[i].getText())
                thisSTR = int(STRMatch.group(1))
                DEXMatch = DEXRegex.search(statBlocks[i].getText())
                thisDEX = int(DEXMatch.group(1))
                CONMatch = CONRegex.search(statBlocks[i].getText())
                thisCON = int(CONMatch.group(1))
                INTMatch = INTRegex.search(statBlocks[i].getText())
                thisINT = int(INTMatch.group(1))
                WISMatch = WISRegex.search(statBlocks[i].getText())
                thisWIS = int(WISMatch.group(1))
                CHAMatch = CHARegex.search(statBlocks[i].getText())
                thisCHA = int(CHAMatch.group(1))
                #challengeRatingMatch = challengeRatingRegex.search(challengeRating[i].getText())
                #thisChallengeRating = challengeRatingMatch.group(2)
                #if '/' in thisChallengeRating:
                #    thisChallengeRating = float(thisChallengeRating[0:thisChallengeRating.find('/')]) / float(thisChallengeRating[thisChallengeRating.find('/')+1:])
                #else:
                #    thisChallengeRating = float(thisChallengeRating)
                d = d.append({'Name': monsterNames[i].getText(), 'STR': thisSTR, 'DEX': thisDEX, 'CON': thisCON, 'INT': thisINT, 'WIS': thisWIS, 'CHA': thisCHA}, ignore_index=True)
                #d = d.append({'Name': monsterNames[i].getText(), 'STR': thisSTR, 'DEX': thisDEX, 'CON': thisCON, 'INT': thisINT, 'WIS': thisWIS, 'CHA': thisCHA, 'Challenge Rating': thisChallengeRating}, ignore_index=True)
    except:
        print('Could not retried any information for letter ' + letter)

print(d)
