#include <stdio.h>

int search(int lst[], int n, int x) {
    int i;
    for (i = 0; i < n; i++){
        if (lst[i] == x)
            return i;
    }
    return -1;
}

int main(void) {
    int lst[] = {10, 7, 11, 5, 3, 8};
    int x = 5;
    int n = sizeof(lst) / sizeof(lst[0]);
    int result = search(lst, n, x);
    int result = search(lst, n, x);
    (result == -1) ? printf("Not found.") : printf("Found at index %d", result);
    return 0;
}