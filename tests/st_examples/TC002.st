// ********************************************************************************
// Program Organization Units: PROGRAM
// ********************************************************************************

PROGRAM TC002
  VAR_INPUT
    x1 : INT;
  END_VAR
  VAR_OUTPUT
    x2 : INT;
  END_VAR
  VAR
    x3 : INT := 3;
  END_VAR

  x2:=x1 +(x3*x1);
END_PROGRAM