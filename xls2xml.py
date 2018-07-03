#coding='utf-8'
import xlrd
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#sys.setdefaultencoding('utf8')

def getPathFileName(path):
    tmp = path.split('/');
    return tmp[len(tmp) -1 ].split('.')[0];

def xlsToxmlPath(path):
    return path.split('.')[0] + '.xml';

def export(path):
    data = xlrd.open_workbook(path, formatting_info = False, encoding_override="utf-8")
    table = data.sheets()[0]
    #print table

    f = open(xlsToxmlPath(path), 'wb')
    f.write(u'<?xml version="1.0" encoding="utf-8" ?>\n')
    f.write(u'<%s>\n' % getPathFileName(path))
    
    
    for i in range(2, table.nrows):
        s = u'<item ';
        tmp = [u'%s = "%s"' % (str(table.cell_value(1,j)), str(table.cell_value(i,j))) for j in range(table.ncols)];
        s += u' '.join(map(str, tmp));
        s += u'>\n';
        f.write(s);
    
    f.write(u'</%s>' % getPathFileName(path));


export('D:/tools2/God.xls')
#export('D:/tools2/mytest.xls')
