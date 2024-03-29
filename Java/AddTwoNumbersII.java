/*
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
*/

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class AddTwoNumbersII {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode number = null;
        Stack<Integer> s1 = new Stack<Integer>();
        Stack<Integer> s2 = new Stack<Integer>();
        int val = 0;
        
        while(l1 != null){
            s1.push(l1.val);
            l1=l1.next;
        }
        
        while(l2 != null){
            s2.push(l2.val);
            l2=l2.next;
        }
        
        while(!s1.isEmpty()||!s2.isEmpty()){
            if(!s1.isEmpty())
                val += s1.pop();
            if(!s2.isEmpty())
                val += s2.pop();
            
            
            number = new ListNode(val%10, number);
            val = val/10;
        }
        return val>0 ? new ListNode(val, number) : number;
    }
}