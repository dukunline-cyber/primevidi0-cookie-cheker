# Prime Video Cookie Checker v1.2

Bot untuk cek validitas cookie Prime Video secara massal dengan dukungan format Netscape dan ekstraksi RAR.

## Install
```bash
pip install -r requirements.txt
```

## Cara Pakai
1. Jika memiliki file RAR cookie, taruh di folder root (sama level dengan script)
2. Jalankan:
```bash
python checker.py
```
3. Bot akan mendeteksi file RAR dan menawarkan untuk mengekstraknya
4. Atau taruh file cookie (.txt) langsung di folder `cookies/`
5. Hasil valid akan disimpan di `results/valid.txt`

## Format Cookie
Bot mendukung 2 format cookie:

### Format 1: Netscape HTTP Cookie File (direkomendasikan)
Diekspor langsung dari browser (biasanya dari browser extensions atau tools).
Format tab-separated dengan struktur:
```
domain flag path secure expiration name value
```

Contoh:
```
.primevideo.com	TRUE	/	TRUE	1805340304	at-main-av	Atza|gQBqp6E...
.primevideo.com	TRUE	/	TRUE	1805340304	session-token	"NDqVEuySGFt3..."
```

### Format 2: Raw Cookie String
Cookie string langsung dari HTTP headers:
```
at-main-av=Atza|gQBqp6E...; session-token="NDqVEuySGFt3..."
```

## Fitur
- ✅ Ekstraksi otomatis file RAR
- ✅ Parsing otomatis format Netscape
- ✅ Multi-threaded checking untuk performa lebih cepat
- ✅ Menyimpan hasil cookie yang valid
- ✅ Error handling yang informatif

## Notes
- Jangan push folder `cookies/` dan `results/` ke GitHub
- Gunakan `.gitignore` yang sudah disediakan
