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
        
    def calculate_stats(self, column):
        mean = np.mean(self.data[column])
        std = np.std(self.data[column])
        std_plus_1 = mean + std
        std_plus_2 = mean + (std * 2)
        std_plus_3 = mean + (std * 3)
        std_minus_1 = mean - std
        std_minus_2 = mean - (std * 2)
        std_minus_3 = mean - (std * 3)
        
        return mean, std, std_plus_1, std_plus_2, std_plus_3, std_minus_1, std_minus_2, std_minus_3

    def visualize_volatility(self, width=8, height=6):
        mean, std, std_plus_1, std_plus_2, std_plus_3, std_minus_1, std_minus_2, std_minus_3 = self.calculate_stats(column="Volatility")
    
        plt.figure(figsize=(width, height))
    
        sns.histplot(data=self.data, bins=60, x="Volatility", kde=True)
        plt.title(f'{self.product_name} Volatility {self.data.iloc[0]["Date"]} - {self.data.iloc[-1]["Date"]}')
        
        plt.axvline(mean, color='Green', linewidth=2, linestyle="--", label="Mean")
        plt.axvline(std_plus_1, color='Blue', linewidth=2, linestyle="--", label="1SD Upper")
        plt.axvline(std_plus_2, color='Coral', linewidth=2, linestyle="--", label="2SD Upper")
        plt.axvline(std_plus_3, color='Red', linewidth=2, linestyle="--", label="3SD Upper")
        plt.axvline(std_minus_1, color='Blue', linewidth=2, linestyle="--", label="1SD Lower")
        plt.axvline(std_minus_2, color='Coral', linewidth=2, linestyle="--", label="2SD Lower")
        plt.axvline(std_minus_3, color='Red', linewidth=2, linestyle="--", label="3SD Lower")
        
        text = f"Mean: {mean*100:.7f} %\n\n1SD Upper: {std_plus_1*100:.7f} %\n2SD Upper: {std_plus_2*100:.7f} %\n3SD Upper: {std_plus_3*100:.7f} %\n\n1SD Lower: {std_minus_1*100:.7f} %\n2SD Lower: {std_minus_2*100:.7f} %\n3SD Lower: {std_minus_3*100:.7f} %"
        plt.text(0.95, 0.05, text, fontsize=10, transform=plt.gca().transAxes,
             verticalalignment='bottom', horizontalalignment='right', bbox=dict(facecolor='white', alpha=0.5))
    
        plt.legend()
        plt.show()

    def visualize_close(self, width=8, height=6):
            
        mean, std, std_plus_1, std_plus_2, std_plus_3, std_minus_1, std_minus_2, std_minus_3 = self.calculate_stats(column="Close")
    
        plt.figure(figsize=(width, height))
    
        sns.histplot(data=self.data, bins=60, x="Close", kde=True)
        plt.title(f'{self.product_name} Close {self.data.iloc[0]["Date"]} - {self.data.iloc[-1]["Date"]}')
        
        plt.axvline(mean, color='Green', linewidth=2, linestyle="--", label="Mean")
        plt.axvline(std_plus_1, color='Blue', linewidth=2, linestyle="--", label="1SD Upper")
        plt.axvline(std_plus_2, color='Coral', linewidth=2, linestyle="--", label="2SD Upper")
        plt.axvline(std_plus_3, color='Red', linewidth=2, linestyle="--", label="3SD Upper")
        plt.axvline(std_minus_1, color='Blue', linewidth=2, linestyle="--", label="1SD Lower")
        plt.axvline(std_minus_2, color='Coral', linewidth=2, linestyle="--", label="2SD Lower")
        plt.axvline(std_minus_3, color='Red', linewidth=2, linestyle="--", label="3SD Lower")
        
        text = f"Mean: {mean:.7f} \n\n1SD Upper: {std_plus_1:.7f} \n2SD Upper: {std_plus_2:.7f} \n3SD Upper: {std_plus_3:.7f} \n\n1SD Lower: {std_minus_1:.7f} \n2SD Lower: {std_minus_2:.7f} \n3SD Lower: {std_minus_3:.7f}"
        plt.text(0.95, 0.05, text, fontsize=10, transform=plt.gca().transAxes,
             verticalalignment='bottom', horizontalalignment='right', bbox=dict(facecolor='white', alpha=0.5))
    
        plt.legend()
        plt.show()