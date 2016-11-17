var Perm = require("./perms");

var p = [2,3,4,5,6,7,8,9,10];
var count = 0;
while (p) {
    if (isValid(p)) {
        var value = p[0] + p[1]*p[2] + p[3]*p[4] + p[5]*p[6] + p[7]*p[8];
        if (Math.sqrt(value) == Math.floor(Math.sqrt(value))) {
            console.log("========================================");
        }
        console.log(
            "\\item $1 \\times " + p[0]
                + " + " + p[1] + " \\times " + p[2]
                + " + " + p[3] + " \\times " + p[4]
                + " + " + p[5] + " \\times " + p[6]
                + " + " + p[7] + " \\times " + p[8]
                + " = " + value + "$."
        );
        if (Math.sqrt(value) == Math.floor(Math.sqrt(value))) {
            console.log("----------------------------------------");
        }
        count++;
    }
    p = Perm(p);
}

console.log("Count: " + count);


function isValid(perm) {
    for (var k=1; k<perm.length; k++) {
        if (perm[k] > perm[k+1]) return false;
    }
    return true;
}



module.exports = function() {
    if (typeof this.arg !== 'number') {
        this.fatal( "A number is expected as argument!" );
    }

    var i;
    this.flush( "\begin{tabular}{|" );
    i = this.arg;
    while( i --> 0 ) {
        
    }
};
