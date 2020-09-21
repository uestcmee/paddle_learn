import os
import paddlehub as hub

humanseg = hub.Module(name='deeplabv3p_xception65_humanseg')

# 加载模型

# 图片文件的目录
path ='D:\\PycharmProjects\\paddle_learn\\01_img_seg\\img\\'
# path =r'D:\PycharmProjects\paddle_learn\01_img_seg\img\'

files=[path+ i for i in os.listdir(path)]
# 获取目录下的文件
#抠图
results = humanseg.segmentation(data={'image':files})
# result=results[0]['data']
