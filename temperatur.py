def temperatur(temp):
    derajat = float(temp[:-1])
    input = temp[-1]

    if input() == 'c':
        convert1 = float(derajat + 273)
        convert2 = float((9*derajat)/5 +32)
        satuanx = 'celsius'
        satuan_1 = 'kelvin'
        satuan_2 = 'fahrenheit'
        print(derajat,satuanx,'=','{:.1f}'.format(convert1),satuan_1)
        print(derajat,satuanx,'=','{:.1f}'.format(convert2),satuan_2)
    
    elif input() == 'k':
        convert1 = float(derajat - 273)
        convert2 = float(((derajat - 273) * 9/5) +32)
        satuanx = 'kelvin'
        satuan_1 = 'celsius'
        satuan_2 = 'fahrenheit'
        print(derajat,satuanx,'=','{:.1f}'.format(convert1),satuan_1)
        print(derajat,satuanx,'=','{:.1f}'.format(convert2),satuan_2)
    
    elif input() == 'f':
        convert1 = float((derajat - 32) * 5/9)
        convert2 = float(((derajat - 32) * 5/9) + 273)
        satuanx = 'fahrenheit'
        satuan_1 = 'celsius'
        satuan_2 = 'kelvin'
        print(derajat,satuanx,'=','{:.1f}'.format(convert1),satuan_1)
        print(derajat,satuanx,'=','{:.1f}'.format(convert2),satuan_2)
    

    i=0
    while i==0:
        temp = input("\nMasukan suhu: ")
        temperatur(temp)
