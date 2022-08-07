/*
Write an algorithm to determine if a number n is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Return True if n is a happy number, and False if not.

Example: 

Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
*/

class HappyNumber {    
    public boolean isHappy(int n) {
        // A set to store numbers during 
        // repeated square sum process 
        HashSet<Integer> s = new HashSet<Integer>(); 
        s.add(n); 
        
        // Keep replacing n with sum of 
        // squares of digits until we either 
        // reach 1 or we endup in a cycle 
        while (true)  
        { 

            // Number is Happy if we reach 1 
            if (n == 1) 
                return true; 

            // Replace n with sum of squares 
            // of digits 
            int sq = 0; 
            while (n > 0)  
            { 
                int digit = n % 10; 
                sq += digit * digit; 
                n = n / 10; 
            }
            
            n = sq;
     

            // If n is already visited, a cycle 
            // is formed, means not Happy 

            if ((s.contains(n) && n != (int)s.toArray()[ s.size()-1 ] )) 
                return false; 

            // Mark n as visited 
            s.add(n); 
        } 
    } 
}