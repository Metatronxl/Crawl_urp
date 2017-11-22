# Crawl_urp
利用URP漏洞进行学生数据获取



---
## URP漏洞简介

> 首先登陆

```
http://zhjw.scu.edu.cn/loginAction.do

```
> 获取网站cookie

```
http://www.xxx.com/reportFiles/cj/cj_zwcjd.jsp

```
> 访问这个页面，输入学生学号就可以看到信息

---
## Environment

> python2.7
>
> iTerm2
>
> 第三方包详情参考requirements.txt

---
## 吐槽
```
整个网页就是一个表格，并且几乎没有使用class或者id进行区分，整理数据非常麻烦，
等哪天有心情了再一个个数据分开扣吧，暂且就这样了，23333
```




