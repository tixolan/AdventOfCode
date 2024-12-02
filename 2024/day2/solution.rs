use std::fs;

fn is_safe(levels: &Vec<i32>, diffs: &Vec<i32>) -> bool {
    let increasing = levels[0] < levels[1];
    let mut safe = true;
    for i in 0..(levels.len() - 1) {
        let diff = if increasing { levels[i + 1] - levels[i] } else { levels[i] - levels[i + 1] };
        if !diffs.contains(&diff) {
            safe = false;
            break;
        }
    }
    return safe
}

fn main() {
    let file_path = "puzzle_input.txt";
    let puzzle = fs::read_to_string(file_path).expect("Couldn't read file.");
    let reports = puzzle.lines();
    let diffs = vec![1, 2, 3];

    // Part 1
    let mut acc = 0;
    for report in reports.clone() {
        let levels: Vec<i32> = report.split_whitespace().into_iter().map(|lvl| { lvl.parse::<i32>().unwrap() }).collect();
        if is_safe(&levels, &diffs) {
            acc += 1;
        }
    }
    println!("Part 1: {}", acc);

    // Part 2
    acc = 0;
    for report in reports.clone() {
        let levels: Vec<i32> = report.split_whitespace().into_iter().map(|lvl| { lvl.parse::<i32>().unwrap() }).collect();
        if is_safe(&levels, &diffs) {
            acc += 1;
        } else {
            for i in 0..levels.len() {
                let mut new_levels = levels.clone();
                new_levels.remove(i);
                let safe = is_safe(&new_levels, &diffs);
                if safe {
                    acc += 1;
                    break;
                }
            }
        }
    }
    println!("Part 2: {}", acc);
}