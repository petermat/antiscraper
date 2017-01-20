#!/usr/bin/env python3

# Usage: mitmdump -s "antiscraper.py"
# (this script works best with --anticache)

from mitmproxy import ctx #for logging
import sys, re
from bs4 import BeautifulSoup


class Injector:
    #def __init__(self, iframe_url):
    #    self.iframe_url = iframe_url


    def response(self, flow):
        #if flow.request.host in self.iframe_url:
        #    return
        html = BeautifulSoup(flow.response.content, "html.parser")
        if html.body:

            ## insert iframe
            #iframe = html.new_tag(
            #    "iframe",
            #    src=self.iframe_url,
            #    frameborder=0,
            #    height=0,
            #    width=0)
            #html.body.insert(0, iframe)

            ## print tags
            #for tag in html.find_all(True):
            #    print(tag.name)

            ## text replacement
            findtoure = html.find_all(text=re.compile('HTML'))
            for comment in findtoure:
                fixed_text = comment.replace('HTML', 'Yaya Toure')
                comment.replace_with(fixed_text)

        flow.response.content = str(html).encode("utf8")



def start():
    if len(sys.argv) != 1:
        raise ValueError('Usage: -s "antiscraper.py"')
    return Injector()#(sys.argv[1])