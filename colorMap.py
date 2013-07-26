__author__ = 'Gizetdinov.A'

import itertools
import sys
from colour import Color
from jinja2 import Environment, FileSystemLoader


def WriteHtml(colors, outputFile, templateFile):
    env = Environment(loader=FileSystemLoader(''))
    template = env.get_template(templateFile)
    output_from_parsed_template = template.render(colors=colors)
    with open(outputFile, "w") as fh:
        fh.write(output_from_parsed_template)


def Grouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e != None] for t in itertools.zip_longest(*args))


def main():
    if len(sys.argv) != 3:
        print('usage: ./colorMap.py incomeFile outputHtml')
        sys.exit(1)
    incomeFile = sys.argv[1]
    outputFile = sys.argv[2]
    templateFile = "mytmplate"
    groupCount = 30
    input_file = open(incomeFile)
    colors = []
    stop_words = ['the', 'that', 'to', 'as', 'there', 'has', 'and', 'or', 'is', 'not', 'a', 'of', 'but', 'in', 'by',
                  'on', 'are', 'it', 'if']
    for line in input_file:
        words = line.split()
        for word in words:
            if word not in stop_words and len(word) > 2:
                try:
                    c = Color(word)
                    colors.append(c.get_web())
                except:
                    pass
    WriteHtml(list(Grouper(groupCount, colors)), outputFile, templateFile)
    print('Finished')


if __name__ == '__main__':
    main()
