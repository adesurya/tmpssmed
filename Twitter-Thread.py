from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import random


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

]

# Set up Chrome WebDriver (make sure you have ChromeDriver installed and in your PATH)
driver = webdriver.Chrome()

# Your Twitter credentials
username = "ZaylaRawls47179"
password = "szEJMSukV5"

# Tweet URL to reply to
tweet_url = "https://twitter.com/kegblgnunfaedh/status/1786031786608443514"

# Reply message
reply_message = random.choice(commentsDict)

# Open Twitter login page
driver.get("https://twitter.com/i/flow/login")
sleep(7)

email = driver.find_element_by_name('text')
email.send_keys("ZaylaRawls47179") #replace with your valid twitter username
email.send_keys(Keys.ENTER)
sleep(3)
password = driver.find_element_by_name("password")
password.send_keys("szEJMSukV5") #replace with your valid twitter password
password.send_keys(Keys.ENTER)
sleep(5)

# Open the tweet to reply to
driver.get(tweet_url)
sleep(3)

# Click on the reply button
reply_button = driver.find_element_by_xpath("//div[@aria-label='Post text']")
reply_button.click()
sleep(2)

# Type the reply message
reply_textarea = driver.find_element_by_xpath("//div[@data-testid='tweetTextarea_0']")
reply_textarea.send_keys(reply_message)
sleep(2)

# Click on the tweet button to send the reply
tweet_button = driver.find_element_by_xpath("//div[@data-testid='tweetButtonInline']")
tweet_button.click()
sleep(2)

# Close the browser
driver.quit()
