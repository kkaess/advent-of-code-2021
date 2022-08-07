lines = readlines("input/input_day2.txt");

h = v = 0;

for line in lines
    temp = split(line, ' ')
    val = parse(Int, temp[end])
    if temp[begin] == "forward"
        global h += val
    elseif temp[begin] == "down"
        global v += val
    elseif temp[begin] == "up"
        global v -= val
    end
end

println(h * v);

h = v = a = 0;

for line in lines
    temp = split(line, ' ')
    val = parse(Int, temp[end])
    if temp[begin] == "forward"
        global h += val
        global v += a * val
    elseif temp[begin] == "down"
        global a += val
    elseif temp[begin] == "up"
        global a -= val
    end
end

print(h * v);
