import sys,os
from jsbeautifier import beautify_file,default_options

def listingf(dirList): 
    filesToBeProcessed = []

    for paths,dirs,files in os.walk(dirList): 
        for file in files: 
            filesToBeProcessed.append(os.path.join(os.path.abspath(paths), file))

            opts = default_options()
            opts.wrap_line_length = 80
            
    for file in filesToBeProcessed: 
        res = beautify_file(file,opts);
        fnew = open(file, "w")
        fnew.write(res)

def main(): 
    listingf("/tmp/javascript-folder")

if __name__ == "__main__": 
    main()