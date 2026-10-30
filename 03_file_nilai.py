def nilai_tertinggi(data):

    if len(data) == 0:
        return None

    tertinggi = data[0]

    for nilai in data[1:]:

        if nilai > tertinggi:
            tertinggi = nilai

    return tertinggi


nilai = [80, 60, 90, 70]

print("Nilai tertinggi =", nilai_tertinggi(nilai))