# 导入必要的库
import wordcloud
import jieba
import matplotlib.pyplot as plt

# 读入文本文件
with open('text.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# 中文分词
words = jieba.cut(text)

# 计算词频
freq = {}
for word in words:
    if len(word) > 1:
        freq[word] = freq.get(word, 0) + 1

# 生成词云图片
wc = wordcloud.WordCloud(font_path='SmileySans-Oblique.ttf', width=800, height=600, background_color='white')
wc.generate_from_frequencies(freq)
wc.to_file('wordcloud.png')

# 显示词云图片
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.show()