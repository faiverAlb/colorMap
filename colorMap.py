import re
import webcolors

__author__ = 'Gizetdinov.A'

import itertools
import sys
import csv
from jinja2 import Environment, FileSystemLoader


def WriteHtml(colors, outputFile, templateFile):
    env = Environment(loader=FileSystemLoader(''))
    template = env.get_template(templateFile)
    output_from_parsed_template = template.render(colors=colors)
    with open(outputFile, "w") as fh:
        fh.write(output_from_parsed_template)


def Grouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))


def getHexColorByName(name, language, colorReader=None):
    if not colorReader: colorReader = {}
    if language == "ru":
        if name.lower() in colorReader:
            return colorReader[name.lower()]
        return None
    try:
        color = webcolors.name_to_hex(name)
        return color
    except:
        return None


def main():
    if len(sys.argv) != 4:
        print(u'usage: ./colorMap.py incomeFile outputHtml language("ru"/"en")')
        sys.exit(1)
    incomeFile = sys.argv[1]
    outputFile = sys.argv[2]
    templateFile = "mytmplate"
    language = sys.argv[3]
    groupCount = 30
    colorReader = {}
    if language == 'ru':
        with open('russian_colors.csv', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            colorReader = {rows[0]:rows[1] for rows in reader}

    input_file = open(incomeFile)
    colors = []
    for line in input_file:
        words = line.split()
        for word in words:
            word = re.sub(r'[^\w-]', '', word)
            rgbColor = getHexColorByName(word, language,colorReader)
            if rgbColor is not None:
                colors.append(rgbColor)
    groupedItems = list(Grouper(groupCount, colors))
    WriteHtml(groupedItems, outputFile, templateFile)
    print('Finished')


if __name__ == '__main__':
    main()
