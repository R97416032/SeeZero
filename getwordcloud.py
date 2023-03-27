import jieba
import re
import wordcloud
def generatePic(path,name):
    with open(path+name+".txt", encoding="utf-8") as f:
        s = f.read()
    print(s)
    ls = re.split('[,;]', s)  # 生成分词列表
    text = ' '.join(ls)  # 连接成字符串
    print(text)
    stopwords = ["的","是","了"] # 去掉不需要显示的词

    wc = wordcloud.WordCloud(font_path="msyh.ttc",
                             width=1000,
                             height=700,
                             background_color='white',
                             max_words=100, stopwords=stopwords)
    # msyh.ttc电脑本地字体，写可以写成绝对路径
    wc.generate(text)  # 加载词云文本
    wc.to_file("pic/"+name+".png")  # 保存词云文件
    # 读取文本
    with open(path+name+"ch.txt", encoding="utf-8") as f:
        s = f.read()
    print(s)
    ls = jieba.lcut(s)  # 生成分词列表
    text = ' '.join(ls)  # 连接成字符串
    print(text)
    wc.generate(text)  # 加载词云文本
    wc.to_file("pic/"+name+"ch.png")  # 保存词云文件
generatePic("zerogenesdetails/Oligodendrocytes/","OBP")
generatePic("zerogenesdetails/Oligodendrocytes/","OMF")
generatePic("zerogenesdetails/Neural Stem/","NBP")
generatePic("zerogenesdetails/Neural Stem/","NMF")