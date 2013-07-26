import itertools

__author__ = 'Gizetdinov.A'


def WriteHtml(colors):
    from jinja2 import Environment, FileSystemLoader
    env = Environment(loader=FileSystemLoader(''))
    template = env.get_template('mytmplate.txt')
    output_from_parsed_template = template.render(colors=colors)
    with open("my_new_file.html", "w") as fh:
        fh.write(output_from_parsed_template)

def mygrouper(n, iterable):
     args = [iter(iterable)] * n
     return ([e for e in t if e != None] for t in itertools.zip_longest(*args))

def main():
    from colour import Color
    input_file = open('file.txt')
    colors = []
    for line in input_file:
        words = line.split()
        for word in words:
            try:
                c = Color(word)
                colors.append(c.get_web())
            except:
                pass
    WriteHtml(list(mygrouper(30, colors)))
    print('Finished')




if __name__ == '__main__':
  main()
