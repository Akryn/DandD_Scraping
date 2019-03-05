import requests, bs4, re
from pandas import DataFrame as df

res = requests.get('https://www.dndbeyond.com/sources/basic-rules/monster-stat-blocks-a')
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')

monsterNames = soup.find_all(class_="tooltip-hover monster-tooltip")
statBlocks = soup.find_all(class_='stat-block-ability-scores')

STRRegex = re.compile(r'\nSTR\n(\d+)\(')
DEXRegex = re.compile(r'\nDEX\n(\d+)\(')
CONRegex = re.compile(r'\nCON\n(\d+)\(')
INTRegex = re.compile(r'\nINT\n(\d+)\(')
WISRegex = re.compile(r'\nWIS\n(\d+)\(')
CHARegex = re.compile(r'\nCHA\n(\d+)\(')

d = df({'Name': [], 'STR': [], 'DEX': [], 'CON': [], 'INT': [], 'WIS': [], 'CHA': []})
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
    d = d.append({'Name': monsterNames[i].getText(), 'STR': thisSTR, 'DEX': thisDEX, 'CON': thisCON, 'INT': thisINT, 'WIS': thisWIS, 'CHA': thisCHA}, ignore_index=True)

print(d)
