reset
set terminal wxt size 400,400
set encoding utf8
set style fill solid
set key outside bottom center horizontal font ",17"
set yrange [0.70 : 0.75]
set ytics 0,0.03 font ",15"

set style line 1\
	linecolor rgb "#49434a"

set style line 2\
	linecolor rgb "#a5cdd4"
	
set style line 3\
	linecolor rgb "#ffea75"

set style line 4\
	linecolor rgb "#F22727"


set ylabel "Accuracy" font ",17" offset -0.6,0.3
set xtics font ",17"
plot "src/Plot/NSL-KDD-2parameters/5class/NSL-KDD-2parameters_5class_Avg.txt" using 2:xtic(1) with histogram linestyle 1 title "DNN",\
"src/Plot/NSL-KDD-2parameters/5class/NSL-KDD-2parameters_5class_Avg.txt" using 3:xtic(1) with histogram linestyle 2 title "HC-DNN",\
"src/Plot/NSL-KDD-2parameters/5class/NSL-KDD-2parameters_5class_Avg.txt" using 4:xtic(1) with histogram linestyle 3 title "SA-DNN",\
"src/Plot/NSL-KDD-2parameters/5class/NSL-KDD-2parameters_5class_Avg.txt" using 5:xtic(1) with histogram linestyle 4 title "GA-DNN"
set terminal png
set output "src/Plot/NSL-KDD-2parameters/5class/5classAccuracy.png"
replot

#output  ------------------------------------------------------------------------------------------------------------------------
set output
