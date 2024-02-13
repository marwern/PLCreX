FUNCTION_BLOCK TC13 //_arithmeticOperators
  VAR
    x0 : REAL;
    x1 : REAL := 1.0;
    x2 : REAL := 2.0;
    x3 : INT := 1;
    x4 : INT := 2;
    x5 : INT;
  END_VAR

  x0 := x1 + x2;
  x0 := ADD(x1, x2);
  x0 := x1 - x2;
  x0 := SUB(x1, x2);
  x0 := x1 * x2;
  x0 := MUL(x1, x2);
  x0 := x1 / x2;
  x0 := DIV(x1, x2);
  x0 := EXPT(x1, x2);
  x5 := MOD(x3, x4);
END_FUNCTION_BLOCK