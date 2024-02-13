FUNCTION_BLOCK TC21
  VAR_OUTPUT
    y : INT;
  END_VAR
  VAR
    x : INT := 1;
    i : INT;
    i0 : INT := 0;
    i1 : INT := 10;
  END_VAR

  i:=i0;
  REPEAT
    y := i;
    i := i+1;
  UNTIL i>i1
  END_REPEAT;
  y := x;
END_FUNCTION_BLOCK