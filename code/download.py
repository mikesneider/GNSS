# -*- coding: utf-8 -*-                                                                                     
from os import  mkdir,listdir, path,sep                                                                     
import urllib                                                                                               
                                                                                                            
                                                                                                            
#Descargar brdc de los días de los anos 2012 al actual, de IGS                                              
                                                                                                            
#years=["2012","2013","2014","2015","2016"]
years=["2016"]   
days=range(1,366)                                                                                           
                                                                                                            
#outputdir="/home/wanda/Descarga_IGR"   
outputdir="/home/mikesneider/Descarga_IGR" 
outfile=open("notfound_daysIONEX.txt", "wb")                                                                
                                                                                                            
for year in years:                                                                                          
        for day in days:                                                                                    
                strday=str(day)                                                                             
                if len(strday)==1:                                                                          
                        strday="00"+strday                                                                  
                elif len(strday)==2:                                                                        
                        strday="0"+strday                                                                   
                #ftp://cddis.gsfc.nasa.gov/gps/products/ionex/2003/011/igrg0110.03i.Z                       
        #ftp://cddis.gsfc.nasa.gov/gps/products/ionex/2013/001/igrg0010.13i.Z                               
                url="ftp://cddis.gsfc.nasa.gov/gps/products/ionex/"+year+"/"+strday+"/igrg"+strday+"0."+yea$
                print url                                                                                   
                                                                                                            
                if year not in listdir(outputdir):                                                          
                        mkdir(outputdir+sep+year)                                                           
                                                                                                            
                location=outputdir+sep+year                                                                 
                filename=location+"/igrg"+strday+"0."+year[-2:]+"i.Z"                                       
                                                                                                            
                try:                                                                                        
                        urllib.urlretrieve(url,filename)                                                    
                except:                                                                                     
                        print "File not found"                                                              
                        row="Day # "+strday+" not found in year "+year                                      
                        outfile.write(row)                                                                  
                                           
