#include <stdio.h>
#define SIZE 10
int main() {
//anonymous structure
struct {int x; int y;} a = {
.y = 7,
.x = 6,
};
printf("a.x = %d, a.y = %d\n", a.x, a.y);
// Less popular way of sparse array initialization
int array[SIZE] = {[5] 7, 19, [3] 17, 18};
for (int i = 0; i < SIZE; i++) {
printf("%d ", array[i]);
}
}