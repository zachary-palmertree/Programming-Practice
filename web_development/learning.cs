using System;

namespace HelloWorld{
    class Program{
        static void Main(string[] args){
            Console.WriteLine("Hello, World!");

            // Variables and Data Types
            int number = 10;
            string name = "Alice";
            float price = 19.99f;

            // Control Structures
            if(number > 5){
                Console.WriteLine("Number is greater than 5");
            }
            else{
                Console.WriteLine("Number is 5 or less");
            }

            for(int i = 0; i < 5; i++){
                Console.WriteLine(i);
            }

            // OOP
            // in a different class
        }
    }

    class Person{
        public string Name {get; set;}
        public int Age {get; set;}

        public void Introduce(){
            Console.WriteLine($"Hi, I'm {Name} and I'm {Age} years old.");
        }

        // Advaned Topics
        // Inheritance
        // Polymorphism
        // LINQ
        

        // PRACTICE
        // build small projects
        // look at libraries and frameworks

        // Small Project - calculator
        
    }
}