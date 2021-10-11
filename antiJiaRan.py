import os
import random
import glob

#可能会随到文字或者图片的反嘉然
def antiJiaRan():
    #反嘉然文字
    antiJiaRanText = [random.choice(['我超，夹心糖','不要嘉然不要嘉然'])],[],[]
    #反嘉然图片
    antiJiaRanPic = [],[random.choice(glob.glob('antiJiaRanPic'+os.path.sep+'*'))],[]
    #选一个返回
    antiJiaRanResponse = random.choice([antiJiaRanPic,antiJiaRanText])
    return antiJiaRanResponse

#反犯病用文案
def antiFanBing():
    antiFanBing = [random.choice(['你不要过来啊','能不能正常点','犯病的滚嗷','?'])],[],[]
    return antiFanBing