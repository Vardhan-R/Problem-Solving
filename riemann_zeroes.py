import matplotlib.pyplot as plt, numpy as np

# fp = open("riemann_zeroes.txt", 'r')
# raw_data = fp.readlines()
# fp.close()

riemann_zeroes_lst = [14.134725141734695, 21.022039638771556, 25.01085758014569, 30.424876125859512, 32.93506158773919, 37.586178158825675, 40.9187190121475, 43.327073280915, 48.00515088116716, 49.7738324776723, 52.970321477714464, 56.44624769706339, 59.34704400260235, 60.83177852460981, 65.1125440480816, 67.07981052949417, 69.54640171117398, 72.0671576744819, 75.70469069908393, 77.1448400688748, 79.33737502024937, 82.91038085408603, 84.73549298051705, 87.42527461312523, 88.80911120763446, 92.49189927055849, 94.65134404051989, 95.87063422824531, 98.83119421819369, 101.31785100573138, 103.72553804047834, 105.44662305232609, 107.1686111842764, 111.02953554316967, 111.87465917699264, 114.32022091545271, 116.22668032085755, 118.79078286597621, 121.37012500242065, 122.94682929355258, 124.25681855434577, 127.5166838795965, 129.57870419995606, 131.08768853093267, 133.4977372029976, 134.75650975337388, 138.11604205453344, 139.7362089521214, 141.12370740402113, 143.11184580762063, 146.0009824867655, 147.42276534255961, 150.05352042078488, 150.92525761224147, 153.0246938111989, 156.11290929423788, 157.59759181759406, 158.8499881714205, 161.18896413759603, 163.030709687182, 165.5370691879004, 167.1844399781745, 169.09451541556882, 169.9119764794117, 173.41153651959155, 174.75419152336573, 176.44143429771043, 178.37740777609997, 179.916484020257, 182.20707848436646, 184.8744678483875, 185.59878367770747, 187.22892258350186, 189.41615865601693, 192.0266563607138, 193.0797266038457, 195.26539667952923, 196.87648184095832, 198.01530967625192, 201.2647519437038, 202.49359451414054, 204.18967180310455, 205.3946972021633, 207.90625888780622, 209.57650971685626, 211.6908625953653, 213.34791935971268, 214.54704478349143, 216.1695385082637, 219.0675963490214, 220.714918839314, 221.43070555469333, 224.00700025460432, 224.9833246695823, 227.4214442796793, 229.33741330552536, 231.25018870049917, 231.98723525318024, 233.6934041789083, 236.5242296658162]
riemann_zeroes_arr = np.array(riemann_zeroes_lst)

x = np.arange(riemann_zeroes_arr.size)
# temp = np.sin(0.5 + riemann_zeroes_arr * 1j)
temp = np.array([sum(1 / (np.e ** ((0.5 + i_2 * 1j) * i_1) - 1)) for i_2 in riemann_zeroes_arr for i_1 in x])
y = temp.real
z = temp.imag

# for i in range(0, len(raw_data), 16):
#     riemann_zeroes_lst.append(float(raw_data[i][2:-1]))

# print(len(riemann_zeroes_lst))
# print(riemann_zeroes_lst)

# np.array([])

plt.plot(x, y)
plt.plot(x, z)
# plt.plot(x, 2 * x + 45)
plt.show()