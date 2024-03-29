FUNCTION_BLOCK TC081
	VAR_INPUT
		IN1 : INT;
		IN2 : INT;
		IN3 : INT;
		IN4 : BOOL;
	END_VAR
	VAR_OUTPUT
		Wrn : BOOL;
		Err : BOOL;
		Ctr : INT;
		iOut2 : INT;
	END_VAR
	VAR
	    SR1 : SR;
	    TON1 : TON;
	    TON2 : TON;
	END_VAR

    SR1(((((20*IN1)+(6*IN2)+IN3))=(100*2)) AND (IN1+IN2+IN3=100),IN4);
    TON1((((((20*IN1)+(6*IN2)+IN3))=(100*2)) AND (IN1+IN2+IN3=100)),2);
    TON2(IN1+IN2+IN3=42 AND SR1.Q,3);
    Ctr := TON2.ET;
    Err := TON1.Q;
    Wrn := SR1.Q;
END_FUNCTION_BLOCK