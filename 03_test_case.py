def status_lulus(nilai):
    if nilai >= 60:
        return "Lulus"
    return "Tidak lulus"


test_data = [59, 60, 61]

for nilai in test_data:
    print(f"Nilai {nilai} -> {status_lulus(nilai)}")