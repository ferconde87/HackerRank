def full_name(first_name, *middle_names, last_name)
    name = first_name
    middle_names.each do |middle|
        name += " "
        name += middle
    end
    name += " "
    name += last_name
    name
end
