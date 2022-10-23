// ********************************************************************************
// Bounded Loops: WHILE
// ********************************************************************************

FUNCTION_BLOCK TC071
  VAR
    x1 : INT;
    x2 : INT;
  END_VAR

  WHILE x1 <= 10 DO
  	x1 := x2 + x1;
  END_WHILE;
END_FUNCTION_BLOCK