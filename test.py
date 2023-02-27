import os
import argparse


def parse():
    argParser = argparse.ArgumentParser()
    argParser.add_argument("-s", "--start", action="store_true", help="initialize remote repository")
    argParser.add_argument("-u", "--url", help="repository URL")
    argParser.add_argument("-p", "--push", action="store_true", help="push to the repository if no arguments selected everything is pushed")
    argParser.add_argument("-f", "--files", help="file list to push")



    args = argParser.parse_args()
    
    return args

def execute(args):
    if args.start is not False:
        os.system('git init')
        
        if args.url is not None:
            os.system('git remote add origin ' + args.url)
            os.system('git pull origin main')
            os.system('git checkout main')
        else: 
            raise( ValueError("missing url"))
    
    elif args.push is not False:
        
        if args.files is None:
            print("Every change will be pushed")
            os.system('git add .')

        else:
            for file in args.files:
                os.system('git add ' + file)
        
        os.system('git commit -m "automated commit')
        os.system ('git push origin main')
        



if __name__ == '__main__':
    args = parse()
    execute(args)

