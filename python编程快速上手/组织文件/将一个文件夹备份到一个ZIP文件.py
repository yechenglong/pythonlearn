# 假定你正在做一个项目，它的文件保存在C:\AlsPythonBook 文件夹中。你担心工作
# 会丢失，所以希望为整个文件夹创建一个ZIP 文件，作为“快照”。你希望保存不同的版
# 本，希望ZIP 文件的文件名每次创建时都有所变化。例如AlsPythonBook_1.zip、
# AlsPythonBook_2.zip、AlsPythonBook_3.zip，等等。你可以手工完成，但这有点烦人，
# 而且可能不小心弄错ZIP 文件的编号。运行一个程序来完成这个烦人的任务会简单得多。
# 针对这个项目，打开一个新的文件编辑器窗口，将它保存为backupToZip.py。
import zipfile,re,os
def backupToZip(folder):
    # TODO:Backup the entire contents of "folder" into a ZIP file.
    folder = os.path.abspath(folder) # make sure folder is absolute
    print(folder)
    # TODO:Figure out the filename this code should use based on
    number = 1
    while True:
        zipfileName = os.path.basename(folder) + '_' + str(number) + '.zip'
        print(zipfileName)
        # TODO:what files already exist.
        if not os.path.exists(zipfileName):
            break
        number += 1

    # TODO: Create the ZIP file.
    print("Creating %s ... "% zipfileName)
    backupZip = zipfile.ZipFile(zipfileName,'w')
    # TODO: Walk the entire folder tree and compress the files in each folder.
    for folderName,subfolders,fileNames in os.walk(folder):
        print('Adding files in %s...' % (folderName))
        # Add the current folder to the ZIP file.
        backupZip.write(folderName)
        # Add all the files in this folder to the ZIP file.
        for fileName in fileNames:
            print('Adding files in %s...' % (fileName))
            newBase = os.path.basename(folder) + '_'
            if fileName.startswith(newBase) and fileName.endswith(".zip"):
                continue
            backupZip.write(os.path.join(folderName,fileName))
    backupZip.close()


backupToZip('.')
