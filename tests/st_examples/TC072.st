// ********************************************************************************
// Bounded Loops: REPEAT UNTIL
// ********************************************************************************

FUNCTION_BLOCK TC072
  VAR
    x1 : INT;
    x2 : INT;
  END_VAR

  REPEAT
  	x1 := 5 + x2;
  UNTIL x1 > 10
  END_REPEAT;
END_FUNCTION_BLOCK