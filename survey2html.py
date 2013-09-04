from __future__ import print_function, division
import pickle


def header():
    print('''

    <html>
    <head>
    <link rel="stylesheet" href="aspp.css" type="text/css" media="screen"/>
    </head>

    <body>
    ''')


def bar3(left_labels, right_labels, values3):
    print('<table>')

    for n, (left, vals, right) in enumerate(zip(left_labels, values3, right_labels)):
        print('<tr>')
        if left:
            print('<td class="left-label">%s</td>' % left)

        print('<td>')
        bar(vals)
        print('</td>')

        if right:
            print('<td class="right-label">%s</td>' % right)

        print('</tr>')


def bar(values):
    print('<div class="bar">')
    for n, v in enumerate(values):
        if v == 0:
            continue
        print(('<div class="block%d">&nbsp;</div>' % n) * v)
    print('</div>')


def footer():
    print('</body></html>')


if __name__ == "__main__":
    left_labels = ('Level', 'Interest', 'Materials')
    right_label = ('Tiziano Zito', 'Introduction', 'Day0')
    values3 = ((5, 10, 15), (0, 20, 10), (20, 5, 3))

    header()
    bar3(left_labels, right_label, values3)
    footer()
