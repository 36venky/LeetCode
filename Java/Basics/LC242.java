package Java.Basics;

public class LC218 {
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
        LC218 obj = new LC218();
        String s = "anagram";
        String t = "naiaram";
        boolean result = obj.validAnagram(s, t);
        System.out.println(result);
    }
    
}
