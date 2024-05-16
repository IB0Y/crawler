from urllib.request import urlopen
from linkFinder import LinkFinder
from general import *

class Spider:
# class variables (shared among all instances of this class)
      project_name =''
      baseURL=''
      domain_name=''
      queue_file =''
      crawled_file =''
      queue = set()
      clawled = set()   
      
def __init__(self, project_name, baseURL, domain_name):
    Spider.project_name = project_name
    Spider.baseURL = baseURL
    Spider.domain_name = domain_name
    Spider.queue_file = Spider.project_name + '/queue.txt'
    Spider.crawled_file = Spider.project_name + '/crawled.txt'
    
    self.boot()
    self.crawl_page("First spider", baseURL)
    

@staticmethod    
def booot():
    create_project_dir(Spider.project_name)
    create_data_files(Spider.project_name, Spider.baseURL)
    
    Spider.queue = file_to_set(Spider.queue_file)
    Spider.crawled = file_to_set(Spider.crawled_file)    
    
@staticmethod    
def crawl_page(thread_name, baseURL):    
    if baseURL not in Spider.queue:
        print(thread_name + " now crawling " + baseURL)
        print('Queue '+ str(len(Spider.queue)) + '| crawled ' + str(len(Spider.crawled)))
        
        Spider.add_links_to_queue(Spider.gather_links(baseURL))
        Spider.queue.remove(baseURL)
        Spider.crawled.add(baseURL)
        
        Spider.update_files()