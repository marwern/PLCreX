// ********************************************************************************
// Conditional Statements: IF ELSE
// ********************************************************************************

FUNCTION_BLOCK TC068
  VAR
    x1 : BOOL := TRUE;
    x2 : INT := 5;
	x3 : INT;
  END_VAR

  IF x1 THEN
    x3:=x2;
  ELSIF x2 = 5 THEN
    x3:=-x2;
  ELSE
    x3:=2*x2;
  END_IF;
END_FUNCTION_BLOCK