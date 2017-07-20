from lxml import etree

broken_html = "<html><head><title>test<body><h1>page title</h3>"

tree = etree.HTML(broken_html)
result = etree.tostring(tree, pretty_print=True, method="html")

print result


html = """
    <html>
        <head>
            <title>test</title>
        </head>
        <body>
            <h1>page title</h1>

            <h2>One</h2>
            <h2 class="valid">Two</h2>
            <h2 class="not-valid">Free</h2>
            <h2 class="valid">Four</h2>
        </body>
    </html>
"""

tree = etree.HTML(html)



for el in tree.find('body').iter('h2'):
    if el.attrib.get('class') == "valid":
        print el.tag, el.text


els = tree.xpath('/html/body/h2')
print len(els), els[0].text

els = tree.xpath('/html/body/h2[@class][1]/@class')
print len(els), els

els = tree.xpath('//h2')
print len(els), els

els = tree.xpath('/html/body/h2[@class = "valid"][1]/@class')
print len(els), els

