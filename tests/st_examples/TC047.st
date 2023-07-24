// ********************************************************************************
// Expressions: XOR
// ********************************************************************************

FUNCTION_BLOCK TC047
  VAR
    x1 : BOOL := FALSE;
    x2 : BOOL := TRUE;
	x3 : BOOL;
  END_VAR

  x3:=x1 XOR x2;
END_FUNCTION_BLOCK