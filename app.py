from codes import codes
from flask import jsonify
import re

def app_code(data):

    code = data['code'].strip()
    _byte = len(code) / 8
    print(int(_byte))
    compare = r'[^0-1]'
    if re.search(compare, code):
        return jsonify({ 
            'status': False,
            'error': 1,
            'data': 'there are some characters that are not 0 or 1'})
    
    if int(str(_byte).split('.')[1]) > 0:
        return jsonify({
            'status': False,
            'error': 2,
            'data': 'there is an incomplete byte'})
    
    nums = convert_to_num(code)
    text = verify_codes(nums)
    return jsonify({'status': True,'data': text})



def convert_to_num(code): 
    code_list=list(code)
    _bits=len(code_list)
    _byte=_bits / 8
    output = []
    nums = []
    _count = 0
    for x in range(int(_byte)):
        sl = slice(_count, _count + 8)
        output.append(code_list[sl])
        _count = _count+8
    
    for x in output:
        num = iterete(x)
        nums.append(num)
    
    return nums

def iterete(code_list):
    table_num = [128, 64, 32, 16, 8, 4, 2, 1]
    output = []

    for x in range(len(code_list)):
        c=code_list[x]
        n=table_num[x]

        if(c != '0'):
            output.append(n)

    return sum(output)


def verify_codes(nums):
    the_text = []
    a_z = codes['a_z']
    a_z_m = codes['A_Z']
    d_g = codes['num']
    s_c = codes['xx']

    for n in nums:
        for a in a_z:
            if a['code'] == n:
                the_text.append(a['id'])
        for a in a_z_m:
            if a['code'] == n:
                the_text.append(a['id'])
        for a in d_g:
            if a['code'] == n:
                the_text.append(a['id'])
        for a in s_c:
            if a['code'] == n:
                the_text.append(a['id'])
    
    return ''.join(the_text)
