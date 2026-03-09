#ifndef MATH_LIB_C
#define MATH_LIB_C

#ifndef FACE
  #define MATH_IMPL
#endif

int Math·add(int a ,int b);

#ifdef MATH_IMPL

int Math·add(int a ,int b){
  return a + b;
}

#endif // MATH_IMPL
#endif // MATH_LIB_C
