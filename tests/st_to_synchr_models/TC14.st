FUNCTION_BLOCK TC14 //_conditional
  VAR
    x0 : BOOL;
    x1 : BOOL := TRUE;
  END_VAR

  IF x1 THEN
    x0:=TRUE;
  ELSE
    x0:= FALSE;
  END_IF;

  x0 := SEL(x1,TRUE,FALSE);
END_FUNCTION_BLOCK