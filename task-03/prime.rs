fn is_prime(num : i32) -> bool { // i32 => data type 32 bit integer
    if num <= 1 {
        return false;
    } else if num <= 3 {
        return true;
    } else if num % 2 == 0 || num % 3 == 0 {
        return false;
    }

    // check 6k+-1
    let mut i = 5;
    while i * i <= num {
        if num % i == 0 || num % (i + 2) == 0 {
            return false;
        }
        i += 6;
    }
    true
}

fn main(){
    let mut n = String::new();
    
    std::io::stdin().read_line(&mut n).expect("Failed to read line");

    let n: i32 = n.trim().parse().expect("Invalid input");
    for i in 2..=n {
        if is_prime(i){
            print!("{} " , i);
        }
    }
}


// run with rustc prime.rs and then run ./prime