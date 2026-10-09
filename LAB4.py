# LAB4
# REMINDER: The work in this assignment must be your own original work and must be completed alone.

class Node:   # You are not allowed to modify this class
    def __init__(self, value=None):  
        self.next = None
        self.value = value
    
    def __str__(self):
        return f"Node({self.value})"

    __repr__ = __str__

class Malloc_Library:

    """
    ** This is NOT a comprehensive test sample, test beyond this doctest
        >>> lst = Malloc_Library()
        >>> lst
        <BLANKLINE>
        >>> lst.malloc(5)
        >>> lst
        None -> None -> None -> None -> None
        >>> lst[0] = 23
        >>> lst
        23 -> None -> None -> None -> None
        >>> lst[0]
        23
        >>> lst[1]
        >>> lst.realloc(1)
        >>> lst
        23
        >>> lst.calloc(5)
        >>> lst
        0 -> 0 -> 0 -> 0 -> 0
        >>> lst.calloc(10)
        >>> lst[3] = 5
        >>> lst[8] = 23
        >>> lst
        0 -> 0 -> 0 -> 5 -> 0 -> 0 -> 0 -> 0 -> 23 -> 0
        >>> lst.realloc(5)
        >>> lst
        0 -> 0 -> 0 -> 5 -> 0
        >>> other_lst = Malloc_Library()
        >>> other_lst.realloc(9)
        >>> other_lst[0] = 12
        >>> other_lst[5] = 56
        >>> other_lst[8] = 6925
        >>> other_lst[10] = 78
        Traceback (most recent call last):
            ...
        IndexError
        >>> other_lst.memcpy(2, lst, 0, 5)
        >>> lst
        None -> None -> None -> 56 -> None
        >>> other_lst
        12 -> None -> None -> None -> None -> 56 -> None -> None -> 6925
        >>> temp = lst.head.next.next
        >>> lst.free()
        >>> temp.next is None
        True
    """

    def __init__(self): # You are not allowed to modify the constructor
        self.head = None
    
    def __repr__(self):  # You are not allowed to modify this method
        current = self.head
        out = []
        while current != None:
            out.append(str(current.value))
            current = current.next
        return " -> ".join(out)

    __str__ = __repr__
    
    def __len__(self):
        # --- YOUR CODE STARTS HERE
        count = 0
        curr = self.head
        while curr is not None:
            count += 1
            curr = curr.next
        return count 

    def __setitem__(self, pos, value):
        # --- YOUR CODE STARTS HERE
        curr = self.head
        curr_idx = 0
        if self.head is None or pos < 0:
            raise IndexError("Index out of range")
        while curr is not None and curr_idx < pos:
            curr = curr.next
            curr_idx += 1  
        if curr is None:
            raise IndexError("Index out of range")
        curr.value = value 

    def __getitem__(self, pos):
        # --- YOUR CODE STARTS HERE
        if self.head is None or pos < 0:
            raise IndexError("Index out of range")
        curr = self.head
        curr_idx = 0
        while curr is not None and curr_idx < pos:
            curr = curr.next
            curr_idx += 1 
        if curr is None:
            raise IndexError("Index out of range")   
        return curr.value
    

    def malloc(self, size):
        # --- YOUR CODE STARTS HERE
        self.free()
        if size <= 0:
            return
        self.head = Node(None)
        curr = self.head
        count = 1
        while count < size:
            curr.next = Node(None)
            curr = curr.next
            count += 1

    def calloc(self, size):
        # --- YOUR CODE STARTS HERE
        self.free()
        if size <= 0:
            return
        self.head = Node(0)
        curr = self.head
        count = 1
        while count < size:
            curr.next = Node(0)
            curr = curr.next
            count += 1

    def free(self):
        # --- YOUR CODE STARTS HERE
        curr = self.head
        self.head = None
        while curr is not None:
            nxt = curr.next
            curr.next = None
            curr = nxt

    def realloc(self, size):
        # --- YOUR CODE STARTS HERE
        if size == 0:
            self.free()
            return
        if self.head is None:
            self.malloc(size)
            return
        current_size = len(self)
        if size > current_size:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            count = current_size
            while count < size:
                curr.next = Node(None)
                curr = curr.next
                count += 1
        elif size < current_size:
            curr = self.head
            count = 1
            while count < size:
                curr = curr.next
                count += 1 
            to_remove = curr.next
            curr.next = None
            while to_remove is not None:
                nxt = to_remove.next
                to_remove.next = None
                to_remove = nxt 

    def memcpy(self, ptr1_start_idx, pointer_2, ptr2_start_idx, size):
        # --- YOUR CODE STARTS HERE
        size_1 = len(self)
        size_2 = len(pointer_2)
        if (size_1 == 0 or size_2 == 0 or ptr1_start_idx < 0 or ptr1_start_idx >= size_1 or ptr2_start_idx < 0 or ptr2_start_idx >= size_2 or size <= 0):
            return
        src_curr = self.head
        idx1 = 0
        while src_curr is not None and idx1 < ptr1_start_idx:
            src_curr = src_curr.next
            idx1 += 1
        dest_curr = pointer_2.head
        idx2 = 0
        while dest_curr is not None and idx2 < ptr2_start_idx:
            dest_curr = dest_curr.next
            idx2 += 1
        copied = 0
        while src_curr is not None and dest_curr is not None and copied < size:
            dest_curr.value = src_curr.value
            src_curr = src_curr.next
            dest_curr = dest_curr.next
            copied += 1
    
def run_tests():
    import doctest
    doctest.testmod(verbose=True)
     

if __name__ == "__main__":
     run_tests()