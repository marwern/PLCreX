FUNCTION_BLOCK TC12 //_numericRelations
  VAR
    x0 : BOOL;
    x1 : INT := 1;
    x2 : INT := 2;
  END_VAR

  x0 := x1 < x2;
  x0 := LT(x1, x2);
  x0 := x1 <= x2;
  x0 := LE(x1, x2);
  x0 := x1 > x2;
  x0 := GT(x1, x2);
  x0 := x1 >= x2;
  x0 := GE(x1, x2);
END_FUNCTION_BLOCK