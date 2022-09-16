

import os

os.listdir('..')



import yaml
import re




def curly(s):
    return s.replace('<','{').replace('>','}')

def bold(s):
    # s=' '+s
    sp = s.split('**')
    if len(sp)==1:
        return s
    r = [' \\textbf{', '}']
    i=0
    result=''
    result+=sp[0]
    for spp in sp[1:]:
        result += r[i]
        i = (i+1)%2
        result+=spp

    #print("--",result)
    return result


def markdown_links(s):
    site = re.compile( "\[(.*)\]" ).search(s)
    url = re.compile( "\((.*)\)" ).search(s)
    if site is not None and url is not None:
        s = s.replace(f'[{site.group(1)}]', f'\\href<{url.group(1)}>')
        s = s.replace(f'({url.group(1)})', f'<{site.group(1)}>')
    return s




def create_subsection(sub):
    INDENT=4
    lines=[]
    if "heading" in sub.keys():
        h = sub["heading"]
        lines += [' '*INDENT+'\\resumeSubheading']
        startdate=h['startdate' ] if 'startdate' in h else ''
        enddate=h['enddate' ] if 'enddate' in h else ''


        lines+=[' '*(INDENT+2)+f'<{h["label"]}><{startdate} -- {enddate}>']
        lines+=[' '*(INDENT+2)+f'<Stanford University><Stanford, California>']
    if 'degrees' in sub.keys():
        lines+=[' '*INDENT+f'\\resumeItemListStart']
        for d in sub['degrees']:
            lines+=[' '*(INDENT+2)+f'\\resumeItem<{d}>']
        lines+=[' '*INDENT+'\\resumeItemListEnd']
    if 'points' in sub.keys():
        lines+=[' '*INDENT+'\\resumeItemListStart']
        for d in sub['points']:
            if type(d)==list:
                lines+=[' '*(INDENT+2)+f'\\resumeItemListStart']
                for dl in d:
                    lines+=[' '*(INDENT+4) + f'\\resumeItem<{dl}>']
                lines+=[' '*(INDENT+2)+f'\\resumeItemListEnd']
            else:
                lines+=[' '*(INDENT+2) + f'\\resumeItem<{d}>']
        lines+=[' '*INDENT+'\\resumeItemListEnd']
    return lines


def create_section(s):
    lines=[]
    if "heading" in s.keys():
        lines += [f'\section<{s["heading"]}>']
    if 'subsections' in s.keys():
        lines += ['  \\resumeSubHeadingListStart']
        for sub in s['subsections']:
           lines += create_subsection(sub)
        lines += ['  \\resumeSubHeadingListEnd']
    if 'points' in s.keys():
        lines+=['  \\resumeItemListStart']
        for d in s['points']:
            lines+=[f'    \\resumeItem<{d}>']
        lines+=['  \\resumeItemListEnd']
    return lines


def get_sections(yaml_output):
    lines = []
    sections = yaml_output["sections"]
    # s = sections[0]

    for s in sections:
        lines += create_section(s)
        lines += [""]


    lines = [curly(bold(markdown_links(l))) for l in lines]
    return '\n'.join(lines)


if __name__ == "__main__":

    INFILE = "content.yaml"

    with open("template.tex", "r") as f:
        output = f.read()

    with open(INFILE, "r") as stream:
        try:
            result = yaml.safe_load(stream)
            print(result)
        except yaml.YAMLError as exc:
            print(exc)
    s = get_sections(result)

    output = output.replace('<<sections>>', s)
    output = output.replace('<<github>>', result['github'])
    output = output.replace('<<name>>', result['name'])
    output = output.replace('<<website>>', result['website'])
    output = output.replace('<<email>>', result['email'])
    # output = output.replace('<<linkedin>>', result['linkedin'])
    # output = output.replace('<<phone>>', result['phone'])

    with open(INFILE.replace('yaml','tex'), 'w') as f:
        f.write(output)

    print(output)