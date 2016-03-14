set output "results.png"
set title 'results.png'                       				   # plot title
set xlabel 'Roll Results' font "bold"                          # x-axis label
set ylabel '# of Occurances' font "bold"                       # y-axis label
set style fill solid 1.00 border 0
set style histogram
set style data histogram
plot 'results.dat' with boxes lt rgb "blue"
pause -1