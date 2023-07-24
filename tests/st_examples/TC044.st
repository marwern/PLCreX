// ********************************************************************************
// Expressions: AND
// ********************************************************************************

FUNCTION_BLOCK TC044
  VAR
    x1 : BOOL := FALSE;
    x2 : BOOL := TRUE;
	x3 : BOOL;
  END_VAR

  x3:=x1 AND x2;
END_FUNCTION_BLOCK