isPrime :: Int -> Bool
isPrime num 
    | num <= 1 = False
    | num <= 3 = True
    | num `mod` 2 == 0 || num `mod` 3 == 0 = False
    | otherwise = isPrime' num 5
    where
        isPrime' num i
            | i * i <= num = num `mod` i /= 0 && num `mod` (i + 2) /= 0 && isPrime' num (i + 6)
            | otherwise = True

main :: IO ()
main = do
    input <- getLine
    let n = read input :: Int
    mapM_ (\i -> if isPrime i then putStr (show i ++ " ") else return ()) [2..n]
