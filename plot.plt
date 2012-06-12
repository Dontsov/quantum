set dummy u,v
set samples 51, 51
set isosamples 21, 21
set title "3D quantum dot" 
set xlabel "X axis" 
set xlabel  offset character -3, -2, 0 font "" textcolor lt -1 norotate
set xrange [ -1.00000 : 1.00000 ] noreverse nowriteback
set ylabel "Y axis" 
set ylabel  offset character 3, -2, 0 font "" textcolor lt -1 rotate by -270
set yrange [ -1.00000 : 1.00000 ] noreverse nowriteback
set zlabel "Z axis" 
set zlabel  offset character -5, 0, 0 font "" textcolor lt -1 norotate
#splot [x=0:3] [y=0:3] sin(x) * sin(y)
# for python style ((np.exp(((-1.0) * E * t))) * np.sqrt(2 / a) * np.sin((np.pi * n * x) / a) 
#                                                     * np.sqrt(2 / b) * np.sin((np.pi * n * y) / b) 
#                                                     * np.sqrt(2 / c) * np.sin((np.pi * n * z) / c))
a = 1
b = 2
E = 30
n = 2
t = 1
h = 100
ph  = (6.26075E-34) / (2 * pi)
#splot [x=0:a] [y=0:b] [z=0:h] (exp(sqrt(1))) * sqrt(2/a) * sin((pi * n * x)/a)*sqrt(2/b) * sin((pi * n * x)/b)*sqrt(2/b) * sin((pi * n * z)/b)
#splot [x=0:a] [y=0:b] (exp(sqrt(1))) * sqrt(2/a) * sin((pi * n * x)/a)*sqrt(2/b) * sin((pi * n * x)/b)
#splot [x=0:a] [y=0:b] (exp(sqrt(-1) * E / ph)) * sqrt(2/a) * sin(pi * x * n / a) * sqrt(2/b) * sin(pi * y * n / b)#* sqrt(2/b)*sin((pi * n * z)/b)
#splot [x=0:a] [y=0:b] sqrt(2/a) * sin(pi * x * n / a) * sqrt(2/b) * sin(pi * y * n / b) * 23 * cos(x + 46) # for 3d
plot [x=0:a] [y=-1.5:b] sqrt(2/a) * sin(pi * x * 1 / a) ti "n = 1", sqrt(2/a) * sin(pi * x * 2 / a) ti "n = 2", sqrt(2/a) * sin(pi * x * 3 / a) ti "n = 3", (2/a) * sin(pi * x * 4 / a) ti "n = 4"

#m = 1.9E-31
#plot ((1**2) * ((6.26075E-34)**2)) / (2 * m * a), ((3**2) * (6.26075E-34)) / (2 * m * a)

#m = 2
#splot [x=0:a] [y=0:b] (sqrt(2/a) * sin(pi * x * m / a) * sqrt(2/b) * sin(pi * y * m / b) - sqrt(2/a) * sin(pi * x * n / a) * sqrt(2/b) * sin(pi * y * n / #b))/sqrt(2)  # for 3d


plot [x=0:a] [y=-1.5:b] (sqrt(2/a) * sin(pi * x * 1 / a)  + sqrt(2/a) * sin(pi * x * 2 / a)) / sqrt(2)