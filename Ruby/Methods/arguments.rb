def take(arr, amount=1)
    amount.times { arr.shift }
    arr
end
