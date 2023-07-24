// ********************************************************************************
// Real POU
// ********************************************************************************

FUNCTION_BLOCK TC080
	VAR_INPUT
		S1 : BOOL;
		R : BOOL;
	END_VAR
	VAR_OUTPUT
		Q1 : BOOL;
	END_VAR

	Q1 := S1 XOR (Q1 AND NOT R);
END_FUNCTION_BLOCK