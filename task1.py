#Tapşırıq 1: Tələbə qiymətləri statistikası
#Məlumat: 30 tələbənin imtahan balı.
#1. Orta balı hesabla. 
#2. Median və mod-u tap. 
#3. Dispersiya və standart sapmanı hesabla. 
#4. Bal paylanmasını qrafiklə vizuallaşdır (histogram).

import numpy as np 
from scipy import stats
import matplotlib.pyplot as plt

grades = [55, 70, 68, 90, 85, 77, 60, 70, 73, 88, 92, 50, 67, 80, 78, 85, 95, 62, 74, 81, 69, 77, 84, 71, 66, 89, 93, 70, 75, 82, 88]

print(len(grades))

mean_grade = np.mean(grades)
print("1)Orta bal:", f"{mean_grade:.2f}")




median_grade = np.median(grades)
print("2)Median:", median_grade)


mode_grade1 = stats.mode(grades).mode #tekrarlanan ededi gosterir
mode_grade2 = stats.mode(grades).count #tekrarlanma sayin gosterir
print("3)Mod:", mode_grade1)
print("3.1)Mod:", mode_grade2)

 
variance_grade = np.var(grades)
print("4)Dispersiya:", f"{variance_grade:.5f}")


std_grade = np.std(grades)
print("5)Standart Sapma:", f"{std_grade:.5f}")



plt.hist(grades, bins=10, color='silver', edgecolor='black')
plt.title("Telebelerin bal paylanmasi")
plt.xlabel('Bal')
plt.ylabel('Telebe sayi')
plt.axvline(mean_grade, color='red', linestyle='dashed', linewidth=2, label=f'Orta: {mean_grade:.2f}')
plt.axvline(median_grade, color='gold', linestyle='dashed', linewidth=2, label=f'Median: {median_grade}')
plt.legend()
plt.savefig("grades.png")
plt.show()

