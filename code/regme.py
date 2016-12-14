from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By
from datetime import *
import wget

#si no encuentra una estacion que?
#descargar en carpetas separadas 

outfile1=open("found_stations.txt", "wb") 
outfile2=open("notfound_stations.txt", "wb") 

#Input format : Month/Day/Year
stations={"CUEC":"01/01/2016", 
          "PTEC":"01/01/2016", 
          "QVEC":"01/01/2016", 
           "RIOP":"01/01/2016", 
           "STEC":"01/01/2016", 
           "ALEC":"01/01/2016", 
           "GZEC":"01/01/2016", 
           "AUCA":"01/01/2016", 
           "ESMR":"01/01/2016", 
           "COEC":"01/01/2016", 
           "MHEC":"01/01/2016", 
           "PDEC":"01/01/2016", 
           "PJEC":"01/01/2016", 
           "QUEM":"01/01/2016", 
           "TNEC":"01/01/2016", 
           "CLEC":"01/01/2016", 
           "ECEC":"01/01/2016", 
           "NJEC":"01/01/2016", 
           "NORE":"01/01/2016", 
           "QUI1":"01/01/2016", 
           "CXEC":"01/01/2016", 
           "EPEC":"01/01/2016", 
           "GYEC":"01/01/2016", 
           "PEEC":"01/01/2016", 
           "OREC":"01/01/2016", 
           "SIEC":"01/01/2016", 
           "FOEC":"01/01/2016", 
           "LJEC":"01/01/2016", 
           "LPEC":"01/01/2016", 
           "GUEC":"01/01/2016", 
           "ONEC":"01/01/2016", 
           "BHEC":"01/01/2016", 
           "LREC":"01/01/2016", 
           "MAEC":"01/01/2016", 
           "MTEC":"01/01/2016", 
           "SNLR":"01/01/2016", 
           "EREC":"01/01/2016", 
           "IBEC":"01/01/2016", 
           "PREC":"01/01/2016", 
           "CHEC":"01/01/2016", 
           "SCEC":"01/01/2016", 
           "SEEC":"01/01/2016", 
           "ABEC":"01/01/2016", 
	}


def daterange(start_date): # input: Installation Date.  Returns: List of days between station's installation date and current day.
    month=int(start_date.split("/")[0]) 
    day=int(start_date.split("/")[1]) 
    year=int(start_date.split("/")[2])
    dates=[]
    y=[int(i) for i in str(datetime.today()).split()[0].split("-")][0] #Current day
    m=[int(i) for i in str(datetime.today()).split()[0].split("-")][1]
    d=[int(i) for i in str(datetime.today()).split()[0].split("-")][2]
    #~ today= date(y,m,d)
    today= date(2016,1,3)
    start_date = date(year,month,day)
    for n in range(int ((today - start_date).days)): #Year-Month-Day
		nextday=str(start_date + timedelta(n)).split("-")
		nextday=[nextday[1],nextday[2],nextday[0]] 
		nextday="/".join(nextday)#Month/Day/Year
		dates.append(nextday)
    return dates


for station in stations:
    print station
    first_date=stations[station]
    days=daterange(first_date) 
    for day in days:
		driver = webdriver.Firefox()
		url="http://www.geoportaligm.gob.ec/ftp/inicio.php?codigo="+station
		driver.get(url)
		
		#Login
		inputUser =  driver.find_element(By.NAME, "usuario")
		inputUser.send_keys("53080737")
		inputPw =  driver.find_element(By.NAME, "clave")
		inputPw.send_keys("yNeZeNaN")
		driver.find_element(By.TAG_NAME, "form").submit()
		
		try:
			alert = driver.switch_to_alert()
			alert.accept()
			print "alert accepted"
		except:
			print "no alert"
		
		#Filling Form
		radio_btn_Intervalo =  driver.find_element(By.ID, "RadioGroup1_1")
		radio_btn_Intervalo.click()
		print "radio checked"
		inputProy =  driver.find_element(By.NAME, "proyecto")
		inputProy.send_keys("Multipos")
		inputDate = driver.find_element_by_xpath("//input[@name='fecha']") #Month/Day/Year
		driver.execute_script('document.getElementById("fecha").removeAttribute("readonly")')
		inputDate.send_keys(day)
		driver.find_element(By.NAME, "Enviar").click()
		
		year=day.split("/")[2][-2:]
		
		nav=year+"N"
		obs=year+"D"
		try:
			navlink=driver.find_element_by_partial_link_text(nav)
			wget.download(navlink.get_attribute('href'))
			obslink=driver.find_element_by_partial_link_text(obs) 
			wget.download(obslink.get_attribute('href'))
			row="Station :"+station+" M/D/Y: "+day+"  "+str(obslink.get_attribute('href'))+"\n"
			outfile1.write(row) 
			print "Data Found"
			
		except:
			print "There arent any files for this date"
			row="There arent any files for station "+station+" in "+day+"\n"
			outfile2.write(row) 
			
		driver.quit()
    

