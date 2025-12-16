use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn read_file_as_digits<P: AsRef<Path>>(path: P) -> io::Result<Vec<Vec<u32>>> {
    let file = File::open(path)?;
    let reader = io::BufReader::new(file);

    let mut result = Vec::new();

    for line in reader.lines() {
        let line = line?; // unwrap io::Result<String>

        let digits: Vec<u32> = line
            .chars()
            .map(|c| c.to_digit(10).expect("non-digit character"))
            .collect();

        result.push(digits);
    }

    Ok(result)
}

fn solve_lines(numbers: &[Vec<u32>], digits: usize) -> u64 {
    let mut ans: u64 = 0;

    for line in numbers {
        let mut res_num: u64 = 0;
        let mut left_bound = 0;

        for round_it in 0..digits {
            let max_it = line.len() - digits + round_it;
            let mut highest_idx = 0;
            let mut highest_val = 0;

            for it in left_bound..=max_it {
                let num = line[it];
                if highest_val < num {
                    highest_idx = it;
                    highest_val = num;
                }
            }

            left_bound = highest_idx + 1;

            let exp = (digits - 1 - round_it) as u32;
            res_num += 10u64.pow(exp) * highest_val as u64;
        }

        ans += res_num;
    }

    ans
}

fn main() -> io::Result<()> {
    let numbers = read_file_as_digits("input.txt")?;
    let digits = 12;

    let ans = solve_lines(&numbers, digits);

    println!("Ans is: {}", ans);
    Ok(())
}

#[cfg(test)]
mod tests {
    use super::*;

    fn run_test(file: &str, digits: usize) -> u64 {
        let numbers = read_file_as_digits(file)
            .expect("failed to read input file");
        solve_lines(&numbers, digits)
    }

    #[test]
    fn test_txt_2_digits() {
        let result = run_test("test.txt", 2);
        assert_eq!(result, 357);
    }

    #[test]
    fn test_txt_12_digits() {
        let result = run_test("test.txt", 12);
        assert_eq!(result, 3121910778619);
    }

    #[test]
    fn input_txt_2_digits() {
        let result = run_test("input.txt", 2);
        assert_eq!(result, 17100);
    }
}
