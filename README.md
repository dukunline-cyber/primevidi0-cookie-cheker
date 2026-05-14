# Prime Video Cookie Checker v1.1

Bot untuk cek validitas cookie Prime Video secara massal dengan dukungan format Netscape.

## Install
```bash
pip install -r requirements.txt
```

## Cara Pakai
1. Taruh file cookie (.txt) di folder `cookies/`
2. Jalankan:
```bash
python checker.py
```
3. Hasil valid akan disimpan di `results/valid.txt`

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
- ✅ Parsing otomatis format Netscape
- ✅ Multi-threaded checking untuk performa lebih cepat
- ✅ Menyimpan hasil cookie yang valid
- ✅ Error handling yang informatif

## Notes
- Jangan push folder `cookies/` dan `results/` ke GitHub
- Gunakan `.gitignore` yang sudah disediakan
