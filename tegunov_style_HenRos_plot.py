import numpy as np
import math
import matplotlib.pyplot as plt 
num_ptc = [8000, 16000, 32000, 64000, 114564]
res = [4.276, 3.605, 3.33, 3.115, 3.029]
num_ptc_ext = [8000, 16000, 32000, 64000, 114564, 800000]
res_ext = [4.276, 3.605, 3.33, 3.115, 3.029, 2.56]
ln_num_ptc = [float(np.log(i)) for i in num_ptc]
ln_num_ptc_ext = [float(np.log(i)) for i in num_ptc_ext]
res_inv = [1/(i*i) for i in res]
res_inv_ext = [1/(i*i) for i in res_ext]
#res_inv_unsharp = [1/(i*i) for i in res]
lin_fit = np.polyfit(ln_num_ptc, res_inv, 1)
nynquist = 1/(2.56*2.56)
labels_x = ['8','16','32','64','114.5']
labels_x_ext = ['8','16','32','64','114.5','800']
labels_y = ['4.27', '3.61', '3.33', '3.12', '3.03']
labels_y_ext = ['4.27', '3.61', '3.33', '3.12', '3.03','2.56']
#inv_res_sqr = [float(1/i** for i in list]
#for i in list_2:
#   print(f"{i:.2f}")
m, int_y = lin_fit
straight = [m*i+int_y for i in ln_num_ptc]
straight_ext = [m*i+int_y for i in ln_num_ptc_ext]
fig = plt.figure()
ax = fig.add_subplot(111)
#ax.plot(res_inv, ln_num_ptc)
ax.set_ylim(0.05, 0.157)
ax.set_xlim(8.95, 13.55)
#ax.plot(ln_num_ptc, straight, c='gray', linewidth=2)
ax.plot(ln_num_ptc_ext, straight_ext, c='gray', linewidth=2)
ax.hlines(nynquist, 8.4, 14, colors='darkmagenta', linestyles='--', linewidth=2.5, label='Nyquist')
ax.set_xticks(ln_num_ptc_ext)
ax.set_xticklabels(labels_x_ext)
ax.set_yticks(res_inv_ext)
ax.set_yticklabels(labels_y_ext)
plt.xlabel('x1000 Particles', fontweight='bold')
plt.ylabel('Resolution (Å)', fontweight='bold')
plt.text(8.95, 0.146, 'Nyquist limit', fontweight='bold', c='darkmagenta')
plt.text(9.8, 0.135, '2.0/slope= 99.16 Å$^2$', fontweight='bold', c='dimgray', fontsize=12)
plt.text(9.45, 0.12, 'slope= 0.02017, y-int= -0.122', c='dimgray', fontsize=12)
for i in range(len(num_ptc)):
	ax.hlines(res_inv[i], 8, ln_num_ptc[i], linestyles='--', colors='silver', linewidth=1, zorder=1)
for i in range(len(num_ptc)):
	ax.vlines(ln_num_ptc[i], 0.005, res_inv[i], linestyles='--', colors='silver', linewidth=1, zorder=1)
ax.scatter(ln_num_ptc, res_inv, s=80, c='limegreen', edgecolors=None)
plt.savefig('cug_bplot.png', dpi=300)
plt.show()
print(m, int_y)
