#FUNKSIYAGA RO'YXAT UZATISH
# def bahola(ismlar):
#     baholar={}
#     while ismlar:
#         ism=ismlar.pop()
#         baho=input(f'Talaba {ism.title()} bahosini kiriting: ')
#         baholar[ism]=baho
#     return baholar
# isms=['nodirbek','sharifjon','malika']
# baho=bahola(isms)
# print(baho)
# def matn_katta_harf(matn):
#     matn=matn[:]
#     for i in range(len(matn)):
#         matn[i]=matn[i].title()
#     return matn
# ismlar = ['ali', 'vali', 'hasan', 'husan']
# yangi_ismlar = matn_katta_harf(ismlar)
# print(ismlar)
# # print(yangi_ismlar)
# def matn_katta_harf(matn):
#     matns=matn[:]
#     for i in range(len(matns)):
#         matns[i]=matns[i].title()
#     return matns
# ismlar = ['ali', 'vali', 'hasan', 'husan']
# yangi_ismlar = matn_katta_harf(ismlar)
# print(ismlar)
# print(yangi_ismlar)
def bahola(ismlar):
    isms=ismlar[:]
    baholar={}
    for ism in isms:
        ism1=ism
        baho=input(f'{ism1.title()} ning bahosi: ')
        baholar[ism1]=baho
    return baholar
ismlar = ['ali', 'vali', 'hasan', 'husan']
print(bahola(ismlar))
print(ismlar)
