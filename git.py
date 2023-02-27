import os
import argparse


def parse():
    argParser = argparse.ArgumentParser()
    argParser.add_argument("-s", "--start", action="store_true", help="initialize remote repository")
    argParser.add_argument("-u", "--url", help="repository URL")
    argParser.add_argument("-p", "--push", action="store_true", help="push to the repository if no arguments selected everything is pushed")
    argParser.add_argument("-f", "--files",'--nargs', nargs='+', help="file list to push")
    argParser.add_argument("-b", "--back", help="change back given number of versions", type=int)
    argParser.add_argument("-r", "--reset", action="store_true", help="resets to current version")




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
        
        print(args.files)

        if args.files is None:
            print("Every change will be pushed")
            os.system('git add .')

        else:
            for file in args.files:
                os.system('git add ' + file)
        
        os.system('git commit -m "automated commit')
        os.system ('git push origin main')
    
    elif args.back is not None:
        print('Reverting back ' + str(args.back) + ' versions')
        os.system('git checkout HEAD~' + str(args.back))

    elif args.reset is not False:
        print("resetting to current version")       
        os.system('git checkout main') 



if __name__ == '__main__':
    args = parse()
    execute(args)

