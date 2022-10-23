// ********************************************************************************
// Real POU
// ********************************************************************************

FUNCTION_BLOCK TC082
  VAR_INPUT
    IN : BOOL;
	PT : INT;
  END_VAR
  VAR_OUTPUT
    Q : BOOL;
	ET : INT;
  END_VAR
  VAR
    CYCLE : INT;
    TIMER : INT;
    TIMERN : INT;
    GE7_OUT : BOOL;
    ADD8_OUT : INT;
    SEL3_OUT : INT;
    SEL5_OUT : INT;
    SEL2_OUT : INT;
    SEL6_OUT : INT;
    SEL1_OUT : BOOL;
    SEL4_OUT : BOOL;
  END_VAR

  GE7_OUT := GE(TIMER, PT);
  ADD8_OUT := ADD(TIMER, CYCLE);
  SEL3_OUT := SEL(GE7_OUT, TIMER, ADD8_OUT);
  SEL5_OUT := SEL(IN, SEL3_OUT, 0);
  SEL2_OUT := SEL(GE7_OUT, PT, TIMER);
  SEL6_OUT := SEL(IN, SEL2_OUT, 0);
  SEL1_OUT := SEL(GE7_OUT, true, false);
  SEL4_OUT := SEL(IN, SEL1_OUT, false);
  Q := SEL4_OUT;
  ET := SEL6_OUT;
  TIMERN := SEL5_OUT;
  TIMER := TIMERN;
END_FUNCTION_BLOCK