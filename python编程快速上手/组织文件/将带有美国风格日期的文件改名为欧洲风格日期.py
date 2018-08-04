# 假定你的老板用电子邮件发给你上千个文件，文件名包含美国风格的日期
# （MM-DD-YYYY），需要将它们改名为欧洲风格的日期（DD-MM-YYYY）。手工完
# 成这个无聊的任务可能需要几天时间！让我们写一个程序来完成它。
# 下面是程序要做的事：
# • 检查当前工作目录的所有文件名，寻找美国风格的日期。
# • 如果找到，将该文件改名，交换月份和日期的位置，使之成为欧洲风格。

import shutil, os, re
# TODO:Create a regex that matches files with the American date format.
datePattern = re.compile(r"""^(.*?) # all text before the date
    ((0|1)?\d)- # one or two digits for the month
    ((0|1|2|3)?\d)- # one or two digits for the day
    ((19|20)\d\d) # four digits for the year
    (.*?)$ # all text after the date
    """, re.VERBOSE)
# TODO: Loop over the files in the working directory.
for amerFilename in os.listdir('.'):
    # print(filenames)
    mo = datePattern.search(amerFilename)
    # TODO: Skip files without a date.
    if mo == None:
        continue
    # TODO: Get the different parts of the filename.
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)
    # TODO: Form the European-style filename.
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart +afterPart
    # TODO: Get the full, absolute file paths.
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)
    # TODO: Rename the files.
    print('Renaming "%s" to "%s"...' % (amerFilename, euroFilename))
    shutil.move(amerFilename, euroFilename) # uncomment after testing
