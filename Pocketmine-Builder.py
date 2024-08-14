import os
import glob
import subprocess as sp
os.system("color b")
print("Thx for using DemonicEagle143's PocketMine-MP Builder <3 \n")
print("We kindly recommend to use the bin you are using for your pocketmine server :D, just copy it here\n")
print("It might be that composer needs a new api key, then you need to restart the cmd after entering the new api key")

nat_path = os.getcwd();
def hasPHP():
    try:
        sp.check_call(['php', '-v'])
        return True
    except:
        return False
    
def update_php_file(file_path):
    # Read the file content
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Update the specific line
    with open(file_path, 'w') as file:
        for line in lines:
            if 'public const IS_DEVELOPMENT_BUILD' in line:
                # Check if the line contains 'true' and change it to 'false'
                if 'true' in line:
                    line = line.replace('true', 'false')
            file.write(line)
   
def Build(var):
    php_file_path = nat_path + f"\{var}\src\VersionInfo.php"
    update_php_file(php_file_path)
    print(f"Updated {php_file_path} to DEVELOPMENT_BUILD = false") 
    #
    result = sp.run("where composer", capture_output=True, text=True, shell=True)
    composer_paths = result.stdout.strip().split('\n')
    composer_path = composer_paths[0]
    composercmd = f"{php} {composer_path}.phar install --working-dir={var} --no-dev --classmap-authoritative"
    os.system(composercmd)
    composercmd2 = f"{php} {composer_path}.phar make-server --working-dir={var}"
    os.system(composercmd2)
    bp = "output\\PocketMine-MP.phar"
    ccmd = "copy" + " " + var + "\\PocketMine-MP.phar " + bp
    os.system(ccmd)
def prepare():
    print("\nWhich Pocketmine Lib you want to build?")
    print("1 => PMMP\PocketMine-MP")
    print("2 => NetherGamesMC\PocketMine-MP [MultiProtocol]")
    x = input("=> ")
    print(x)
    if(x == "1"):
        os.system("git clone https://github.com/pmmp/PocketMine-MP.git")
    elif(x == "2"):
        os.system("git clone https://github.com/NetherGamesMC/PocketMine-MP.git")
    else:
        exit("Custom will be added")
    Build("PocketMine-MP")
    
if(os.path.isdir("output") == False):
    os.mkdir("output")
    print("generating Folder called 'output'")    
if(os.path.isdir("bin")):
    print("We are going to use the bin folder as PHP source")
    php = "bin\php\php.exe"
elif(hasPHP()):
    print("since there is no folder called 'bin', we are using the installed PHP version")
    php = "php"
else:
    print("No PHP installed and No Directonary called 'bin' found")
    print("to use this code pls install PHP or copy the bin Folder by Pocketmine into this Folder")
    exit("Exit: 'NO PHP FOUND'")
if(os.path.isdir("PocketMine-MP-stable")):
    Build("PocketMine-MP-stable")
elif(os.path.isdir("PocketMine-MP")):
    Build("PocketMine-MP")
else:
    prepare()
exit("end of code")    
if(os.path.isdir("PocketMine-MP-stable")):
    virions = glob.glob("virions/*.phar")
    print(len(virions), "Virions Detected:")
    if(len(virions) == 0):
        exit("There are no virions to inject")
    for i in virions:
        print("===> ", i)
    if(os.path.isdir("plugins")):
        plugins = glob.glob("plugins/*.phar")
        print(len(plugins), "Plugins Detected:")
        if (len(plugins) == 0):
            exit("There are no plugins to be injected")
        elif(len(plugins) > 1):
            print("There are more then 1 Plugins in the Plugin Folder")
            x = input("Should We inject all Virions into Every Plugin? Y/[N]")
            if(x != "Y"):
                exit("If u want to inject the virions to only one Plugin, pls remove the other Plugins from the Plugins_folder")
        for p in plugins:
            print("")
            print("===> ", p)
            ap = p.replace("plugins", "")
            bp = "output" + ap
            ccmd = "copy" + " " + p + " " + bp
            os.system(ccmd)
            print("")
            print("")
            for v in virions:
                print("===> ","Injecting", v, "into", p)
                cmd = php + " -dphar.readonly=0 " + v + " " + bp
                os.system(cmd)
    else:
        os.mkdir("plugins")
        exit("Error: Folder 'plugins' not Found")
else:
    os.mkdir("virions")
    if (os.path.isdir("plugins") == False):
        os.mkdir("plugins")
    exit("Error: Folder 'virions' not Found")
print("")
print("finnished Injecting")