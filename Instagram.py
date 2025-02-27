from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver import ActionChains
import random
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException
from seleniumwire import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

commentsDict = [
#'@repnas.indonesiamaju @anggawira.id memang luar biasa program relawannya, kongkrit',
#'lebih bermutu relawan daripada tim kampanye mudanya, program aktif dan merangkul anak muda. top emang @repnas.indonesiamaju @anggawira.id',
#'@repnas.indonesiamaju ini harusnya nomor 1 sih, dari awal sampai akhir sosialisasi program @prabowo terusss @anggawira.id',
#'tadi gw cek, @repnas.indonesiamaju masih sibuk sosialisasi program indonesia maju, tim kampanye muda nya malah vakum. lawak lawak',
#'ga salah sih, statistik kegiatan dan aktif kampanye @repnas.indonesiamaju ga ada lawannya',
#'jokowi perpanjangan tangannya projo, prabowo perpanjangan tangannya @repnas.indonesiamaju @anggawira.id. semua program dijelasin ama mereka',
#'ini tipikal relawan yang ga berani di kandang, dimana-mana dijabanin debat ama mereka @repnas.indonesiamaju @anggawira.id',
#'podcast, tv, sosmed rame terus ama @repnas.indonesiamaju',
#'ini baru relawan boss @repnas.indonesiamaju @anggawira.id',
#'pas masa kampanye seminggu bisa 3 kali kegiatan @repnas.indonesiamaju. ilmu padi abangku @anggawira.id',
#'ekonomi, kesehatan, geopolitik, pendidikan, budaya, investasi dibabat terus sama @repnas.indonesiamaju dan @anggawira.id',
#'disaat quick count relawan lain haha hihi merasa paling berjasa, @repnas.indonesiamaju dan @relawanpride ngawal terus @prabowo',
#'relawan yang ga banyak ngaku2, cuma 2. @repnas.indonesiamaju dan @relawanpride',
#'dari awal cuma rispek sama @repnas.indonesiamaju @relawanpride, sisanya gajeeee',
#'komandannya @repnas.indonesiamaju, @anggawira.id komut yang mundur untuk fokus kampanye',
#'kelas emang kakanda @anggawira,id',
#'orang paling komit yang paling gw tau, mundur komut bumn untuk fokus kampanye pemenangan prabowo gibran',
#'gw sih mikir2 buat cabut dari komisaris, ni orang gila juga @anggawira.id demi dukung @prabowo',
#'maestro politik emang ini @anggawira.id, ninggalin posisi komisaris tau-taunya tepat @prabowo menang',
#'kalau @anggawira.id yang turun, menang lah pasti barang ini',
#'@anggawira.id serba bisa, ekonomi paham, energi paham, tambang paham, investasi paham. emang si paling paham wkwkww',
#'relawan yang ga ngemis-ngemis ya @repnas.indonesiamaju',
#'satu slot menteri cocok untuk @anggawira.id',
#'kalo tipe komisaris atau menterinya kaya @anggawira.id, ga salah sih',
#'Asslammualaikum Kementrian Investasi, Calon Menteri masuk nih @anggawira.id',
#'kontribusi terbesar di relawan, ya @repnas.indonesiamaju dan @anggawira.id',
#'organisator dan pemimpin ulung @anggawira.id',
#'ga pernah gagal, tangan dingin @anggawira.id keren',
#'sukses organisasi, sukses bisnis dan sukses politik. definisi @anggawira.id',
#'kalo maen bola, @repnas.indonesiamaju ini tim bintang. bisa di orkestrasi oleh @anggawira.id',
#'dibayar berapa pinterpolitik sama nomor 1, wkwkwk padhaal dimana-mana yang dikenal orang @repnas.indonesiamaju',
#'lucu-lucu aja pinterpolitik narok @repnas.indonesiamaju nomor 2. admin kurang piknik',
#'udah pas issue @anggawira.id calon menteri, potensial sih',
#'boss @repnas.indonesiamaju @anggawira.id butuh stafsus di menteri investasi ga? mau apply nih',
#'Pak @prabowo, orang dibelakang anda top top @anggawira.id',
#'kalau kader KIM, pasti jadi menteri nih @anggawira.id',
#'Sekjend HIPMI emang topp @@repnas.indonesiamaju @anggawira.id',
#'mentor gw emang ga kaleng-kaleng @anggawira.id',
#'ilmu padi abang menteri @anggawira.id',
#'menteri kabinet sekarang ketar-ketir ama AW, ekonomi, investasi, pendidikan, pemuda olahraga dipahamin semua ama @anggawira.id',
#'ini orang top @anggawira.id, pernah kerja bareng dan narok investasi kedia komitmen nya luar biasa',
#'kalo masih ada yang ga kenal @anggawira.id parah sihh',
#'dari awal gw yakin pas tau @anggawira.id  mundur dari komut bumn dan turun gunung ikut kampanye @prabowo',
'menteri investasi, assalammualaikum @anggawira.id',
#'pengganti yang pass untuk bahlil nih, makin banyak investasi masuk kalo @anggawira.id menterinya',
#'HIPMI emang penghasil kader top, 2 orang kader hipmi sukses di panggung politik relawan @anggawira.id dan @anthonyleong.id',
#'jenderal luar biasaa emang @anggawira.id',
#'top sih ini bukan kaleng-kaleng @anggawira.id'

] #Add or replace words...

# #Selenium Wire configuration to use a proxy
# proxy_username = 'bd22e8abe4b1f976a2d2'
# proxy_password = '83c5bb1f397229f5'
# seleniumwire_options = {
#     'proxy': {
#         'http': f'http://{proxy_username}:{proxy_password}@gw.dataimpulse.com:10001',
#         'verify_ssl': False,
#     },
# }

# driver = webdriver.Chrome(
#     seleniumwire_options=seleniumwire_options
# )

# driver= webdriver.Chrome("/media/patusacyber/Data/RschAde/Master/chromedriver")

#Apabila tidak menggunakan proxy, gunakan line path ini dan hapus block Selenium Wire
driver = webdriver.Chrome('chromedriver')


#driver.maximize_window()
driver.get("https://www.instagram.com")
sleep(3)

driver.find_element_by_name('username').send_keys('tititzyyy') #replace with your insta username
sleep(1)
driver.find_element_by_name('password').send_keys('tarjoo') #replace with your insta password
sleep(2)
driver.find_element_by_xpath("//button[@type='submit']").click()
sleep(6)
driver.get('https://www.instagram.com/pinterpolitik/p/C5kv23cpJlL') #change the url 

sleep(4)
# post_click=driver.find_element_by_class_name("_aagw").click() #click on first post 
# sleep(3)
#like=driver.find_element_by_class_name("xp7jhwk").click() #click on like button
sleep(4)
driver.find_element(By.XPATH, "//textarea[@aria-label='Add a comment…']").click()
sleep(2)
driver.find_element(By.XPATH, "//textarea[@aria-label='Add a comment…']").send_keys(random.choice(commentsDict)) #send the text in comment section
sleep(5)
driver.find_element(By.XPATH, "//textarea[@aria-label='Add a comment…']").click() #click on comment section area
sleep(5)
driver.find_element(By.XPATH, "//textarea[@aria-label='Add a comment…']").send_keys(Keys.ENTER) #send the text in comment section
sleep(5)

# commentArea = driver.find_element_by_class_name("_akhn")
# commentArea.click()
# commentArea.send_keys("Using selenium to comment in burst of 5 ")

#commentArea.send_keys(Keys.RETURN)
#sleep(5)

# # next_button=driver.find_element_by_class_name("_abl-").click() #next button (code changed)
# # sleep(4)
