/*
Guessing game

Author: Luis Esteban Rodriguez <rodriguezjluis0@gmail.com>
Date: Feb 22 2023
*/

use std::io;
use std::cmp::Ordering;
use rand::Rng;
use colored::*;

fn main() {
    
    println!("Guess the number!");

    let mut number_of_guesses: u32 = 0;

    loop {
    
        println!("Please input your guess.");

        let secret_number: u32 = rand::thread_rng().gen_range(1, 10);
        
        let mut guess: String = String::new();

        io::stdin()
            .read_line(&mut guess)
            .expect("Failed to readline");

        let guess: u32 = match guess.trim().parse() {
            Ok(num) => num,
            Err(_) => continue,
        };

        // PLUS: tracking of number of guesses
        number_of_guesses += 1;

        println!("The secret number is {}", secret_number);
     
        println!("You guessed: {}", guess);

        match guess.cmp(&secret_number){
            Ordering::Less => println!("{}", "Too small".red()),
            Ordering::Greater => println!("{}", "Too big".red()),
            Ordering::Equal => {
                println!("{}", "You win".white());
                println!("{}", format!("Number of guesses: {}", number_of_guesses).white());
                break;
            },
        }
    }
}