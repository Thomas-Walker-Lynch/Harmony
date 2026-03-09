#ifndef GREETER_LIB_C
#define GREETER_LIB_C
#ifndef FACE
  #define GREETER_IMPL
#endif

#define FACE
#include "math.lib.c"
#undef FACE

void Greet·hello_loop(int count);

#ifdef GREETER_IMPL

#include <stdio.h>

void Greet·hello_loop(int count){
  for(int TM = 0; TM < count; ++TM){
    int current_count = Math·add(TM ,1);
    printf("Hello iteration: %d\n" ,current_count);
  }
}

#endif // GREETER_IMPL
#endif // GREETER_LIB_C

