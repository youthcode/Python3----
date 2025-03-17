from lxml import etree

text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html"><span>first item</span></a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>
'''
html = etree.HTML(text)
result = html.xpath('//li[1]/ancestor::*')
# print(result)
result = html.xpath('//li[1]/ancestor::div')
# print(result)
result = html.xpath('//li[1]/attribute::*')
# print(result)
result = html.xpath('//li[1]/child::a[@href="link1.html"]')
# print(result)
result = html.xpath('//li[1]/descendant::span')
# print(result)
result = html.xpath('//li[1]/following::*[2]')
# print(result)
result = html.xpath('//li[1]/following-sibling::*')
print(result)
#




# from lxml import etree
# text = '''
# <div>
#     <ul>
#          <li class="item-0"><a href="link1.html">first item</a></li>
#          <li class="item-1"><a href="link2.html">second item</a></li>
#          <li class="item-inactive"><a href="link3.html">third item</a></li>
#          <li class="item-1"><a href="link4.html">fourth item</a></li>
#          <li class="item-0"><a href="link5.html">fifth item</a>
#      </ul>
#  </div>
# '''
# html = etree.HTML(text)
# result = html.xpath('//li[1]/a/text()')
# print(result)
# result = html.xpath('//li[last()]/a/text()')
# print(result)
# result = html.xpath('//li[position()<3]/a/text()')
# print(result)
# result = html.xpath('//li[last()-2]/a/text()')
# print(result)
#




# from lxml import etree
# text = '''
# <li class="li li-first" name="item"><a href="link.html">first item</a></li>
# '''
# html = etree.HTML(text)
# result = html.xpath('//li[contains(@class, "li") and @name="item"]/a/text()')
# print(result)





# from lxml import etree
# text = '''
# <li class="li li-first"><a href="link.html">first item</a></li>
# '''
# html = etree.HTML(text)
# result = html.xpath('//li[contains(@class, "li")]/a/text()')
# print(result)





# from lxml import etree
# text = '''
# <li class="li li-first"><a href="link.html">first item</a></li>
# '''
# html = etree.HTML(text)
# result = html.xpath('//li[@class="li"]/a/text()')
# print(result)




# from lxml import etree

# html = etree.parse('./test.html', etree.HTMLParser())
# result = html.xpath('//li/a/@href')
# print(result)





# from lxml import etree

# html = etree.parse('./test.html', etree.HTMLParser())
# result = html.xpath('//li[@class="item-0"]//text()')
# print(result)





# from lxml import etree

# html = etree.parse('./test.html', etree.HTMLParser())
# result = html.xpath('//li[@class="item-0"]/a/text()')
# print(result)





# from lxml import etree

# html = etree.parse('./test.html', etree.HTMLParser())
# result = html.xpath('//li[@class="item-0"]/text()')
# print(result)





# from lxml import etree
# html = etree.parse('./test.html', etree.HTMLParser())
# result = html.xpath('//li[@class="item-0"]')
# print(result)





# from lxml import etree
# html = etree.parse('./test.html', etree.HTMLParser())
# result = html.xpath('//a[@href="link4.html"]/../@class')
# print(result)





# from lxml import etree

# html = etree.parse('./test.html', etree.HTMLParser())
# result = html.xpath('//a[@href="link4.html"]/../@class')
# print(result)





# from lxml import etree

# html = etree.parse('./test.html', etree.HTMLParser())
# result = html.xpath('//ul//a')
# print(result)





# from lxml import etree

# html = etree.parse('./test.html', etree.HTMLParser())
# result = html.xpath('//li/a')
# print(result)





# from lxml import etree
# html = etree.parse('./test.html', etree.HTMLParser())
# result = html.xpath('//li')
# print(result)
# print(result[0])





# from lxml import etree
# html = etree.parse('./test.html', etree.HTMLParser())
# result = html.xpath('//*')
# print(result)





# from lxml import etree

# html = etree.parse('./test.html', etree.HTMLParser())
# result = etree.tostring(html)
# print(result.decode('utf-8'))





# from lxml import etree
# text = '''
# <div>
#     <ul>
#          <li class="item-0"><a href="link1.html">first item</a></li>
#          <li class="item-1"><a href="link2.html">second item</a></li>
#          <li class="item-inactive"><a href="link3.html">third item</a></li>
#          <li class="item-1"><a href="link4.html">fourth item</a></li>
#          <li class="item-0"><a href="link5.html">fifth item</a>
#      </ul>
#  </div>
# '''
# html = etree.HTML(text)
# result = etree.tostring(html)
# print(result.decode('utf-8'))