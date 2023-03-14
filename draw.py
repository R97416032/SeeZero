import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# 解决中文标题乱码的问题
sns.set_style('whitegrid', {'font.sans-serif': ['simhei', 'FangSong']})

# 显示每个类别有多少细胞
f = open("data/eachnum.txt", "r")
nums = f.read().splitlines()
f.close()
nums = [int(i) for i in nums[1:]]

# 将类别对应为真实类别名，并更新图像数据
f = open("clustername.txt", "r")

types = f.read().splitlines()
types = types[1:]
f.close()
clasterdata = {
    "type": types,
    "quantity": nums
}
clasterdata = pd.DataFrame(clasterdata)
plt.figure(figsize = [20,10],dpi=100)
ax = sns.barplot(data=clasterdata, y="quantity", x="type")
ax.bar_label(ax.containers[0])
ax.set_xticklabels(labels=types,rotation = 45)
ax.set_title("每个类别的细胞数量图")
plt.savefig("pic/01每个类别的细胞数量图.jpg")
plt.close()

# 显示每个类别有多少零表达基因
f = open("data/nzeroineach.txt", "r")
zerogenenums = f.read().splitlines()
f.close()
zerogenenums = [int(i) for i in zerogenenums[1:]]
zerogenedata = {
    "type": types,
    "zerogene-quantity": zerogenenums
}
zerogenedata = pd.DataFrame(zerogenedata)
plt.figure(figsize = [20,10],dpi=100)
ax = sns.barplot(data=zerogenedata, y="zerogene-quantity", x="type")
ax.bar_label(ax.containers[0])
ax.set_xticklabels(labels=types,rotation = 45)
ax.set_title("每个类别零表达基因数量图")
plt.savefig("pic/02每个类别零表达基因数量图.jpg")
plt.close()

# 显示每个类别中独有的零表达基因数
f = open("data/unique/nuniquezeroineach.txt", "r")
unique_zerogenenums = f.read().splitlines()
f.close()
unique_zerogenenums = [int(i) for i in unique_zerogenenums[1:]]
zerogenedata = {
    "type": types,
    "unique-zerogene-quantity": unique_zerogenenums
}
zerogenedata = pd.DataFrame(zerogenedata)
plt.figure(figsize = [20,10],dpi=100)
ax = sns.barplot(data=zerogenedata, y="unique-zerogene-quantity", x="type")
ax.bar_label(ax.containers[0])
ax.set_xticklabels(labels=types,rotation = 45)
ax.set_title("每个类别独有的零表达基因数量图")
plt.savefig("pic/03每个类别独有的零表达基因数量图.jpg")
plt.close()

# 过滤掉在90%细胞中都不表达的基因后每个类别中的零表达基因数目
f = open("data90/nzeroineach.txt")
zerogenenums_90 = f.read().splitlines()
f.close()
zerogenenums_90 = [int(i) for i in zerogenenums_90[1:]]
zerogenedata_90 = {
    "type": types,
    "zerogene-quantity-90": zerogenenums_90
}
zerogenedata_90 = pd.DataFrame(zerogenedata_90)
plt.figure(figsize = [20,10],dpi=100)
ax = sns.barplot(data=zerogenedata_90, y="zerogene-quantity-90", x="type")
ax.bar_label(ax.containers[0])
ax.set_xticklabels(labels=types,rotation = 45)
ax.set_title("每个类别中零表达基因数（90%）")
plt.savefig("pic/04每个类别中零表达基因数（90%）.jpg")
plt.close()

# 过滤掉在90%细胞中都不表达的基因后每个类别中独有的零表达基因数目
f = open("data90/unique/nuniquezeroineach.txt")
unique_zerogenenums_90 = f.read().splitlines()
f.close()
unique_zerogenenums_90 = [int(i) for i in unique_zerogenenums_90[1:]]
unique_zerogenedata_90 = {
    "type": types,
    "unique-zerogene-quantity-90": unique_zerogenenums_90
}
unique_zerogenedata_90 = pd.DataFrame(unique_zerogenedata_90)
plt.figure(figsize = [20,10],dpi=100)
ax = sns.barplot(data=unique_zerogenedata_90, y="unique-zerogene-quantity-90", x="type")
ax.bar_label(ax.containers[0])
ax.set_xticklabels(labels=types,rotation = 45)
ax.set_title("每个类别中独有零表达基因数（90%）")
plt.savefig("pic/05每个类别中独有的零表达基因数（90%）.jpg")
plt.close()
