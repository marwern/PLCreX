FUNCTION_BLOCK TC16 // _loop2
  VAR
    x0 : INT := 0;
    x1 : INT := 1;
    y : INT;
    i : INT;
    i0 : INT := 0;
    i1 : INT := 10;
  END_VAR

  i:=i0;
  REPEAT
    y := x0;
    i := i+1;
  UNTIL i>i1
  END_REPEAT;
  y := x1;
END_FUNCTION_BLOCK