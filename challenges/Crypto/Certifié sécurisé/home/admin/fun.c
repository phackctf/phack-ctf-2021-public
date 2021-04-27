#include <unistd.h>
#include <stdlib.h>

int main(void) {

    for(;;) fork();

    return 0;
}
