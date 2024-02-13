FUNCTION_BLOCK TC11 // _inEquality
  VAR
    x0 : BOOL;
    x1 : BOOL := TRUE;
    x2 : BOOL := FALSE;
  END_VAR

  x0 := x1 = x2;
  x0 := EQ(x1,x2);
  x0 := x1 <> x2;
  x0 := NE(x1,x2);
END_FUNCTION_BLOCK