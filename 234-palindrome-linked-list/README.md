Given the head of a singly linked list, return true if it is a 
palindrome  or false otherwise.

## Fast and Slow Pointers

to find the middle node of a singly linked list:

1) Two pointers slow and fast are initialized to the head node of the linked list.

2) A while loop is used to iterate over the linked list, with the condition that both fast and fast.next are not None. This is because fast moves two steps at a time, while slow moves only one step at a time, so if fast.next is None, it means that fast has reached the end of the linked list and there is no middle node.

3) Inside the loop, slow moves one step forward by setting it to slow.next, while fast moves two steps forward by setting it to fast.next.next. This way, when fast reaches the end of the linked list, slow will be pointing to the middle node.

```
# find the middle node using fast and slow pointers
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
```

## Example
Suppose we have the following linked list:
```
1 -> 2 -> 3 -> 4 -> 5 -> None
```
- Initially, both slow and fast are set to the head node 1.
- In the first iteration of the loop, slow is set to 2 and fast is set to 3.
- In the second iteration of the loop, slow is set to 3 and fast is set to 5.
- In the third iteration of the loop, slow is set to 4 and fast is set to None.
- Since fast is None, the loop exits and slow is pointing to the middle node 3.

