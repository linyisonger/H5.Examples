# 自动编号
import os
import shutil
import sys
if __name__ == '__main__':
    args = sys.argv[1:]

    index = 1
    useNumList = []

    for file in os.listdir(os.getcwd()):
        if file.endswith(".html"):
            if file.split(".")[0].isdigit():
                useNumList.append(int(file.split(".")[0]))
    
    while index in useNumList:
        index+=1
    
    index = f'{index}'.zfill(3)
    newFileName =f'{index}.{args[0]}.html' 
    shutil.copy(os.path.join(os.getcwd(), 'build', 'template.html'),os.path.join(os.getcwd(), newFileName))
    
    print('新建文件成功', newFileName)