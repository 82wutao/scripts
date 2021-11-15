#!/usr/bin/python3
# -*- coding:UTF-8 -*-
import sys
import atexit

import numpy as np

def output(file,data,ln=None):
    file.write(data)
    if ln is None:
        return 
    file.write(ln)


if __name__=="__main__":
    '''
    mt.py -trans matrix.txt -src.txt [-out out.txt]
    '''
    args=sys.argv

    trans=np.loadtxt(args[1],dtype=float,delimiter=" ")
    data=np.loadtxt(args[2],dtype=float,delimiter=" ")
    outfile=None
    if len(args)>=4:
        outfile=open(args[3],mode="wt",encoding='utf8')
        def close_out():
            outfile.close()
            pass

        atexit.register(close_out)
    else:
        outfile=sys.stdout


    r=True
    while r:
        if data.size==0:
            break
        if trans.size==0:
            break

        dim=data.shape[1]
        map_count=trans.shape[0]
        if dim!=map_count:
            break

        result = np.dot(data,trans)
        for row in result:
            o=' '.join(str(c) for c in row)
            output(outfile,o,'\n')
        
        r=False
    pass
