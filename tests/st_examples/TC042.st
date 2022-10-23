// ********************************************************************************
// Expressions: AND
// ********************************************************************************

FUNCTION_BLOCK TC042
  VAR
    x1 : BOOL := TRUE;
    x2 : BOOL := FALSE;
	x3 : BOOL;
  END_VAR

  x3:=x1 AND x2;
END_FUNCTION_BLOCK