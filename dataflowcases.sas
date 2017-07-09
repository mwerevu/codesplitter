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



/* DATA block with multiple SET inputs
multiple spacing configurations */
data temp1;
     set temp2 temp3;
run;

data temp1 temp2(drop=b);
     set
	temp2(keep=a)
	temp3(keep=b)
	;
run;

data temp1 temp2(drop=b);
     merge
	temp2(keep=a)
	temp3(keep=b)
	;
run;


/* PROC FREQ */
proc freq data=temp1;
     tables b / out=OUTPUTS.freqout;
run;
/* PROC MEANS */
proc means data=temp1;
     output out=meansout sum(b)=;
run;
/* PROC SUMMARY */
proc summary data=temp1;
     output out=summout sum(b)=;
run;
/* PROC IMPORT */
proc import datafile="temp1.csv"
     out=summout
     DBMS=CSV
     REPLACE;
run;
/* PROC EXPORT */
proc export data=temp1
     outfile="export.csv"
     DBMS=CSV
     REPLACE;
run;     
