using DelimitedFiles;
mat = readdlm("input/input_day1.txt",Int);
println(sum(0 .< (mat[begin+1:end]-mat[begin:end-1])));
println(sum(0 .< (mat[begin+3:end]-mat[begin:end-3])));