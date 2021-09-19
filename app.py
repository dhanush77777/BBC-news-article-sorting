from flask import Flask,request,render_template,url_for
import pickle
clf=pickle.load(open('nlp_model1.pkl','rb'))
cv=pickle.load(open('transform1.pkl','rb'))
import requests      
  
api_key="706c4dbcb4ac484a9c9c2488add37812"

app=Flask(__name__)

@app.route('/')
def home():
    
    return render_template('home.html')


main_url="https://newsapi.org/v2/top-headlines?country=in&category=sport&apiKey="+api_key
main_url1="https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey="+api_key
main_url2="https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey="+api_key
main_url3="https://newsapi.org/v2/top-headlines?country=in&category=politics&apiKey="+api_key
main_url4="https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey="+api_key

news=requests.get(main_url).json()
news1=requests.get(main_url1).json()
news2=requests.get(main_url2).json()
news3=requests.get(main_url3).json()
news4=requests.get(main_url4).json()

article=news["articles"]
article1=news1["articles"]
article2=news2["articles"]
article3=news3["articles"]
article4=news4["articles"]
    
news_article=[]
img=[]
n=[]
m=[]
for arti in article:
    news_article.append(arti['title'])
    img.append(arti['url'])
        #print(news_article)
for i in range(5):
    n.append(news_article[i])
    m.append(img[i])
    
    
news_article1=[]
img1=[]
n1=[]
m1=[]
for arti1 in article1:
    news_article1.append(arti1['title'])
    img1.append(arti1['url'])
        #print(news_article)
for i1 in range(5):
    n1.append(news_article1[i1])
    m1.append(img1[i1])

news_article2=[]
img2=[]
n2=[]
m2=[]
for arti2 in article2:
    news_article2.append(arti2['title'])
    img2.append(arti2['url'])
        #print(news_article)
for i2 in range(5):
    n2.append(news_article2[i2])
    m2.append(img2[i2])


news_article3=[]
n3=[]
img3=[]
m3=[]
for arti3 in article3:
    news_article3.append(arti3['title'])
    img3.append(arti3['url'])
        #print(news_article)
for i3 in range(5):
    n3.append(news_article3[i3])
    m3.append(img3[i3])


news_article4=[]
n4=[]
img4=[]
m4=[]
for arti4 in article4:
    news_article4.append(arti4['title'])
    img4.append(arti4['url'])
        #print(news_article)
for i4 in range(5):
    n4.append(news_article4[i4])    
    m4.append(img4[i4])

s,a=str(n[0]),str(m[0])
st,b=str(n[1]),str(m[1])
st1,c=str(n[2]),str(m[2])
st2,d=str(n[3]),str(m[3])
st3,e=str(n[4]),str(m[4])

s1,a1=str(n1[0]),str(m1[0])
st1,b1=str(n1[1]),str(m1[1])
st11,c1=str(n1[2]),str(m1[2])
st21,d1=str(n1[3]),str(m1[3])
st31,e1=str(n1[4]),str(m1[4])


s2,a2=str(n2[0]),str(m2[0])
st2,b2=str(n2[1]),str(m2[1])
st12,c2=str(n2[2]),str(m2[2])
st22,d2=str(n2[3]),str(m2[3])
st32,e2=str(n2[4]),str(m2[4])

s3,a3=str(n3[0]),str(m3[0])
st3,b3=str(n3[1]),str(m3[1])
st13,c3=str(n3[2]),str(m3[2])
st23,d3=str(n3[3]),str(m3[3])
st33,e3=str(n3[4]),str(m3[4])


s4,a4=str(n4[0]),str(m4[0])
st4,b4=str(n4[1]),str(m4[1])
st14,c4=str(n4[2]),str(m4[2])
st24,d4=str(n4[3]),str(m4[3])
st34,e4=str(n4[4]),str(m4[4])
    

@app.route('/predict',methods=['POST'])
def predict():
    
    
    
    
    if request.method=='POST':
        message=request.form['message']
        data=[message]
        vect=cv.transform(data).toarray()
        my=clf.predict(vect)
        
    
    if my == ['business']:
        return render_template("business1.html",pre=s1,pre1=st1,pre2=st11,pre3=st21,pre4=st31,r=a1,r1=b1,r2=c1,r3=d1,r4=e1)
    elif my == ['tech']:
        return render_template("tech1.html",pre=s2,pre1=st2,pre2=st12,pre3=st22,pre4=st32,r=a2,r1=b2,r2=c2,r3=d2,r4=e2)
    elif my == ['politics']:
        return render_template("politics1.html",pre=s3,pre1=st3,pre2=st13,pre3=st23,pre4=st33,r=a3,r1=b3,r2=c3,r3=d3,r4=e3)
    elif my == ['sport']:
        return render_template("sport1.html",pre=s,pre1=st,pre2=st1,pre3=st2,pre4=st3,r=a,r1=b,r2=c,r3=d,r4=e)
    else:
        return render_template("entertainment1.html",pre=s4,pre1=st4,pre2=st14,pre3=st24,r=a4,r1=b4,r2=c4,r3=d4,r4=e4)



if __name__=='__main__':
    app.run(debug=True)

