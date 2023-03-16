# 导入必要的库
import wordcloud
import matplotlib.pyplot as plt

# 定义词库
#words = "物联网 大数据 人工智能 万物互联 操作系统 数据库 计算机 编程 网络协议栈 无线通信 蓝牙 传感器"
words = "碳中和 碳达峰 碳交易 碳排放权 碳价 碳税 碳汇 碳足迹 CCUS ESG IPCC 巴黎协定 二氧化碳当量 循环经济 碳捕获技术 碳配额 3060目标 清洁发展机制 温室气体 全球气候变暖 国家自主贡献"

# 生成词云图片
wc = wordcloud.WordCloud(font_path='SmileySans-Oblique.ttf', width=800, height=600, background_color='white')
wc.generate_from_text(words)
wc.to_file('wordcloud.png')

# 显示词云图片
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.show()
