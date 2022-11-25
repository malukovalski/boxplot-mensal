import xarray as xr
import numpy as np
import matplotlib.pyplot as plt

dataset = xr.open_dataset('data_xarray.nc')

#Dependendo do arquivo é necessário um tratamento nos dados nessa etapa

def boxplot(dataset, titulo, save_img):

    mes_group = dataset.groupby('time.month')

    mes = ['Janeiro','Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 
               'Setembro', 'Outubro', 'Novembro', 'Dezembro']

    fig = plt.figure(figsize = (18,23))
    plt.suptitle(titulo, fontsize=18, ha='center')
    
	for i in range(12):

        hour = mes_group[i+1].groupby('time.hour')

        ax = fig.add_subplot(6,2,i+1)
        
        boxplots = ax.boxplot([hour[0],hour[3],hour[6],hour[9],hour[12],hour[15],hour[18],hour[21]], 
                              labels=['00', '03', '06', '09', '12', '15', '18', '21'],
                   widths = .7,
                   patch_artist=True,
                   medianprops = dict(linestyle='-', linewidth=2, color='Black'),
                   boxprops = dict(linestyle='--', linewidth=2, color='Black', facecolor = 'blue', alpha = .4)
                  );

        boxplot1 = boxplots['boxes'][0]
        boxplot1.set_facecolor('red')
        boxplot2 = boxplots['boxes'][1]
        boxplot2.set_facecolor('green')
        boxplot3 = boxplots['boxes'][2]
        boxplot3.set_facecolor('orange')
        boxplot4 = boxplots['boxes'][3]
        boxplot4.set_facecolor('blue')
        boxplot5 = boxplots['boxes'][4]
        boxplot5.set_facecolor('teal')
        boxplot6 = boxplots['boxes'][5]
        boxplot6.set_facecolor('brown')
        boxplot7 = boxplots['boxes'][6]
        boxplot7.set_facecolor('pink')
        boxplot8 = boxplots['boxes'][7]
        boxplot8.set_facecolor('purple')

        ax.set_yticks(np.arange(0, 14, 2))
        plt.grid()
        if i >= 10: 
            plt.xlabel('Hora (UTC)', fontsize = 18);
        if i == 0 or i%2 == 0:
            plt.ylabel('Intensidade (m/s)', fontsize = 18);
        plt.xticks(fontsize = 16);
        plt.yticks(fontsize = 16);
        plt.title(f'{mes[i]}', fontsize = 18, loc='right')
        
        plt.subplots_adjust(left=0.125,
                    bottom=0.1, 
                    right=0.9, 
                    top=0.95, 
                    wspace=0.2, 
                    hspace=0.35)
    
    figname=f'path/{save_img}'
    plt.savefig(figname, dpi=300, bbox_inches="tight")