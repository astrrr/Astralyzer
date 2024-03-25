import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class Astralyzer:
    def __init__(self, filepath, product_name):
        self.filepath = filepath
        self.product_name = product_name
        self.data = None
        self._load_data()
        self._assign_col()      
        
        
    def _load_data(self):
        self.data = pd.read_csv(self.filepath)
        
    def _assign_col(self):
        column_names = ['Date', 'Time', 'Open', 'High', 'Low', 'Close', 'Volume']
        self.data.columns = column_names
        
        date_time_str = [f'{self.data.iloc[i]["Date"]}, {self.data.iloc[i]["Time"]}' for i in range(len(self.data))]
        self.data['DateTime'] = date_time_str
        
        vol = [((self.data.iloc[i]['High'] - self.data.iloc[i]['Low']) / self.data.iloc[i]['Open']) for i in range(len(self.data))]
        self.data['Volatility'] = vol
        
    def calculate_volatility_stats(self):
        vol_mean = np.mean(self.data["Volatility"])
        vol_std = np.std(self.data["Volatility"])
        vol_1std_plus = vol_mean + vol_std
        vol_2std_plus = vol_mean + (vol_std * 2)
        vol_3std_plus = vol_mean + (vol_std * 3)
        vol_1std_minus = vol_mean - vol_std
        vol_2std_minus = vol_mean - (vol_std * 2)
        vol_3std_minus = vol_mean - (vol_std * 3)
        
        return vol_mean, vol_std, vol_1std_plus, vol_2std_plus, vol_3std_plus, vol_1std_minus, vol_2std_minus, vol_3std_minus

    def visualize_volatility(self):
        vol_mean, vol_std, vol_1std_plus, vol_2std_plus, vol_3std_plus, vol_1std_minus, vol_2std_minus, vol_3std_minus = self.calculate_volatility_stats(data)
    
        sns.histplot(data=self.data, bins=60, x="Volatility", kde=True)
        plt.title(f'{self.product_name} Volatility {self.data.iloc[0]["Date"]} - {self.data.iloc[-1]["Date"]}')
        
        plt.axvline(vol_mean, color='Green', linewidth=2, linestyle="--", label="Mean")
        plt.figtext(0.3, 0.50, f"Mean: {vol_mean*100:.7f} %", fontsize=10)
        
        plt.axvline(vol_1std_plus, color='Blue', linewidth=2, linestyle="--", label="1SD Upper")
        plt.figtext(0.3, 0.60, f"1SD Upper: {vol_1std_plus*100:.7f} %", fontsize=10)
        
        plt.axvline(vol_2std_plus, color='Coral', linewidth=2, linestyle="--", label="2SD Upper")
        plt.figtext(0.3, 0.70, f"2SD Upper: {vol_2std_plus*100:.7f} %", fontsize=10)
        
        plt.axvline(vol_3std_plus, color='Red', linewidth=2, linestyle="--", label="3SD Upper")
        plt.figtext(0.3, 0.80, f"3SD Upper: {vol_3std_plus*100:.7f} %", fontsize=10)
        
        plt.axvline(vol_1std_minus, color='Blue', linewidth=2, linestyle="--", label="1SD Lower")
        plt.figtext(0.3, 0.40, f"1SD Lower: {vol_1std_minus*100:.7f} %", fontsize=10)
        
        plt.axvline(vol_2std_minus, color='Coral', linewidth=2, linestyle="--", label="2SD Lower")
        plt.figtext(0.3, 0.30, f"2SD Lower: {vol_2std_minus*100:.7f} %", fontsize=10)
        
        plt.axvline(vol_3std_minus, color='Red', linewidth=2, linestyle="--", label="3SD Lower")
        plt.figtext(0.3, 0.20, f"3SD Lower: {vol_3std_minus*100:.7f} %", fontsize=10)
        
        plt.legend()
        plt.show()

