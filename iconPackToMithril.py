import glob
import errno

#Path to write the mithrilfile
fileWrite_Path = './scripts/drawModule/mithrilIcons.js'
#sets the source path
image_path = './images/iconpack/*.png'
files = glob.glob(image_path)
spacer = '     '
quadSpacer = spacer + spacer + spacer + spacer
nameList = ""
# writes the header
nameList += 'const iconTools =' + '\n'
nameList += '{' + '\n'
nameList += spacer + 'view: function()' + '\n' 
nameList += spacer + '{' + '\n'
nameList += spacer + spacer + 'return m("div",' + '\n'
nameList += spacer + spacer + '{"id":"icontools"},'+ '\n'
nameList += spacer + spacer + '['+ '\n'
nameList += spacer + spacer + spacer + 'm("div",' + '\n' 
nameList += spacer + spacer + spacer + '{"id":"iconContainer"}, ' + '\n'
nameList += spacer + spacer + spacer + '[' + '\n'
    
#runs through all the images in iconpack and writes them to a mithrilformated JS file.
for name in files:
    try:
       
        currentName = name.split('\\',1)[1]
        currentName = currentName.split('.png', 1)[0]
        nameOutput = ""
        nameOutput += quadSpacer + 'm("img",' + '\n'
        nameOutput += quadSpacer + '{' + '\n'
        nameOutput += quadSpacer + spacer + '"src":"images/iconpack/' + currentName + '.png",' + '\n'
        nameOutput += quadSpacer + spacer + '"class":"drawIcons",' + '\n'
        nameOutput += quadSpacer + spacer + '"id":"markerIcon-' + currentName + '",' + '\n'
        nameOutput += quadSpacer + spacer + '"title":"' + currentName + '",' + '\n'
        nameOutput += quadSpacer + spacer + 'onclick: (e) =>' + '\n' 
        nameOutput += quadSpacer + spacer + '{markerIcons_click(e)}' + '\n'
        nameOutput += quadSpacer +'}),' + '\n'
        nameList += nameOutput
    except IOError as exc:
        print(exc)
#adds bracket and spaceing.
nameList += spacer + spacer + spacer + '])' + '\n'
nameList += spacer + spacer + '])' + '\n'
nameList += spacer + '}' + '\n'
nameList += '}'

writeToFile = open(fileWrite_Path,'w')
writeToFile.write(nameList)
writeToFile.close()