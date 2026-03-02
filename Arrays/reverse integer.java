class Solution {
    public int reverse(int x) {
        int rev = 0;

        while (x != 0) {
            int digit = x % 10;   // get last digit
            rev = rev * 10 + digit; // add to reverse
            x = x / 10;  // remove last digit
        }

        return rev;
    }
}
