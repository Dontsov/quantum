set tmargin 0
set bmargin 0
set lmargin 3
set rmargin 3
unset xtics
unset ytics
#set term postscript eps enhanced
#set output "test.eps"
set multiplot layout 4,1 title "Собственные функции вычислительных состояний\n"

a = 1
b = 2
E = 30
n = 2
t = 1
h = 100
plot [x=0:1.5] [y=-1.5:b] sqrt(2/a) * sin(pi * x * 2 / a) ti "n = 2"
plot [x=0:a] [y=-1.5:b] (sqrt(2/a) * sin(pi * x * 1 / a)  + sqrt(2/a) * sin(pi * x * 2 / a)) / sqrt(2) ti "n = 3"
plot [x=-0.3:1.3] [y=-1.5:b] sqrt(2/a) * sin(pi * x * 1 / a) ti "n = 1"
plot [x=0:a] [y=-1.5:b] (sqrt(2/a) * sin(pi * x * 1 / a)  - sqrt(2/a) * sin(pi * x * 2 / a)) / sqrt(2) ti "n = 0"
#set terminal eps
#print  foo.eps