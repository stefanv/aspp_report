bar_width = 15 # in pixels
bar_height = 15
blocks_per_row = 30
table_width = 700


def template(fn, data):
    import tempita

    with open(fn.replace('.tmpl', ''), 'w') as out:
        out.write(tempita.Template.from_filename(fn).substitute(data))


data = {'bars':
            [
                ('Level', 'Iterest', 'Materials'),
                [(5, 10, 15), (0, 20, 10), (20, 5, 3)],
                ('Tiziano Zito', 'Introduction', 'Day0')
            ]
        }

data['width'] = bar_width
data['height'] = bar_height
data['N'] = blocks_per_row
data['table_width'] = table_width

template('report.html.tmpl', data)

