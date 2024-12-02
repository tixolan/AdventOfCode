use std::fs;
use std::collections::HashMap;

fn main() {
    let file_path = "puzzle_input.txt";

    let puzzle = fs::read_to_string(file_path).expect("Couldn't Read File");
    let lines: Vec<Vec<&str>> = puzzle.lines().map(|l| { l.split("   ").collect() }).collect();

    let mut left = lines
        .iter()
        .map(|l| l.iter().nth(0).unwrap())
        .collect::<Vec<_>>();
    let mut right = lines
        .iter()
        .map(|l| l.iter().nth(1).unwrap())
        .collect::<Vec<_>>();

    // Part 1
    left.sort();
    right.sort();

    let mut acc = 0;
    for (l, r) in left.iter().zip(right.iter()) {
        acc += (l.parse::<i32>().unwrap() - r.parse::<i32>().unwrap()).abs();
    }
    println!("Part 1: {}", acc);

    // Part 2 - It's ok that the arrays are sorted
    let mut occurrences = HashMap::new();
    for n in right {
        occurrences.entry(n).and_modify(|occ| { *occ += 1 }).or_insert(1);
    }
    
    acc = 0;
    for n in left {
        let num = n.parse::<i32>().unwrap();
        let occ = occurrences.entry(n).or_default();
        acc += num**occ;
    }
    println!("Part 2: {}", acc);
}