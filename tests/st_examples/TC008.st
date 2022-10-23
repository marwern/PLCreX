// ********************************************************************************
// Interface Declaration List: VAR_INPUT
// ********************************************************************************

FUNCTION_BLOCK TC008
  VAR_INPUT
    x1 : BOOL := FALSE;
  END_VAR
  VAR
    x2 : BOOL := FALSE;
    x3 : BOOL := FALSE;
  END_VAR

  x2:=x1;
END_FUNCTION_BLOCK