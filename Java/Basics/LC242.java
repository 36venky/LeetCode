package Java.Basics;

public class LC242 {
    public boolean validAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }

        int[] charCount = new int[26];

        for (int i = 0; i < s.length(); i++) {
            charCount[s.charAt(i) - 'a']++;
            charCount[t.charAt(i) - 'a']--;
        }

        for (int count : charCount) {
            if (count != 0) {
                return false;
            }
        }

        return true;
    }

    public static void main(String[] args){
        LC242 obj = new LC242();
        String s = "anagram";
        String t = "naiaram";
        boolean result = obj.validAnagram(s, t);
        System.out.println(result);
    }
    
}
/*
Time Complexity: O(n) where n is the length of the strings.
Space Complexity: O(1) since the size of the character count array is fixed (26)
 */