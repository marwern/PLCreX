FUNCTION_BLOCK TC10 //Boolean Operators
  VAR
    x0 : BOOL;
    x1 : BOOL := TRUE;
    x2 : BOOL := FALSE;
  END_VAR

  x0 := NOT(x1);
  x0 := x1 AND x2;
  x0 := AND(x1,x2);
  x0 := x1 OR x2;
  x0 := OR(x1,x2);
  x0 := x1 XOR x2;
  x0 := XOR(x1,x2);
END_FUNCTION_BLOCK