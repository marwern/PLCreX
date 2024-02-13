FUNCTION_BLOCK TC15 //_loop1
  VAR
    x0 : INT := 0;
    x1 : INT := 1;
    y : INT;
    i : INT;
    i0 : INT := 0;
    i1 : INT := 10;
  END_VAR

  i:=i0;
  WHILE i<=i1 DO
    y := x0;
    i := i+1;
  END_WHILE;
  y := x1;
END_FUNCTION_BLOCK