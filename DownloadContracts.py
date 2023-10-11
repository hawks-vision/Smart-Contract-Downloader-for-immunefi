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
args=parser.parse_args()
def extractingContractLinks():
    req=Request(url = "https://immunefi.com/bounty/"+args.projectname+"/",headers={'User-Agent': 'Mozilla/5.0'})
    page = urlopen(req)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    for i in soup.find_all("a",{'href': re.compile(r'etherscan\.io/')}):
        # print(i.get('title'))
        linkArr.append(i.get('title'))
    
def DownloadingSmartContracts():
    for i in linkArr:
        print(i.split('/')[-1])
        os.system('ethereum-sources-downloader ' + args.explorer +' '+ i.split('/')[-1])




extractingContractLinks()
DownloadingSmartContracts()