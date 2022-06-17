from pickle import FALSE
from traceback import print_tb
import xlrd

try:




        def aynibul(gelen):
            x=0
            while(x<len(gelen)):
                temp=gelen[x]
                y=x+1
                while y<len(gelen):
                    temp2=gelen[y]
                    if temp==temp2: 
                        del gelen[y]

                    y+=1
                x+=1
            print(gelen)
            return gelen

        def bolumle(gelen):
            kalan=len(gelen)%10
            list=[]
            x=10
            if kalan==0:
                print(len(gelen))
                while x<(len(gelen)+10):
                    list.append(gelen[x-10:x])
                    
                    x+=10
            return list



    
        def excelcek(kacbas,kacmes,col):
            wb=xlrd.open_workbook_xls("enzngnlrtmeyltlr5500.xls")
            sheet=wb.sheet_by_index(0)    
            j=kacbas
            numara=[]
            tut=0
            cell=""
            mikt=kacmes+kacbas
            #bunu eğer liste uzunluğu atılmasını istediğim mesaj miktarından daha az olduğunda kullansın istedim
            #if row+kac<sheet.nrows:
             #   mikt=sheet.nrows

            while j<mikt:
                
                cell=sheet.cell_value(j,col)
                if type(cell)==float:
                    cell=int(cell)
                    cell=str(cell)


                if cell!="" and len(cell)>9:
                    i=0
                    kontrol=""
                    k=0
                    while i<len(cell):
                        if cell[i].isdigit():
                            
                                kontrol+=cell[i]

                        
                        i+=1
                    while k<len(kontrol):
                        if kontrol[k]=="0" and k==0:
                            kontrol=kontrol[1:]
                            k-=1    
                        k+=1
                    if kontrol!="":
                        numara.append(kontrol.strip())
                    

                j+=1
            
        # ind1_excelread.bolumle(numara)
            print(numara,len(numara))
            x=0
            nlist=[]
            nlen=len(numara)
            while(x<nlen):
                if len(numara[x])>15:
                    nlist=bolumle(numara[x])
                    del numara[x]
                    x-=1
                    for i in nlist:
                        numara.append(i)
                    

                
                x+=1

            nlist=aynibul(numara)
                
            numara=nlist

            print(nlist,"nlist")
            print(numara,"numara",len(numara))
            return numara
except Exception as e:
    print(e)


