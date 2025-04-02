fn main() {
    // Print "Hello world!" to the console.
    println!("Hello, world!");

    // Declare a mutable variable.
    let mut x = 5;
    println!("The value of x is: {}", x);

    // Reassign the variable.
    x = 6;
    println!("The value of x is: {}", x);

    // Declare a constant.
    const THREE_HOURS_IN_SECONDS: u32 = 3 * 60 * 60;
    println!("Three hours in seconds: {}", THREE_HOURS_IN_SECONDS);

    // Data Types
    let guess: u32 = "42".parse().expect("Not a number!"); // unsigned 32 bit integer
    println!("guess: {}", guess);

    let y: f64 = 2.0; // f64
    println!("y: {}", y);

    let z = true; // boolean
    println!("z: {}", z);

    let c = 'z'; // character
    
}