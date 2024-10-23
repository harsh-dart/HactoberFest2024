package org.problems.strings;

import java.util.HashMap;

public class Isomorphic {

    public static void main(String[] args) {
        System.out.println(isIsomorphic("abc","aaa"));
    }
    public static boolean isIsomorphic(String s, String t) {

        HashMap<Character, Character> mp1 = new HashMap<>();
        HashMap<Character, Character> mp2 = new HashMap<>();
        if (s.length() != t.length())
            return false;
        for (int i = 0; i < s.length(); i++) {
            if (mp1.containsKey(s.charAt(i)) || mp2.containsKey(t.charAt(i))) {
                if ( (mp1.get(s.charAt(i)) != null && mp1.get(s.charAt(i))!=t.charAt(i)) || (mp2.get(t.charAt(i))!=null && mp2.get(t.charAt(i))!=s.charAt(i)))
                    return false;
            } else {
                mp1.put(s.charAt(i), t.charAt(i));
                mp2.put(t.charAt(i), s.charAt(i));
            }
        }
        return true;
    }
}
