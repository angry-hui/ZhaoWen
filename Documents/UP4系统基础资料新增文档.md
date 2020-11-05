#UP4系统基础资料新增
####基础资料保存在SelectInfo表，通过TypeFlag来区分
####--CODE为编码,Name为名称，TypeFlag为新增的类型
###类型参考：
		【11:办单类型,68:付款方式,87:口岸】
###代码参考:
	    INSERT INTO SelectInfo(CODE,NAME,TypeFlag) VALUES ('CODE','NAME','TYPEFLAG')


#####撰写人:周松辉   撰写时间:9/16/2020 12:16:22 PM
#####最后修改人:		最后修改时间: