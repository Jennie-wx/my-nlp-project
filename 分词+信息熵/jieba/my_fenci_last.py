import jieba
import jieba.posseg as pseg
import jieba.analyse
import os

#停用词读取
def stopwordslist():
    stopwords = [line.strip() for line in open('hit_stopwords.txt',encoding='UTF-8').readlines()]
    return stopwords

stopwords=stopwordslist()   

#lines存储分词后的结果
lines=[]
def fenci(path):
    files = os.listdir(path)
    for file in files:
        position = path + '/' + file
        with open(position,'r',encoding='utf-8') as f:
            for l in f:
                l = l.strip()
                if l != ' ':
                    tags=jieba.cut(l)
                    for t in tags:
                        if t not in stopwords:
                            lines.append(t)
            print(lines)
    #将分词结果写入seg.txt
    with open('seg.txt','w') as segFile:
        for l in lines:
            for p in l:
                #p=list(p)
                segFile.write(p)
            segFile.write('\n')
        print('分词成功')

    #统计词频
    word_dict= {} 
    key_list=[] 
    wcList=[]
    cnt=0
    with open("wordCount2.txt",'w') as wf2: #打开文件 
        for item in lines: 
            if item not in word_dict: #统计数量 
                word_dict[item] = 1
            else: 
                word_dict[item] += 1
        for wc in word_dict.keys():
            wcList.append([wc,word_dict[wc]])
        key_list=sorted(wcList,key=lambda ci:ci[1],reverse=True)
        for key in key_list:
            if key[0] != ' ':
                wf2.write(str(key[0])+' '+str(key[1])+'\n')
                cnt+=1
            if cnt==100:
                break
        print("统计完成")

if __name__ == '__main__':
    path='/Users/wangxin/Desktop/fencitry/t'
    fenci(path)
