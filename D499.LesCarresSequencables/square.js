var COLORS = [
    'red', 'green', 'blue', 'cyan', 'magenta', 'yellow', 'lightgray'
];

module.exports = function() {
    if( !Array.isArray( this.arg ) ) {
        this.fatal( "[square] Expecting an array as argument!" );
    } else {
        var z = .4;  // zoom
        var maxW = 0, maxH = 0;
        var x, y, w, h;
        var ang;
        var i;
        for( i=0 ; i<this.arg.length ; i+=4 ) {
            x = this.arg[i + 0];
            y = this.arg[i + 1];
            w = this.arg[i + 2];
            h = this.arg[i + 3];
            maxW = Math.max( maxW, w + x );
            maxH = Math.max( maxH, h + y );
        }

        this.flush( '\\noindent' );
        this.begin( 'pspicture', '(-.2,-.2)(', .2 + maxW * z , ',', .2 + maxH * z, ')\n' );
        this.flush( '\\psframe[fillstyle=solid,fillcolor=white,linewidth=1pt](0,0)(', 
                    z*maxW, ',', z*maxH, ')\n' );
        var colorIdx = 0;
        while( this.arg.length > 0 ) {
            ang = 180 * this.arg.length / (this.arg.length + 4);
            x = this.arg.shift();
            y = this.arg.shift();
            w = this.arg.shift();
            h = this.arg.shift();
            this.flush( '\\psframe[linewidth=.5pt,fillstyle=vlines,hatchcolor=',
                        COLORS[colorIdx % COLORS.length], ',',
                        'hatchangle=' , ang, ']',
                        '(', z*x, ',', z*y, ')(', z*(x+w), ',', z*(y+h), ')\n' );
            this.flush( '\\rput(', z*(x+w/2), ',', z*(y+h/2), ')' );
            this.flush( 
                '{',
                h < 2 || w < 2 ? '\\tiny' : '',
                '\\psframebox*{', w, 'x', h, '}}\n' );
            colorIdx++;
        }
        this.flush( '\\psframe[fillstyle=none,linewidth=1pt](0,0)(', 
                    z*maxW, ',', z*maxH, ')\n' );
        this.end( 'pspicture' );
    }
}
