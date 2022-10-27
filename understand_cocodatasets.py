import json
#注意这里更改anno_file的路径
anno_file = 'D:/Projects/COCO/annotations/instances_train2017.json' #训练集有118287张图片，860001个注释
# anno_file='D:/Projects/COCO/annotations/instances_val2017.json' #验证集有5000张图片，36781个注释
with open(anno_file) as annos:
        annotation_json = json.load(annos)
'''
认识COCO/instances_train2017.json：
该json文件为一个字典，里面包含五个部分(用.keys方法查看):
['info', 'licenses', 'images', 'annotations', 'categories']
每部分的解释请参考网址：https://blog.csdn.net/qq_36268040/article/details/101635452
'''

print("The 'keys' is:--->",annotation_json.keys(),'\n')
print("The 'info' is:--->",annotation_json['info'],'\n')
print("The 'licenses' is:--->",annotation_json['licenses'],'\n')
#COCO2017总共有118287张图片,其中val2017含有5000张图片
print("The number of images is:--->",len(annotation_json['images']),'a example:--->',annotation_json['images'][0],'\n')
#val2017对应的annotations共有860001个,有两种格式的segmentation，分别为polygon(iscrowd=0)和RLE(iscrowd=1)
#在目标检测中，只关注annotations中的image_id"、"category_id"、"bbox"
print("The number of annotations is:--->",len(annotation_json['annotations']),'a example:--->',annotation_json['annotations'][0],'\n')
#COCO2017共有90个类别，对应的类别id={1, ... ,90}, 其中id=0表示背景
print("The number of 'categories' are:--->",len(annotation_json['categories']),"The ['categories'] are:--->",annotation_json['categories'],'\n')
#需要注意的是：['annotations'][0]['id']这里的id指的是对象id，每个对象都有一个独一无二的id
print("a example of 对象id is: ", annotation_json['annotations'][0]['id'])
'''
需要注意的一点是：
总共有80个类别，但是categories['id]={1, ... ,90}，其中没有id={12,26,29,30,45,66,68,69,71,83}的类别
'''
cate_list=[]
for i in range(len(annotation_json['categories'])):
        cate_list.append(annotation_json['categories'][i]['id'])
print(cate_list)

