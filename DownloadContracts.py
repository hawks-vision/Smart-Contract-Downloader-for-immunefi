import os
import re
import string
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import argparse

linkArr=[]
parser= argparse.ArgumentParser()
parser.add_argument("--explorer","-e",type=str,help="specify the explorer ex: etherscan",required=True)
parser.add_argument("--projectname","-p",type=str,help="specify the name of the project as mentioned in immunefi ex: thegraph",required=True)
parser.add_argument("--out","-o",type=str,nargs="?", default="out",const="out",help="to specify the output directory(optional)")
args=parser.parse_args()

def extractingContractLinks():
    req=Request(url = "https://immunefi.com/bounty/"+args.projectname+"/",headers={'User-Agent': 'Mozilla/5.0'})
    page = urlopen(req)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    for i in soup.find_all("a",{'href': re.compile(r'({0})'.format(args.explorer))}):
        #print(i.get('title'))
        linkArr.append(i.get('title'))
    
def DownloadingSmartContracts():
    for i in linkArr:
        head,sed,tail=(i.split('/')[-1]).partition('?')
        # print(head)
        # print(args.out)
        os.system('ethereum-sources-downloader ' + args.explorer +' '+ head+ ' ' +args.out)

def CreatingMindMap():
    os.system('Rscript ./tree_To_mindMap.R' + ' ' +args.out)
    os.system('mv ./file*.mm ./'+args.out+'/'+args.out+'.mm')



extractingContractLinks()
DownloadingSmartContracts()
CreatingMindMap()
