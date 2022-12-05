# Reverse a LinkedList (easy)
# https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743784192_38Unit

# Problem Statement
#
# Given the head of a Singly LinkedList, reverse the LinkedList. Write a function to return the new head of the
# reversed LinkedList.
# Ex:
#
# Original List: head -> 2 -> 4 -> 6 -> 8 -> 10 -> null
# Reversed list: null <- 2 <- 4 <- 6 <- 8 <- 10 <- head

# Solution
#
# To reverse a LinkedList, we need to reverse one node at a time. We will start with a variable current which will
# initially point to the head of the LinkedList and a variable previous which will point to the previous node that we
# have processed; initially previous will point to null.
#
# In a stepwise manner, we will reverse the current node by pointing it to the previous before moving on to the next
# node. Also, we will update the previous to always point to the previous node that we have processed. Here is the
# visual representation of our algorithm:
#
# previous = null   current -> 2 -> 4 -> 6 -> 8 -> 10 -> null
#                  current = head, previous = null
# null <- 2 <- previous  current -> 4 -> 6 -> 8 -> 10 -> null
# null <- 2 <- 4 <- previous  current -> 6 -> 8 -> 10 -> null
# null <- 2 <- 4 <- 6 <- previous  current -> 8 -> 10 -> null
# null <- 2 <- 4 <- 6 <- 8 <- previous  current -> 10 -> null
# null <- 2 <- 4 <- 6 <- 8 <- 10 <- previous  current -> null
# null <- 2 <- 4 <- 6 <- 8 <- 10 <- head
