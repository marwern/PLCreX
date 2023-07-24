PROGRAM TC005
        VAR_INPUT
                i1 : BOOL;
                i2 : BOOL := FALSE;
                i3 : TIME;
        END_VAR
        VAR_OUTPUT
                o1 : BOOL := FALSE;
                o2 : BOOL := FALSE;
        END_VAR
        VAR
                o4 : BOOL;
                TON0 : TON;
                AND1_OUT : BOOL;
                XOR3_OUT : BOOL;
        END_VAR

        AND1_OUT := AND(i1,i2);
        TON0(AND1_OUT,i3);
        XOR3_OUT := XOR(AND1_OUT,TON0.Q);
        o1 := XOR3_OUT;
        o4 := TON0.Q;
        o2 := i1;
END_PROGRAM