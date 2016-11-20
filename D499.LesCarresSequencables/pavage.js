


function Pavage( size, nbRects ) {
    this.size = size;
    this.rects = [];
    this.index = 0;
    while( nbRects --> 0 ) {
        this.rects.push( [0,0,0,0] );
    }
}

/**
 * @return void
 */
Pavage.prototype.contains = function(rect) {
    var r, ww, hh;
    var w = Math.min( rect[0], rect[1] );
    var h = Math.max( rect[0], rect[1] );
    for( var i = 0 ; i < this.index ; i++ ) {
        r = this.rects[i];
        ww = Math.min( r[2] - r[0], r[3] - r[1] );
        hh = Math.max( r[2] - r[0], r[3] - r[1] );
        if( ww == w && hh == h )
            return true;
    }
    return false;
};

/**
 * @return void
 */
Pavage.prototype.push = function(x, y, w, h) {
    var rect = this.rects[this.index];
    this.index++;
    rect[0] = x;
    rect[1] = y;
    rect[2] = x + w;
    rect[3] = y + h;
};

/**
 * @return void
 */
Pavage.prototype.pop = function() {
    this.index--;
};

/**
 * @return void
 */
Pavage.prototype.test = function(x1, y1, w, h) {
    var rect, i, j,
        x2 = x1 + w,
        y2 = y1 + h;
    for( var k = 0 ; k < this.index ; k++ ) {
        rect = this.rects[k];
        for( j = rect[1] ; j < rect[3] ; j++ ) {
            for( i = rect[0] ; i < rect[2] ; i++ ) {
                if( i >= x1 && i < x2 
                  && j >= y1 && j < y2 ) 
                {
                    return false;
                }
            }
        }
    }
    return true;
};

/**
 * @return void
 */
Pavage.prototype.toString = function() {
    var out = '{{square [';
    out += this.rects.slice( 0, this.index ).map(function(itm) {
        var x = itm[0], y = itm[1], w = itm[2], h = itm[3];
        return x + "," + y + "," + (w-x) + "," + (h-y);
    }).join(', ');
    return out += ']}}';
};



module.exports = Pavage;
