// ********************************************************************************
// Interface Declaration List: VAR_EXTERNAL
// ********************************************************************************

FUNCTION_BLOCK TC011
  VAR_EXTERNAL
    global : BOOL;
  END_VAR
  VAR
    x1 : BOOL;
  END_VAR

  x1 := global;
END_FUNCTION_BLOCK