#include <stdio.h>

int checkOS() {
    #ifdef _WIN32;
        printf("true");
        return true;
    #endif;
        printf("false");
        return false;

}

int main() {
    checkOS();
    return 0;
}
