// ********************************************************************************
// Program Organization Units: PROGRAM
// ********************************************************************************

PROGRAM TC001
  VAR_INPUT
    x1 : INT;
  END_VAR
  VAR_OUTPUT
    x2 : INT;
  END_VAR
  VAR
    x3 : INT := 3;
  END_VAR

  x2:=x1+x3;
END_PROGRAM