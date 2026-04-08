# Import library
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Menyiapkan himpunan fuzzy
barang_terjual = ctrl.Antecedent(np.arange(0, 101, 1), 'barang_terjual')
permintaan = ctrl.Antecedent(np.arange(0, 301, 1), 'permintaan')
harga_peritem = ctrl.Antecedent(np.arange(0, 100001, 1), 'harga_peritem')
profit = ctrl.Antecedent(np.arange(0, 4000001, 1), 'profit')
stok_makanan = ctrl.Consequent(np.arange(0, 1001, 1), 'stok_makanan')

#barang_terjual
barang_terjual['rendah'] = fuzz.trimf(barang_terjual.universe, [0, 0, 40])
barang_terjual['sedang'] = fuzz.trimf(barang_terjual.universe, [30, 50, 70])
barang_terjual['tinggi'] = fuzz.trimf(barang_terjual.universe, [60, 100, 100])

#permintaan
permintaan['rendah'] = fuzz.trimf(permintaan.universe, [0, 0, 100])
permintaan['sedang'] = fuzz.trimf(permintaan.universe, [50, 150, 250])
permintaan['tinggi'] = fuzz.trimf(permintaan.universe, [200, 300, 300])

#harga_peritem
harga_peritem['murah'] = fuzz.trimf(harga_peritem.universe, [0, 0, 40000])
harga_peritem['sedang'] = fuzz.trimf(harga_peritem.universe, [30000, 50000, 80000])
harga_peritem['mahal'] = fuzz.trimf(harga_peritem.universe, [60000, 100000, 100000])

#profit
profit['rendah'] = fuzz.trimf(profit.universe, [0, 0, 1000000])
profit['sedang'] = fuzz.trimf(profit.universe, [1000000, 2000000, 2500000])
profit['tinggi'] = fuzz.trapmf(profit.universe, [1500000, 2500000, 4000000, 4000000])

#stok makanan
stok_makanan['sedang'] = fuzz.trimf(stok_makanan.universe, [100, 500, 900])
stok_makanan['banyak'] = fuzz.trimf(stok_makanan.universe, [600, 1000, 1000])

#Aturan
rule1 = ctrl.Rule(barang_terjual['tinggi'] & permintaan['tinggi'] & harga_peritem['murah'] & profit['tinggi'], stok_makanan['banyak'])
rule2 = ctrl.Rule(barang_terjual['tinggi'] & permintaan['tinggi'] & harga_peritem['murah'] & profit['sedang'], stok_makanan['sedang'])
rule3 = ctrl.Rule(barang_terjual['tinggi'] & permintaan['sedang'] & harga_peritem['murah'] & profit['sedang'], stok_makanan['sedang'])
rule4 = ctrl.Rule(barang_terjual['sedang'] & permintaan['tinggi'] & harga_peritem['murah'] & profit['sedang'], stok_makanan['sedang'])
rule5 = ctrl.Rule(barang_terjual['sedang'] & permintaan['tinggi'] & harga_peritem['murah'] & profit ['tinggi'], stok_makanan['banyak'])
rule6 = ctrl.Rule(barang_terjual['sedang'] & permintaan['rendah'] & harga_peritem['sedang'] & profit ['sedang'], stok_makanan['sedang'])

engine = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6])
system = ctrl.ControlSystemSimulation(engine)
system.input['barang_terjual'] = 80
system.input['permintaan'] = 225
system.input['harga_peritem'] = 25000
system.input['profit'] = 3500000

system.compute()
print(system.output['stok_makanan'])
#*barang_terjual.view()
#permintaan.view()
#harga_peritem.view()
#profit.view()
stok_makanan.view(sim=system)
input("Tekan ENTER untuk melanjutkan")
