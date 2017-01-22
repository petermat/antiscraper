#!/usr/bin/env python3

# Usage: mitmdump -s "antiscraper.py"
# (this script works best with --anticache)

from mitmproxy import ctx #for logging
import sys, re
from bs4 import BeautifulSoup
import string
import random

class Injector:
    #def __init__(self, iframe_url):
    #    self.iframe_url = iframe_url


    def response(self, flow):
        #if flow.request.host in self.iframe_url:
        #    return
        html = BeautifulSoup(flow.response.content, "html.parser")
        if html.body:

            ## PROTOTYPE insert iframe
            #iframe = html.new_tag(
            #    "iframe",
            #    src=self.iframe_url,
            #    frameborder=0,
            #    height=0,
            #    width=0)
            #html.body.insert(0, iframe)

            ## PROTOTYPE loop all tags
            #for tag in html.find_all(True):
            #    print(tag.name)

            ## PROTOTYPE text replacement
            #findtoure = html.find_all(text=re.compile('About'))
            #for comment in findtoure:
            #    fixed_text = comment.replace('About', 'XXXXXXX')
            #    print("fixed_text:", fixed_text)
            #    comment.replace_with(fixed_text)

            ## create dict of identificators
            # <div class="donate-alt">
            class_identificators = {}
            # all_class_objs = html.find_all(lambda tag: tag.get('id') == True or tag.get('class') == True)
            all_class_objs = html.find_all(True, {'class': True})
            print('number of class objs:', len(all_class_objs))

            for class_object in all_class_objs:
                print("class_object['class']:", type(class_object['class']), " full: ", class_object['class'])
                #print( "type class_object:", type(class_object))


                #if isinstance(class_object['class'], list):
                #    class_object['class'] = str(class_object['class'])

                ## class_object is list of css class names, loop required
                for x, classname in enumerate(class_object['class']):

                    ## add random string as value to classname key
                    if classname not in class_identificators.keys():
                        newclass_name = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(12))
                        class_identificators[classname] = newclass_name

                    ## substitude identificators in HTML body and CSS files
                    tags_to_edit = html.find_all(True, {'class': classname})
                    for tag_to_edit in tags_to_edit:
                        if x<1:
                            tag_to_edit['class'] = class_identificators[classname]
                        else:
                            tag_to_edit['class'] = str(tag_to_edit['class']) + ' ' +  str(class_identificators[classname])

                        #edited_tag = tag_to_edit.replace(classname, class_identificators[classname])
                        #tag_to_edit.replace_with(edited_tag)

                ## substitude ifentificators in HTML body and CSS files

                    #print(classname, ":",class_identificators[classname])
                    #print("class_object len:", len(class_object))
                    #print("type(class_object)", type(class_object))
                    #print("class_object", (class_object), '\n')
                    #print("class_object['class']",class_object['class'][x])
                    #class_objects['class'][x] = class_identificators[class_object['class'][x]]
                    #edited_content =
                    #edited_content = class_object.replace(classname, class_identificators[classname])

                #class_objects.replace_with(edited_content)



            print("class_identificators:",class_identificators)



        flow.response.content = str(html).encode("utf8")



def start():
    if len(sys.argv) != 1:
        raise ValueError('Usage: -s "antiscraper.py"')
    return Injector()#(sys.argv[1])