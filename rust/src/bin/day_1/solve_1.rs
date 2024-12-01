const INPUT: &str = include_str!("./input.txt");

fn main() {
    let (mut numbers1, mut numbers2) = fun_name();

    numbers1.sort();
    numbers2.sort();

    let mut res = 0;

    let mut i = 0;

    while i < numbers1.len() {
        res += (numbers1[i] - numbers2[i]).abs();
        i += 1;
    }

    println!("Result: {}", res);
}

fn fun_name() -> (Vec<i32>, Vec<i32>) {
    let mut numbers1: Vec<i32> = Vec::new();
    let mut numbers2: Vec<i32> = Vec::new();

    for line in INPUT.lines() {
        // Split the line into parts and parse the numbers
        let mut parts = line.split_whitespace();

        if let (Some(num1), Some(num2)) = (parts.next(), parts.next()) {
            // Parse the numbers from strings into integers
            if let (Ok(n1), Ok(n2)) = (num1.parse::<i32>(), num2.parse::<i32>()) {
                // Append the numbers to the respective vectors
                numbers1.push(n1);
                numbers2.push(n2);
            } else {
                eprintln!("Failed to parse numbers from line: {}", line);
            }
        }
    }
    (numbers1, numbers2)
}
