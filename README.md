# Smart-Contract-Downloader-for-immunefi
This contains a simple python script which helps you in downloading complete set of contracts from a specified immunefi project.




## Installation


```bash
  
$ git clone https://github.com/hawks-vision/Smart-Contract-Downloader-for-immunefi.git

$ cd Smart-Contract-Downloader-for-immunefi

$ python -m pip install -r requirements.txt or pip install -r requirements.txt

$ npm i -g ethereum-sources-downloader

$ python3.11 DownloadContracts.py
```
    
## Usage/Examples

```javascript
Usage: DownloadContracts.py [-h] --explorer EXPLORER --projectname PROJECTNAME

options:
  -h, --help            show this help message and exit
  --explorer EXPLORER, -e EXPLORER
                        specify the explorer ex: etherscan
  --projectname PROJECTNAME, -p PROJECTNAME
                        specify the name of the project as mentioned in immunefi ex: thegraph
  --out [OUT], -o [OUT]
                        to specify the output directory(optional)


Example:
    python3.11 DownloadContracts.py -e etherscan -p thegraph -o #foldername(optional)

```

