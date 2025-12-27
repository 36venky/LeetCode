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

/*
Time Complexity: O(n), where n is the number of elements in the input array nums. In the worst case, we may need to insert all n elements into the HashSet.
Space Complexity: O(n) in the worst case, when all elements are unique and we store all n elements in the HashSet.
 */