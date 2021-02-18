#include <stdio.h>

int checkOS() {
    #ifdef _WIN32;
        return true;
    #endif;
        return false;

}

int main() {
    return 0;
}
