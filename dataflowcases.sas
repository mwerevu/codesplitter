/* DATA block with single SET inputs
multiple spacing configurations */
data temp1;
    set temp2;
run;
data 
    temp1;
    set 
        temp2;
run;

data OUTPUTS.temp1(drop=a);
    set INPUTS.temp2(keep=c d);
    b=2;
run;

/* PROC MEANS */
proc freq data=temp1;
     tables b;
run;


/* DATA block with multiple SET inputs
multiple spacing configurations */
data temp1;
     set temp2 temp3;
run;

data temp1;
     set
	temp2(keep=a)
	temp3(keep=b)
	;
run;