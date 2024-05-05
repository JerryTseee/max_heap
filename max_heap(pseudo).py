max_heapify(A, i){

    largest = i; #initialize the first position index
    
    if (i > n/2){
        #n/2 position is the last place that has child, so here shows i reach the end of the tree
        return
    }

    left = 2*i;
    if A[left] > A[i]:
        #left child larger than parent
        largest = left; #update the largest index
    
    if (2*i+1 <= n):#check that right child exist
        right = 2*i+1
        if A[right] > A[largest]:
            largest = right; #update the largest index
    
    if largest != i:#if there is a change to the largest index, then we need to update the maximum value
        swap (A[i], A[largest]);
        max_heapify(A,largest);#recursively call the function
}

build_max_heap(A){
    for i = n/2 downto 1:
        max_heapify(A, i);
}


get_maximum(A){
    #get the maximum value in a max-heap
    return A[0];
}

#insert a new value into the heap
insert(A,x){
    A[size + 1] = x; #append to the new value
    size ++;
    i = size
    while i > 1 and A[i] > A[i/2]:#while it is larger than the parent
        swap(A[i], A[i/2]);
        i = i/2;#update the position index
}

heap_sort(A){
    build_heap(A)
    for i = 1 to n:
        temp = max(A);
        A [n-i+1] = temp;
        A --;
        rebuild the heap;
}