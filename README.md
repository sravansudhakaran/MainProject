# MainProject
Main Project Reliability of Electronic Components, Electronics and Communication Department, NSSCE Palakkad

## Dataset Description with hierarchy

### 1.igbt_original
Complete Dataset with 7 Columns , scrapped from mat file .

### 2.igbt_added_RUL
Dataset with 8 columns , last column is RUL (linearly decreasing), populated by RUL_Filler.py applied on [1] .

### 3.igbt_norm
Dataset with 7 columns , 'Time' Column is removed from [2] .

### 4.igbt_algor_checker
Manipulated dataset with 7 columns, 'Heat Sink Temp' is replaced with custom values in [3] .

### 5.igbt_heatsink_removed
Dataset with 6 columns, 'Heat Sink Temp' is removed from [3] .

### 6.igbt_noise_removed
Dataset with 7 columns, taken from [3] , and removed abnormal readings as well as readings after failure occured .

### 7.igbt_noise_removed_normalised
Dataset with 7 columns , taken from [6] , each column is normalised using the maximum value in that column .
