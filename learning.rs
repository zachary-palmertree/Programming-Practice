fn main() { // 1. This is the entry point of every Rust program.
    // Print "Hello world!" to the console.
    println!("Hello, world!"); // 2. println!() - This is a macro used for printing output to the console.
    // {} - are used as placeholders for values.

    // Declare a mutable variable.
    let mut x = 5; // 3. let - is used to declare variables
    println!("The value of x is: {}", x); // mut - keyword makes a variable mutable (changable).
    // Rust is statically typed, but often infers types.
    // Constants are declared using 'const' and must have their type annotated.

    // DATA TYPES
    // u32: Unsigned 32-bit integer
    // i32: Signed 32-bit integer.
    // f64: 64-bit floating-point number
    // bool: Boolean (true or false)
    // char: Single Unicode character
    // Tuples: Fixed-size collections of values of potentially different types.
    // Arrays: Fixed-size collections of values of the same type.

    // FUNCTIONS
    

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
    println!("c: {}", c);

    // Tuples
    let tup: (i32, f64, u8) = (500, 6.4, 1);
    let (a, b, c) tup;
    println!("The value of b is: {}", b);

    let five_hundred = tup.0;
    println!("five_hundred: {}", five_hundred);

    // Arrays
    let arr: [i32; 5] = [1, 2, 3, 4, 5];
    println!("arr[0]: {}", arr[0]);

    // Functions
    let result = add_numbers(10, 20);
    println!("10 + 20 = {}", result);

    // Control Flow
    if x > 5 {
        println!("x is greater than 5");        
    } else {
        println!("x is not greater than 5");
    }

    for element in arr.iter() {
        println!("element: {}", element);
    }

    for number in 1..4 { // 1, 2, 3
        println!("number: {}", number);
    }

    let mut count = 0;
    loop {
        count += 1;
        println!("count = {}", count);
        if count == 3 {
            break;
        }
    }

    let mut number = 3;
    while number != 0 {
        println!("{}", number);
        number = number - 1;
    }
    println!("LIFTOFF!!!");
}

fn add_numbers(a: i32, b: i32) -> i32 {
    a + b
}