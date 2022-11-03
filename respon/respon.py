import datetime as date
import time
import url 
def respon_sample(input):
    u_pesan = str(input).lower()
    
    if u_pesan in ("halo njeng","halo cok"):
        return "sopo iki bgst, kok gk sopan"    
    if u_pesan in ("halo","hello","p"):
        return "siapa ya? ada yg bisa saya bantu?"
    
    if u_pesan in ("nama lo siapa","nama mu siapa"):
        return "bima bot"
    
    if u_pesan in ("tanggal berapa sekarang","sekarang tanggal berapa?","tanggal brp","tanggal?"):
        waktu = time.strftime("%d %b %Y")
        return waktu
    if u_pesan in ("hari ini hari apa","hari apa hari ini","sekarang hari apa","hari?","hari apa sekarang"):
        waktu1 = time.strftime("%A")
        return waktu1
    if u_pesan in ("sekarang bulan apa","bulan apa sekarang","bulan?"):
        aa = time.strftime("%b")
        return aa
    if u_pesan in ("sekarang tahun berapa","tahun berapa sekarang","tahun berapa","tahun?"):
        af = time.strftime("%Y")
        return af
    #if u_pesan in ("help"):
     #   return 
    if u_pesan in ("buka yt","yt"):
        yt = str(url.yt())
        return "membuka Youtube",yt
    if u_pesan in ("buka fb","fb"):
        fb = str(url.fb())
        return "membuka Facebook",fb
    if u_pesan in ("buka ig","ig"):
        ig = str(url.ig())
        return "membuka Instagram",ig
    if u_pesan in ("buka excel","excel"):
        excel = str(url.excel())
        return "membuka Instagram",excel
    if u_pesan in ("buka word","word"):
        word = str(url.word())
        return "membuka word",word
    if u_pesan in ("buka ppt","ppt"):
        ppt = str(url.ppt())
        return "membuka ppt",ppt
    return "maaf gua gk ngerti"