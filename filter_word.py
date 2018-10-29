# -*- coding:utf-8 -*-

import json
import filter

def input_dict(path):
    with open(path) as f:
        dict = json.load(fp = f)
    return dict

def output_dict(dict,path):
    jsonObj = json.dumps(dict, ensure_ascii=False, indent=4)
    fileObject = open(path, 'w')
    fileObject.write(jsonObj)
    fileObject.close()

def get_key_dict(dict):
    key_list = [] 
    for i in dict:
        key_list.append(i)
    return key_list

# dict词库字典； keyword过滤词词库; rate准确率
def filter_kv_dict(dict, keyword, rate):
    gfw = filter.DFAFilter()
    gfw.parse(keyword)
    length = len(list(dict))
    index = 0
    for key in list(dict.keys()):
        index = index + 1
        print("%s/%s"%(index,length))
        value = dict[key]
        if gfw.filter(key):
            del dict[key]
            continue
        for in_key in list(value.keys()):
            print(in_key,value[in_key])
            #根据准确度过滤
            if value[in_key] < rate:
                del dict[key][in_key]
                continue
            print(in_key,gfw.filter(in_key))
            #根据关键词过滤
            if gfw.filter(in_key):
                del dict[key][in_key]
                continue
    #过滤空字典
    for key in list(dict.keys()):
        if dict[key] and len(dict[key]) >4 :
            pass
        else:
            del dict[key]
    return dict

def main():
    dict = input_dict('./more_similar/test.json')
    fdict = filter_kv_dict(dict, 'keywords', 0.6)
    # print(fdict)
    output_dict(fdict, 'more_similar/test_filter.json')
    print('╮(╯▽╰)╭ 终于完成过滤啦~more_normal.json')

main()