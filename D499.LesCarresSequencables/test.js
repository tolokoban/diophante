var Pavage = require("./pavage");


function find(n, f, solution) {
    if( typeof solution === 'undefined' ) solution = [];
    if( solution.length >= n ) {
        f( solution );
        return;
    }
    var previous = solution.length == 0 ? 0 : solution[solution.length - 2];
    var a, b;
    for( a = previous + 1 ; a < n ; a++ ) {
        if( solution.indexOf( a ) == -1 ) {
            solution.push( a );
            for( b = a + 1 ; b <= n ; b++ ) {
                if( solution.indexOf( b ) == -1 ) {
                    solution.push( b );
                    find( n, f, solution );
                    solution.pop( b );
                }
            }
            solution.pop( a );
        }
    }
}


function tile( cfg, pav ) {
    var nbRects = cfg.length;
    if( pav.index >= nbRects ) {
        print( pav.toString() );
        return;
    }
    var r = cfg[pav.index];
    var w = r[0];
    var h = r[1];

    if( pav.index == 0 ) {
        var x, y;
        var hh = (pav.size - h) / 2;
        var ww = (pav.size - w) / 2;
        for( y = 0 ; y < hh ; y++ ) {
            for( x = 0 ; x < ww ; x++ ) {
                if( pav.test( x, y, w, h ) ) {
                    pav.push( x, y, w, h );
                    tile( cfg, pav );
                    pav.pop();
                }
            }
        }
    } else {
        tile2( cfg, pav, w, h );
        tile2( cfg, pav, h, w );
    }
}

function tile2( cfg, pav, h, w ){
    var x, y;
    for( y = 0 ; y < pav.size - h + 1 ; y++ ) {
        for( x = 0 ; x < pav.size - w + 1 ; x++ ) {
            if( pav.test( x, y, w, h ) ) {
                pav.push( x, y, w, h );
                tile( cfg, pav );
                pav.pop();
            }
        }
    }
}

//tile( config, new Pavage( 12, config.length ) );

function print() {
    var i, out = '';
    for (i = 0 ; i < arguments.length ; i++) {
        out += arguments[i];
    }
    console.log( out );
    console.error( out );
}

var count = 0;
for( var size=10 ; size < 31 ; size+=2 ) {
    print( "# size: ", size );
    find( size, function(s) {
        var total = 0;
        var a = 0;
        var cfg = [];
        s.forEach(function (x, idx) {
            if( idx % 2 == 0 ) {
                a = x;
            } else {
                total += x * a;
                cfg.push( [a, x] );
            }
        });
        var sqrt = Math.sqrt( total );
        if( Math.floor( sqrt ) == sqrt ) {
            print( "## ", sqrt + '^2 ', s );
            tile( cfg, new Pavage( sqrt, cfg.length ) );
            count++;
        }
    });
}

console.log( "Count: " + count );
