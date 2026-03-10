#include <stdlib.h>
#include <stdio.h>

#define FACE
#include "math.lib.c"
#include "greeter.lib.c"
#undef FACE

void CLI(void){
  int base_count = Math·add(1 ,2);
  printf("Calculated base loop count: %d\n" ,base_count);
  Greet·hello_loop(base_count);
}

int main(int argc ,char **argv){
  (void)argc;
  (void)argv;
  
  CLI();
  
  return EXIT_SUCCESS;
}
