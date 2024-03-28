# 词性标注(Part-Of-Speech tagging, 简称POS)就是标注出一段文本中每个词汇的词性

import jieba.posseg as pseg
pseg.lcut("我爱北京天安门")
#[pair('我', 'r'), pair('爱', 'v'), pair('北京', 'ns'), pair('天安门', 'ns')] pair元组

# 结果返回一个装有pair元组的列表, 每个pair元组中分别是词汇及其对应的词性, 具体词性含义请参照[附录: jieba词性对照表]()
