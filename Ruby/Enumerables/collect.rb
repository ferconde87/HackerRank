# def rot13(secret_messages)
#     secret_messages.map { |c| c.tr("a-z", "n-za-m") }
# end

def rot13(secret_messages)
    secret_messages.map { |c| c.tr("A-Za-z", "N-ZA-Mn-za-m") }
end
