PROGRAM TC085
  VAR_INPUT
    a: INT;
    b: INT;
  END_VAR
  VAR_OUTPUT
    gcd:INT;
  END_VAR
  VAR
    c: INT;
    d: INT;
  END_VAR

    c:=a;
    d:=b;

    IF (c=0) THEN
        gcd := d;

    ELSE
        WHILE (d <>0) DO
            IF (c>d) THEN
                c := c-d;
            ELSE
                d := d-c;
            END_IF;
        END_WHILE;
        gcd := c;
    END_IF;
END_PROGRAM