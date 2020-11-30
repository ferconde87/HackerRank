def group_by_marks(marks, pass_marks)
    groups = marks.group_by{ |student, mark| mark > pass_marks }
    result = {}
    result["Failed"] = groups[false] unless groups[false].nil?
    result["Passed"] = groups[true] unless groups[true].nil?
    result
end

marks = {"Ramesh":23, "Vivek":40, "Harsh":88, "Mohammad":60}
puts group_by_marks(marks, 30)
