# 导入必要的库
import wordcloud
import matplotlib.pyplot as plt

# 定义词库
words = "Python C/C++ Javascript Java PHP SQL Rust Golang MATLAB R Ruby Swift Lua"

# 生成词云图片
wc = wordcloud.WordCloud(width=800, height=600, background_color='white')
wc.generate_from_text(words)
wc.to_file('wordcloud.png')

# 显示词云图片
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.show()
