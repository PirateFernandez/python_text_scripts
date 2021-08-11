import matplotlib.pyplot as plt 
import numpy as np

u,v,x,y = np.loadtxt('postprocess_job208_job214_columns_2_6_7_8.csv', delimiter=',', unpack=True)
#w,x= np.loadtxt('fsc_post_deepemhr_half1_masked.csv', delimiter=',', unpack=True)
#a,b= np.loadtxt('fsc_post_deepemhr_half2_masked.csv', delimiter=',', unpack=True)
#c,d= np.loadtxt('rln-job140-model-ref/fsc_model_map_rln140_post.csv', delimiter=',', unpack=True)
#c,d= np.loadtxt('fsc_post-masked-ok.csv', delimiter=',', unpac
#c,d= np.loadtxt('fsc_post-masked-ok.csv', delimiter=',', unpack=True)



fig = plt.figure()
ax = fig.add_subplot(111)
x_ticks = [0,0.05,0.1,0.15,0.2,0.25,0.3,0.35]
y_ticks = [0,0.2,0.4,0.6,0.8,1]
plt.xlim([0, 0.382])
plt.ylim([-0.02, 1])
ax.plot(u,v,'k-o', linewidth=1.25, markersize=3.5)
ax.plot(u,x,'b-o', linewidth=1.25, markersize=3.5)
ax.plot(u,y,'r-o', linewidth=1.25, markersize=3.5)
#.plot(c,d,'y-')
#ax.plot(c,d,'or-')
ax.hlines(0.143, 0, 0.6, linewidth=1.25, linestyle='--', color='grey')
plt.xticks(x_ticks, labels=[])
#ax.tick_params(direction='out', length=8, width=2)
plt.yticks(y_ticks, labels=[])
for axis in ['top','bottom','left','right']:
  ax.spines[axis].set_linewidth(2.5)
#ax.set_xlabel('Resolution (1/$\AA$)', fontweight='bold')
#ax.set_ylabel('FSC', fontweight='bold')
plt.savefig("fsc_half_maps_job208_no_label_dpi_300.png", dpi=300)
plt.show()
#print(u)
