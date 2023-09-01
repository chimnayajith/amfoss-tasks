defmodule PrimeNumbers do
    def isPrime(num) when num <= 1, do: false
    def isPrime(num) when num <= 3, do: true
    def isPrime(num) when rem(num, 2) == 0 or rem(num, 3) == 0, do: false
    def isPrime(num) do
        isPrime(num, 5)
    end

    def isPrime(num , i) when i*i <= num do
        rem(num , i )!= 0 and rem(num , i+2) != 0 and isPrime(num , i+6)
    end

    def isPrime(_ , _), do: true    


    def printPrime(n , i) when i<=n do
        if isPrime(i) do 
            IO.write("#{i} ")
        end
        printPrime(n , i+1)
    end
    def printPrime(_,_ ), do: nil
end

input=IO.gets("") |> String.trim() #to remove the /n character from the input
n = String.to_integer(input)
PrimeNumbers.printPrime(n ,2)