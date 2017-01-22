# ABOUT #

Antiscrapper is  a proof-of-concept script, using mitmproxy, that can obfuscate HTML code to mitigate basic web scrapping techniques.

Obfuscation is divided into modules:
* rename of variables
* randomize HTTP structure with minimal impact on design
* introduce sinkholes for scrap engines
* plain text obfuscation

## Technology ##

** mitmproxy **

* (mitmproxy.org)[https://mitmproxy.org/]
* (mimtproxy Inline Scripts)[ https://mitmproxy.org/doc/scripting/inlinescripts.html] 

** Python3 **

* (python3 docs)[https://docs.python.org]

** BeautifulSoup **


# Usage #


## Install ##
To run antiscrapper you need to install some dependencies.

### python3.5 ###

sudo apt-get install build-essential checkinstall

install python 3.5.x

``` sudo apt-get install python3-pip python3.5-dev libffi-dev libssl-dev libtiff5-dev libjpeg8-dev zlib1g-dev libwebp-dev

```
sudo add-apt-repository ppa:fkrull/deadsnakes
sudo apt-get update; 
sudo apt-get install python3.5
sudo python3.5 -m pip install -U setuptools
```

### venv ###
create venv env in working file
```virtualenv -p python3.5 venv```

activate venv
```source venv/bin/activate```

### mitmproxy ###
```sudo pip3.5 install mitmproxy```

### BeatifulSoap4 ###
pip3.5 install bs4
 

## Run ##

To test it out, run mitmproxy with this script in regular mode:

```mitmproxy -s "antiscraper.py"```

