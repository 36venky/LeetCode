package Java.Basics;
import java.util.HashSet;

class LC217 {
    public boolean containsDuplicate(int[] nums) {
        HashSet<Integer> seenNumber = new HashSet<>();
        for (int num : nums){
            if (seenNumber.contains(num)){
                return true;
            }
            seenNumber.add(num);
        }
        return false;
    }
    public static void main(String[] args) {
        LC217 sol = new LC217();
        int[] nums = {1, 2, 3, 1};
        System.out.println("Hello!!"); // Output: true
        System.out.println(sol.containsDuplicate(nums)); // Output: true
    }
}