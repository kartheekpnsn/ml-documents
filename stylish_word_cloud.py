# make worldcloud
from wordcloud import WordCloud, ImageColorGenerator
from PIL import Image

# getting tokens
texts = " ".join(token for token in corpus)
# setting stopwords
stopwords_wc = set(stopwords)
# loading custom font
font_path = "../input/wcloud/acetone_font.otf"

# generating wordcloud
wordcloud = WordCloud(stopwords=stopwords_wc, font_path=font_path,
                      max_words=1500,
                      max_font_size=350, random_state=42,
                      width=2000, height=1000,
                      colormap = "gist_stern")
wordcloud.generate(texts)

# plotting
plt.figure(figsize = (24, 13))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
