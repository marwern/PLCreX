// ********************************************************************************
// Bounded Loops: FOR
// ********************************************************************************

FUNCTION_BLOCK TC070
  VAR
    x2 : INT;
  END_VAR

  FOR x1:=0 TO 10 DO
  	x2 := x1;
  END_FOR;
END_FUNCTION_BLOCK