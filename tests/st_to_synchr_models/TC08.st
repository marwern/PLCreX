FUNCTION_BLOCK TC08 // _datatypes
  VAR
    x0 : BOOL;
    x1 : BOOL := TRUE;
    x2 : INT;
    x3 : INT := 2;
    x4 : REAL;
    x5 : REAL := 1.23;
    x7 : TIME;
    x8 : TIME := t#5s;
    x9 : ARRAY [1..2] OF BOOL;
    x10 : ARRAY [1..2] OF INT;
    x11 : ARRAY [1..2] OF REAL;
    x12 : ARRAY [1..2] OF TIME;
  END_VAR

  x0 := x1;
  x2 := x3;
  x4 := x5;
  x7 := x8;
  x9[0]:=TRUE;
  x10[0]:=2;
  x11[0]:=1.23;
  x12[0]:=t#2s;
END_FUNCTION_BLOCK