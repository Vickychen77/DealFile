import os, shutil
# path=str(input(r'please input file path:')) 

stopword = '' 
path = ''
for line in iter(input, stopword): 
  path += line + '\n'

tmp_path=path.split(' ')

for path in tmp_path:
    if "pages" in path:
        curPath=os.getcwd()
        path.replace('\\','\\\\')  
        source_path=curPath.replace('\\','/')+'/'+str(path)
        target_path=source_path.replace('wxapp','wxapp-dist')

        shutil.copy(source_path,target_path)
        print('copy success')
    
  