lines = readlines("input/input_day3.txt")
println(length(lines))
# Part 1

ones = zeros(Int, 12);
zilches = zeros(Int, 12);
for line in lines
    for (ind, ch) in enumerate(line)
        if ch == '0'
            zilches[ind] += 1
        else
            ones[ind] += 1
        end
    end
end

gamma_str = ""
epsilon_str = ""
for (a, b) in zip(ones, zilches)
    if a > b
        global gamma_str *= '1'
        global epsilon_str *= '0'
    else
        global gamma_str *= '0'
        global epsilon_str *= '1'
    end
end

gamma = parse(Int, gamma_str, base=2)
epsilon = parse(Int, epsilon_str, base=2)
println(gamma * epsilon)

# Part 2

function index_wrapper(x, i)
    if typeof(x) == Char
        return x
    else
        return x[begin+i]
    end
end

sort!(lines)

view = lines[begin:end]
pos = 0
while length(view) > 1 && pos < 12
    first_one = searchsortedfirst(view, '1', by=x -> index_wrapper(x, pos))
    println(first_one)
    if (first_one - 1) <= length(view) / 2
        global view = view[first_one:end]
    else
        global view = view[begin:first_one]
    end
    global pos += 1
end
println(view[begin])
ogr = parse(Int, view[begin], base=2)

view = lines[begin:end]
pos = 0
while length(view) > 1 && pos < 12
    first_one = searchsortedfirst(view, '1', by=x -> index_wrapper(x, pos))
    println(first_one)
    if first_one == length(view) + 1
        global pos += 1
        continue
    end
    if (first_one - 1) > length(view) / 2
        global view = view[first_one:end]
    else
        global view = view[begin:first_one]
    end
    global pos += 1
end
println(view[begin])
csr = parse(Int, view[begin], base=2)

println(ogr * csr)
