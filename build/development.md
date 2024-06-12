### 开发

新建文件钩子文件

用于提交时更新**examples.txt**，从而更新列表以及预览图。

[.git/hooks/pre-commit](.git/hooks/pre-commit)

```shell
#!/bin/sh

# 复制文件进入文件夹
ls -R  *.html > examples.txt
git add examples.txt
```

新建示例文件
```shell
echo '' > "058.tesseract.js 文字识别.html"
# 或者
python .\build\new.py 思绪万千
```

#### 示例截图

执行以下命令之前需要配置

- conda
- vscode 
    - Live Server
        - 目前我配置是6600端口，可根据自己端口进行修改index.py。

启用 Live Server 后再进行生成示例图片。

```shell
# 切换文件夹
cd build
# 使用conda新建环境
conda create --name h5-build-310 python==3.10
# 切换环境
conda activate h5-build-310
# 安装依赖
pip install -r requirements.txt -i https://pypi.douban.com/simple/
# 生成截图，但是有些截图可能存在问题，将其删除重新执行python index.py即可
python index.py
```
