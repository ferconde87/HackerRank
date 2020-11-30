# select and return all odd numbers from the Array variable `arr`
def select_arr(arr)
    arr.select{|x| x.odd?}
end

# reject all elements which are divisible by 3
def reject_arr(arr)
    arr.reject{|x| x % 3 == 0}
end

# delete all negative elements
def delete_arr(arr)
    arr.delete_if{|x| x < 0}
end

# keep all non negative elements ( >= 0)
def keep_arr(arr)
    arr.keep_if{|x| x >= 0}
end
