FUNCTION_BLOCK TC006
  VAR_INPUT
    i1 : BOOL;
    i2 : BOOL;
    i3 : BOOL;
    i4 : BOOL;
  END_VAR
  VAR_OUTPUT
    o1 : BOOL;
    o2 : BOOL;
    o3 : BOOL;
    o4 : BOOL;
    o5 : BOOL;
  END_VAR
  VAR
    l1 : BOOL;
    l2 : TIME := T#5s;
    l3 : TIME := T#2s;
    l4 : BOOL;
    TON0 : TON;
    TOF0 : TOF;
    AND1_OUT : BOOL;
    XOR3_OUT : BOOL;
    OR13_OUT : BOOL;
  END_VAR

  AND1_OUT := AND(i1, i2);
  TON0(IN := AND1_OUT, PT := l2);
  XOR3_OUT := XOR(AND1_OUT, TON0.Q);
  l1 := XOR3_OUT;
  o1 := TON0.Q;
  o2 := i1;
  OR13_OUT := OR(i2, i1);
  TOF0(IN := OR13_OUT, PT := l3);
  o3 := TOF0.Q;
  l4 := i2;
  o4 := i3;
END_FUNCTION_BLOCK


CONFIGURATION config

  RESOURCE resource1 ON PLC
  END_RESOURCE
END_CONFIGURATION
