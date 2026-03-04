## Pocketmine-Builder-Lite (Lite.py)
## UPDATE: Linux Support Added
# Important ⚠️
U need to get Composer [https://getcomposer.org/](https://getcomposer.org/), since composer is needed to build the phar
# - New Features: AutoDetecting
# Using it:
- you put the Bin (php Library used for Pocketmine) in the folder Lite.py is used
- Download any Pocketmine (Fork) from github, which you want to build
- move the zip into the Folder and unpack it there
- start Lite.py by CMD
- It will search the Folder for Pocketmine Source Folders, if found one, it will use it, if null are found, it will exit and if more than one is found, it will ask you to choose which to Build :)

Have Fun using it, and no pain Building Pocketmine by source again, (ALSO SETS DEVELOPERMODE TO FALSE BY DEFAULT!!!

(I Recommend using Lite.py)




## Pocketmine-Builder

just drop the Pocketmine-MP folder with source in the folder with this Programm or just start it and use one of its 2 preset options
1 => Pocketmine from PMMP
2 => NetherGamesMC PocketMineMP with build in Multiversion

else just drop the Pocketmine-MP (or PocketMine-MP-stable) folder in the same folder this programm is located in

Requires Composer
When Pocketmine src is downloaded as ZIP file and is different to PocketMine-MP, rename it to PocketMine-MP

(Caution: this tool sets automatically IS_DEVELOPMENT_BUILD to false)
(with the drop and play you could basically build your own coded pmmp version too :D)
(It is recommended to copy the bin folder from your pocketmine server folder (the windows one) also to the folder this programm is located, this will make sure the programm wont run into bugs)
(when Composer asks for a Github AuthO key, put it in and rerun this code in an new opened cmd window)
(Currently only Windows Supported)
