def sum_terms(n)
    tr = (1..n).each.map{|x| (x*x)+1 }
    sum = tr.reduce(0, :+)
end
