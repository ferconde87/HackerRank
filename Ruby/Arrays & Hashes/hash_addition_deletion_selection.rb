hackerrank[543121] = 100
# or h.store(key, value)

hackerrank.keep_if{|key, value| key.is_a?(Integer)}

hackerrank.delete_if{|key, value| key.even?}
