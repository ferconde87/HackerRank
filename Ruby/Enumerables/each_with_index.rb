def skip_animals(animals, skip)
    result = []
    animals.each_with_index do |animal, index|
        result.push("#{index}:#{animal}") unless index < skip
    end
    result   
end
