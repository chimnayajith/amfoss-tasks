package main

import (
	"fmt"
)


func isPrime(num int) bool {
	if num <= 1{
		return false
	} else if (num <= 3){
		return true
	} else if (num % 2 == 0 || num % 3 == 0){
		return false
	}

	// check 6k+-1
	i := 5
	for i * i <= num{
		if num % i == 0 || num % (i + 2) == 0 {
			return false
		}
		i += 6
	}
	return true
}

func main(){
	var n int
	fmt.Scanln(&n)

	for i:=2; i <= n;i++ {
		if(isPrime(i)){
			fmt.Printf("%d " , i)
		}
	}
}