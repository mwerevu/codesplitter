/*BEGINCCC
CCCEND*/
* some opening stuff;

/*BEGINCCC
testcode01.sas
Latex block
\begin{enumerate}
\item An item
\item Another item
\end{enumerate}

End of the Latex block
CCCEND*/

data temp;
    do i=1 to 10;
        output;
    end;
run;

/*BEGINCCC test block CCCEND*//*BEGINCCC another block CCCEND*/

/*
Not a Latex block.
*/

proc print data=temp;
run;

* Some other comment.;

/*BEGINCCC
Another Latex block.
CCCEND*/

* Some more stuff.;