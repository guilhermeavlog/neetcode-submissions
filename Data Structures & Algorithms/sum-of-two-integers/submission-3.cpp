class Solution {
public:
    int getSum(int a, int b) {
        /*
        1111
        1111

       11110 b
        1111 a
        

        

        */

        while (b != 0){
            int carry = (a & b) << 1;
            a = (a ^ b);
            b = carry;
            
        }
        return a;
    }
};
