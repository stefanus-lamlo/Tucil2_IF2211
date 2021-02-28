#LIST VARIABEL GLOBAL
ListMatkul = []
MatkulTerurut = []

def bacaFile(namaFile):
    #buka file
    buka = "..\\test\\"+namaFile+".txt"
    file_sample = open(buka, 'r')
    doc = file_sample.readlines()
    #buka iterasi isi file
    for line in doc:
        #pisahkeun koma, hapus titik, buat jadi list of lists.
        pelajaran = [lim.strip() for lim in line.replace('.','').split(',')]
        ListMatkul.append(pelajaran)

def matkulSendirian(ListMatkulNew):
    #memasukkan matkul yang sendirian ke list terurut
    ListSendirian = []
    for pelajaran in ListMatkulNew:
        if (len(pelajaran)==0): #menghapus list kosong
            ListMatkulNew.remove(pelajaran)
        if (len(pelajaran)==1): #mencari list yang sendirian
            ListSendirian.append(pelajaran[0])
    if(len(ListSendirian)!=0): #memasukkan list sendirian ke matkul terurut sebagai semester
        MatkulTerurut.append(ListSendirian)

def topoSort(SisaMatkul):
    matkulSendirian(SisaMatkul) #memasukkan matkul ke list
    for pelajaran in SisaMatkul: #looping antara pelajaran tersisa
        for semester in MatkulTerurut: #looping isi matkul yang sudah diambil
            for keluarkan in semester: #menghapus matkul yang sudah diambil dari prereq
                if keluarkan in pelajaran:
                    pelajaran.remove(keluarkan)
    if(len(SisaMatkul) != 0): #rekursif uwu
        topoSort(SisaMatkul)

def senja(angka): #mengubah angka menjadi romawi biar kayak anak senja indie
    result = ''
    pengecualian = {100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'} #listing dict pengecualian
    while angka != 0:
        for find, v in pengecualian.items():
            if angka >= find:
                bagi = int(angka/find) #hitung sisa romawi
                angka %= find
                result += bagi*v #masukkan karakter ke romawi
    return result

def hasil(MatkulTerurut): #print hasil, inputan formatnya list of matkul in semester
    count = 1
    print("___________________________________________________")
    for semester in MatkulTerurut: #looping per semester
        print("Semester ke",senja(count),"maneh kudu ngambil:", end=" ")
        sks = 1
        for pelajaran in semester:
            if (sks!=len(semester)):
                print(pelajaran, end=", ")
                sks+=1
            else :
                print(pelajaran, end="")
        print()
        count+=1
    print("___________________________________________________")

#Program utama hohohihe
namaFile=input("masukkan nama file txt: ")
bacaFile(namaFile)
topoSort(ListMatkul)
hasil(MatkulTerurut)