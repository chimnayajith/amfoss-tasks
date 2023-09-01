def isPrime(num)
    return false if num <= 1
    return true if num <= 3
    return false if num % 2 == 0 || num % 3 == 0

    i = 5
    while i * i <= num
        return false if num % i == 0 || num % (i + 2) == 0
        i += 6
    end

    return true
end

n = gets.to_i #gets is to read the input from a line & to_i is to convert it into a integer

# looping from 2 to n
(2..n).each do |i|
    if isPrime(i)
        print "#{i} "
    end
end

# ruby prime.rb