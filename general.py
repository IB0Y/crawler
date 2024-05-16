import os

# Each website has its own separate folder
def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating directory ' + directory)
        os.makedirs(directory)

# Creare queue and crawled files (if not created already)
def create_data_files(project_name, base_url):
   queue = project_name + '/queue.txt'
   crawled = project_name + '/crawled.txt'

   if not os.path.isfile(queue):
      write_file(queue, base_url)

   if not os.path.isfile(crawled):
      write_file(crawled, '')

# create files
def  write_file(path, data):     
   f = open(path, 'w')
   f.write(data)
   f.close()

# add data to existing file
def append_to_file(path, data):
   with open(path, 'a') as file:
      file.write(data + '\n')


# Delete the content of a file
def delete_file_content(path):
   with open(path, 'w'):
      pass


# Read a file and convert each line to set items
def file_to_set(file_name):
   results = set()

   with open(file_name, 'rt') as op:
      for line in op:
         results.add(line.replace('\n', ''))


# Iterate through a set, each item will be  a new line in a file
def set_to_file(links, file):
   delete_file_content(file)

   for link in sorted(links):
      append_to_file(file, link)
