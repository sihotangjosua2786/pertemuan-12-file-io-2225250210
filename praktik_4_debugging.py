def hitung_rata_rata(nilai):

    if len(nilai) == 0:
        return 0

    return sum(nilai) / len(nilai)


def status(nilai):

    if nilai >= 60:
        return "Lulus"

    return "Tidak lulus"


def nilai_tertinggi(nilai):

    if len(nilai) == 0:
        return None

    tertinggi = nilai[0]

    for x in nilai[1:]:

        if x > tertinggi:
            tertinggi = x

    return tertinggi


nilai = [80, 60, 90, 70]

print("Rata-rata :", hitung_rata_rata(nilai))
print("Status 60 :", status(60))
print("Tertinggi :", nilai_tertinggi(nilai))
```【1-176c2a】

---

# Hasil Retest

| ID | Expected | Actual | Status |
|----|----|----|----|
| T1 | 75 | 75 | PASS |
| T2 | 90 | 90 | PASS |
| T3 | Lulus | Lulus | PASS |
| T4 | Tidak lulus | Tidak lulus | PASS |
| T5 | 90 | 90 | PASS |

---

# README.md

```markdown
# Pertemuan 13 - Debugging dan Testing

Nama : ....................
NIM : ....................
Kelas : ....................

## Kasus

Program memuat bug pada perhitungan rata-rata,
status kelulusan, dan pencarian nilai tertinggi.

## Test Case

| ID | Input | Expected | Actual Awal | Status |
|----|--------|--------|--------|--------|
| T1 | [80,60,90,70] | 75 | 60 | FAIL |
| T2 | [100,80] | 90 | 36 | FAIL |
| T3 | 60 | Lulus | Tidak lulus | FAIL |
| T4 | 59 | Tidak lulus | Tidak lulus | PASS |
| T5 | [80,60,90,70] | 90 | 0 | FAIL |

## Bug Report

### B01
Pembagi rata-rata selalu 5.

### B02
Operator > digunakan sehingga nilai 60 gagal.

### B03
Logika pencarian nilai tertinggi terbalik.

## Retest

Semua test case PASS.

## Cara Menjalankan

python3 praktik/praktik_4_debugging.py

## Refleksi

Tracing dan test case batas paling membantu karena
langsung menunjukkan sumber kesalahan logika.