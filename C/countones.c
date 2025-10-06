
#include <stdio.h>

int countSetBits(int n){
        int setbits = 0;
        
        while (n) {
            
            if (n & 1) {
                setbits ++;
            }
            n >>= 1;
        }
        return setbits;
}

int main() {
    int number;
    printf("Welcome to the CountOnes program.n");
 
    printf("Please enter a number:");
    
    scanf("%d",&number);
    

    int results = countSetBits(number);
    
    printf("The number of bits set is: %d\n", results );
    
    return 0;
 
}