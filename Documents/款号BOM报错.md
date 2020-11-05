##NO.UP4-ERROR001

##故障表现:进入款号BOM，提示“s”运算符后缺少操作数
###故障产生原因：部位名称中包含了特殊符号" ' " ， 表名(MaterialCalculationDetail列partname)
解决途径:取消掉MaterialCalculationDetail列partname中内容的单引号

关联数据表: MaterialCalculationDetail  b  --材料档？ ---   PurchaseShipMaterial 采购材料档？
		

源码参考:
    
	--通过物料BOM画面的后台log得到StyleDocTreeID ,用来取得PurchaseShipMaterial的ID
	select * from PurchaseShipMaterial where StyleDocTreeID = 100043202
	
	--通过PurchaseShipMaterial表与MaterialCalculationDetail关联，得到MaterialCalculationDetail表的ID与部位名称
	select b.ID,b.PartName from PurchaseShipMaterial a left join MaterialCalculationDetail b on a.MaterialCalculationDetailID = b.ID 
	where a.id = 100063914
	
	--update PurchaseShipMaterial
	--set PartName = '车于穿计左侧骨下脚上3  above wearer s left hem 3 on side seam'
	--where id = 100063913
	
	--通过ID名称来更新MaterialCalculationDetail表的部位名称
	select *  from MaterialCalculationDetail
	where id = 100118788
	
	update MaterialCalculationDetail
	set PartName = '车于穿计左侧骨下脚上3  above wearer s left hem 3 on side seam'
	where id = 100118788
	           


###撰写时间:9/15/2020 9:41:14 AM      撰写人:zhousonghui
