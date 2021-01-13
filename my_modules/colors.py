colors = {
    'white':  0,
    'red':    1,
    'green':  2,
    'yellow': 3,
    'blue':   4,
    'purple': 5,
    'cyan':   6,
    'gray':   7
    }
styles = {
    'bold':      1,
    'underline': 4,
    'negative':  7
}
def cprint(string, c='', bgc='', style=0,end='\n'):
    end = '\033[m'+end
    if c != '':
        c= ('3{}'.format(colors[c]))
    if bgc!= '':
        bgc= ('4{}'.format(colors[bgc]))
    if style != 0:
        style = styles[style]
    if bgc=='':
        print ('\033[{};{}m{}'.format(style, c, string), end=end)
    else:
        print ('\033[{};{};{}m{}'.format(style, c, bgc, string), end=end)

def creturn (string, c='', bgc='', style=0,end='\033[m'):
    if c != '':
        c= ('3{}'.format(colors[c]))
    if bgc!= '':
        bgc= ('4{}'.format(colors[bgc]))
    if style != 0:
        style = styles[style]
    if bgc=='':
        string_return = '\033[{};{}m{}{}'.format(style, c, string,end)
    else:
        string_return = '\033[{};{};{}m{}{}'.format(style, c, bgc, string,end)
    return string_return