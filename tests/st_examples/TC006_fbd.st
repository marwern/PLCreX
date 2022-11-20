FUNCTION_BLOCK TC006
  VAR_INPUT
    i1 : BOOL;
    i2 : BOOL;
  END_VAR
  VAR_OUTPUT
    o1 : BOOL;
    o2 : BOOL;
    o3 : BOOL;
  END_VAR
  VAR
    l1 : BOOL;
    l2 : TIME := T#5s;
    TON0 : TON;
    AND1_OUT : BOOL;
    XOR3_OUT : BOOL;
    OR13_OUT : BOOL;
  END_VAR

  AND1_OUT := AND(i1, i2);
  TON0(AND1_OUT, l2);
  XOR3_OUT := XOR(AND1_OUT, TON0.Q);
  l1 := XOR3_OUT;
  o1 := TON0.Q;
  o2 := i1;
  OR13_OUT := OR(i2, l1);
  o3 := OR13_OUT;
END_FUNCTION_BLOCK