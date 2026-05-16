let x = "global";

if (true) {
    //TDZ for block-scoped "x" starts here
    //
    let x = "block";
    console.log(x);
}
