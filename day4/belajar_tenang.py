"""
Program   : Belajar Tenang
Deskripsi : Program ini menghitung hari ke-n dari suatu tanggal berdasarkan tahun 1900+y dengan memperhitungkan tahun kabisat.
NIM/Nama  : 24060124110142/Muchammad Yuda Tri Ananda
Tanggal   : 23/09/2024
"""

"""
**************************************************************
DEFINISI DAN SPESIFIKASI
HariKe1900 : integer [1..31], integer [1..12], integer [0..99] → integer [1..366]
{HariKe1900(d,m,y) dari suatu tanggal <d,m,y> adalah hari absolut dihitung mulai 1 Januari tahun 1900+y. 1 Januari tahun 1900+y adalah hari ke 1}

dpm : integer [1..12] → integer [1..366]
{dpm(B) adalah jumlah hari kumulatif dari tanggal 1 Januari hingga tanggal 1 bulan B pada tahun tertentu, tanpa memperhitungkan tahun kabisat.}

IsKabisat? : integer [0..99] → boolean
{IsKabisat?(y) menghasilkan True jika tahun 1900+y adalah tahun kabisat, yaitu habis dibagi 4 tetapi tidak habis dibagi 100, atau habis dibagi 400.}
**************************************************************
"""

"""
**************************************************************
REALISASI
**************************************************************
"""


def BelajarTenang(dB, m):
    return (
        "Isi bensin dulu, bang"
        if round(15 * 10 ** ((dB - 40) / 20), 3) > m
        else f"{round(15 * 10 ** ((dB - 40) / 20), 3)} meter"
    )


"""
**************************************************************
APLIKASI
**************************************************************
"""

print(
    f"{BelajarTenang(102, 20000)} -> 18883.881 meter",
    f"{BelajarTenang(100, 1300)} -> Isi bensin dulu, bang",
)
