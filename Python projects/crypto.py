s_blocks = ["1430165277356420", "5517070321342466", "2133203220003111"] # true
main_peres = "87325416"
expend_peres = "327856143728"
def peres_s(ctr, n_key):
    dic = {}
    d1 = ""
    # n_key = key[:-4]
    for k, u in zip(range(1, 10), ctr):
        dic.update({str(k): u})
    for r in n_key:
        d1 += dic.get(r)
    return d1
def peres(ctr, n_key):
    dic = {}
    for k, u in zip(n_key, ctr):
        dic.update({int(k): u})
    lis_n = ""
    for p in sorted(dic.keys()):
        lis_n += dic.get(p)
    return lis_n
def probability_calculation(default, c_real, round):
    probal.clear()
    def11 =[]
    if round == 3:
        for tt, c in zip(default, range(4)):
            if c == 4:
                break
            def11.append(tt)
    else:
        def11 = default
    for ds in def11:
        count = c_real.count(ds)
        if count / len_mass == 1:
            probal.append(0)
        else:
            probal.append(count/16)
    return probal
def per_ex(s, key):
    dic = {}
    p = ""
    for k, u in zip(range(8), s):
        dic.update({int(k): u})
    for k1 in key:
        p += str(dic.get(int(k1)-1))
    return p
c = [{}, {}, {}]
a_end = []
c_end = []
mon = []
main_pos_a = [[], [], []]
main_pos_c = [[], [], []]
for s_block, round in zip(s_blocks, range(len(s_blocks))):
    len_mass = len(s_block)
    c_mass = [bin(c) for c in range(int(len_mass//2))]  # дефолтные значения для С
    a_mass = [bin(c) for c in range(len(s_block))]  # дефолтные значения А
    input_1 = [bin(c) for c in range(len(s_block))]  # Вход 1
    output_1 = [bin(int(a)) for a in s_block]
    input_2 = []
    output_2 = []
    del_c = []
    probal = []
    mon = []
    dict_pos = {}
    a_end = []
    c_end = []
    u = 0
    po =[]
    for del_a in a_mass:
        mon.append([])
        input_2.clear()   # очищаем перед новым дельта А
        output_2.clear()
        del_c.clear()

        for i in input_1:
            input_2.append(bin(int(i, 2) ^ int(del_a, 2)))

        for n in input_2:
            for count in range(len(output_1)):
                if n == input_1[count]:
                    output_2.append(output_1[count])

        for k in range(len(output_1)):
            del_c.append(bin(int(output_1[k], 2) ^ int(output_2[k], 2)))
        rrr = probability_calculation(c_mass, del_c, round)
        for qw in rrr:
            mon[u].append(qw)
        u += 1
        c[round].update({del_a: del_c})
    pos_1 = []
    pos_2 = []
    max1 = 0
    maint = [int(i) for i in range(16)]
    for mo in mon:
        if max1 < max(mo):
            max1 = max(mo)
    for mo, count_1 in zip(mon, range(len(mon))):
        for m, count_2 in zip(mo, range(len(mo))):
            if m == max1:
                pos_1.append(count_1)
                pos_2.append(count_2)
    for po1 in range(len(pos_1)):
        a_end.append(a_mass[pos_1[po1]])
        c_end.append(c_mass[pos_2[po1]])
    main_pos_a[round] = [bin(a) for a in pos_1]
    main_pos_c[round] = [bin(a) for a in pos_2]
    print("!!!!!!")
    for i in mon:
        print(i)
    print("11111111111")
''''
Получили в 3 раунде 3 значения дельта А:  0100, 1001, 1101
Подходит дельта а равное 0100
Конечное значение дельта А: 0010 1110 0100
'''''
final_a = "001011100100"
final_c = "10001101"  # 100-011-01 если 3-3-2, иначе 100-011-001
del_xr = peres(final_a, expend_peres[:-4])  # del xr = 10001110
del_d = peres_s(final_c, main_peres)        # del d  = 10001011
xr_mass = []
yr_mass = []
encrypted_data = open("save.txt", "r")
counter = 0
for line in encrypted_data:
    if line != " ---  ---  ---  --- \n" and line != "\n":
        counter += 1
        if counter < 3:
            text_for_analysis = line[0:-5].split(' --- ')
            XL, XR, YL, YR = text_for_analysis
            xr_mass.append(XR)
            yr_mass.append(YR)
        else:
            counter = 0
del_c = [final_c[:3], final_c[3:6], final_c[-2:]]
qq  = [[], [], []]
aaa = [[], [], []]
input_2 = []
output_2 = []
del_c1 = []
input_1 = [bin(c) for c in range(16)]
main_pos_a[2] = main_pos_a[2][0]
main_pos_a[0] = main_pos_a[0][0]
main_pos_a[1] = main_pos_a[1][0]
main_pos_c[2] = main_pos_c[2][0]
main_pos_c[0] = main_pos_c[0][0]
main_pos_c[1] = main_pos_c[1][0]
for a1, counter in zip(main_pos_a, range(3)):
        output_1 = [bin(int(a)) for a in s_blocks[counter]]
        input_2 = []
        output_2 = []
        del_c1.clear()
        for i in input_1:
            input_2.append(bin(int(i, 2) ^ int(a1, 2)))
        for n in input_2:
            for count in range(len(output_1)):
                if n == input_1[count]:
                    output_2.append(output_1[count])
        for k in range(len(output_1)):
            del_c1.append(bin(int(output_1[k], 2) ^ int(output_2[k], 2)))
        for c1, asd in zip(del_c1, range(16)):

                if bin(int(c1, 2)) == bin(int(del_c[counter], 2)):
                    aaa[counter].append(bin(asd))
def gen_key(mass):
    k = [[], [], []]
    for xr in mass:
        xr = per_ex(xr, expend_peres)
        xr_r = [xr[:4], xr[4:8], xr[-4:]]
        for coun in range(3):
            for ww in aaa[coun]:
                k[coun].append(bin(int(xr_r[coun], 2) ^ int(ww, 2)))
    tab_k = [[], [], []]
    for co in range(3):
        for d in input_1:
            tab_k[co].append(k[co].count(bin(int(d, 2))))
    pr_value_1 = []
    for k_k in tab_k:
        max_k = max(k_k)
        for i, k1 in enumerate(k_k):
            if k1 == max_k:
                pr_value_1.append(bin(i))
    for pp, ff in zip(k, tab_k):
        pp.clear()
        ff.clear()
    return pr_value_1
print(gen_key(xr_mass))
print(gen_key(yr_mass))


''''
values for K1_1
0000
0010
1001
1011

values for K1_2
0010
0011
1100
1101

values for K1_3
1000
1010
1100
1110

###############

values for K3_1
0100
0110
1101
1111

values for K3_2
0000
0001
1110
1111

values for K3_3
0000
0010
0100
0110

'''''
