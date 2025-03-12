import unittest
from markdown_to_html_node import markdown_to_html_node

class TestMarkdownToHTMLNode(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
            html,
        )

    def test_heading_1(self):
        md = """
# Heading
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        control = "<div><h1>Heading</h1></div>"
        self.assertEqual(control, html)

    def test_heading_2(self):
        md = """
## Heading
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        control = "<div><h2>Heading</h2></div>"
        self.assertEqual(control, html)

    def test_heading_3(self):
        md = """
### Heading
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        control = "<div><h3>Heading</h3></div>"
        self.assertEqual(control, html)

    def test_heading_4(self):
        md = """
#### Heading
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        control = "<div><h4>Heading</h4></div>"
        self.assertEqual(control, html)

    def test_heading_5(self):
        md = """
##### Heading
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        control = "<div><h5>Heading</h5></div>"
        self.assertEqual(control, html)

    def test_heading_6(self):
        md = """
###### Heading
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        control = "<div><h6>Heading</h6></div>"
        self.assertEqual(control, html)

    def test_heading_invalid_1(self):
        md = """
####### Heading
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        control = "<div><p>####### Heading</p></div>"
        self.assertEqual(control, html)

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
            html,
        )

    def test_quote_1(self):
        md = """
>This
>is
>a
>quote!
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            "<div><blockquote>This\nis\na\nquote!</blockquote></div>",
            html
        )

    def test_unordered_list_1(self):
        md = """
- This
- is
not
- an
- unordered
- list!
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            "<div><p>- This - is not - an - unordered - list!</p></div>",
            html
        )

    def test_ordered_list_1(self):
        md = """
1. This
2. is
3. an
4. ordered
5. list!
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            "<div><ol><li>This</li><li>is</li><li>an</li><li>ordered</li><li>list!</li></ol></div>",
            html
        )

    def test_ordered_list_invalid_1(self):
        md = """
1. This
2. is
9. not
3. an
4. ordered
5. list!
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            "<div><p>1. This 2. is 9. not 3. an 4. ordered 5. list!</p></div>",
            html
        )

    def test_many_multiblocks_1(self):
        md = """
# First heading

## Second heading

Paragraph
of
some _italic_ **bold** `code`
text
and ![image](path/to/image/img.png)
and [link](https://www.example.co.uk)

- Unordered
- list **bold**
- for _italic_
- fun `code`
- image ![image 2](path/no/fun/img2.jpg)
- link [link 2](www.someaddresoranother.com)
- [link 2](www.someaddresoranother.com)

1. Ordered
2. list **bold**
3. for _italic_
4. fun `code`
5. image ![image 3](path/no/fun/img2.jpg)
6. link [link 3](www.someaddresoranother.com)

>Now
>quote **bold**
>for _italic_
>grief `code`
>image ![image 4](path/no/fun/img2.jpg)
>link [link 4](www.someaddresoranother.com)

```
Now
code **bold**
for _italic_
grief `code`
image ![image 4](path/no/fun/img2.jpg)
link [link 4](www.someaddresoranother.com)```
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            """<div><h1>First heading</h1><h2>Second heading</h2><p>Paragraph of some <i>italic</i> <b>bold</b> <code>code</code> text and <img src="path/to/image/img.png" alt="image"> and <a href="https://www.example.co.uk">link</a></p><ul><li>Unordered</li><li>list <b>bold</b></li><li>for <i>italic</i></li><li>fun <code>code</code></li><li>image <img src="path/no/fun/img2.jpg" alt="image 2"></li><li>link <a href="www.someaddresoranother.com">link 2</a></li><li><a href="www.someaddresoranother.com">link 2</a></li></ul><ol><li>Ordered</li><li>list <b>bold</b></li><li>for <i>italic</i></li><li>fun <code>code</code></li><li>image <img src="path/no/fun/img2.jpg" alt="image 3"></li><li>link <a href="www.someaddresoranother.com">link 3</a></li></ol><blockquote>Now\nquote <b>bold</b>\nfor <i>italic</i>\ngrief <code>code</code>\nimage <img src="path/no/fun/img2.jpg" alt="image 4">\nlink <a href="www.someaddresoranother.com">link 4</a></blockquote><pre><code>Now\ncode **bold**\nfor _italic_\ngrief `code`\nimage ![image 4](path/no/fun/img2.jpg)\nlink [link 4](www.someaddresoranother.com)</code></pre></div>""",
            html
        )
