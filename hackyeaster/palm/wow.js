function checkEntries() {
    var u = document.getElementById('puser').value;
    var p = document.getElementById('ppass').value;
    if (u === 'yolo' && p === '1337') {
        document.location.href = 'challenge14_' + u + '_' + p + '.html';
    } else {
        alert('nope');
    }
}
// this was found beneath a simple function decleration for the above fake checkEntries():
var _0x549b=["value","puser","getElementById","ppass","rolo","length","charAt","href","location","challenge14_","_",".html","nope"];function checkEntries(){var u=document[_0x549b[2]](_0x549b[1])[_0x549b[0]];var p=document[_0x549b[2]](_0x549b[3])[_0x549b[0]];var ok=false;if(u===_0x549b[4]){if(p>0&&p[_0x549b[5]]==10){ok=true;for(i=0;i<=9;i++){var digit=p[_0x549b[6]](i);if(digit!=9-i){ok=false}}}};if(ok){document[_0x549b[8]][_0x549b[7]]=_0x549b[9]+u+_0x549b[10]+p+_0x549b[11]}else {alert(_0x549b[12])}};

// beautified:
var _0x549b = ["value", "puser", "getElementById", "ppass", "rolo", "length", "charAt", "href", "location", "challenge14_", "_", ".html", "nope"];

function checkEntries() {
    var u = document[_0x549b[2]](_0x549b[1])[_0x549b[0]];
    var p = document[_0x549b[2]](_0x549b[3])[_0x549b[0]];
    var ok = false;
    if (u === _0x549b[4]) {
        if (p > 0 && p[_0x549b[5]] == 10) {
            ok = true;
            for (i = 0; i <= 9; i++) {
                var digit = p[_0x549b[6]](i);
                if (digit != 9 - i) {
                    ok = false
                }
            }
        }
    };
    if (ok) {
        document[_0x549b[8]][_0x549b[7]] = _0x549b[9] + u + _0x549b[10] + p + _0x549b[11]
    } else {
        alert(_0x549b[12])
    }
};

// but that function is also a red herring, in the final <script> tag on the
// page, after many spaces so it doesn't show up in view-source (on firefox at least,
// chrome has word wrap)

eval(atob("ZXZhbChmdW5jdGlvbihwLGEsYyxrLGUsZCl7ZT1mdW5jdGlvbihjKXtyZXR1cm4gYy50b1N0cmluZygzNil9O2lmKCEnJy5yZXBsYWNlKC9eLyxTdHJpbmcpKXt3aGlsZShjLS0pe2RbYy50b1N0cmluZyhhKV09a1tjXXx8Yy50b1N0cmluZyhhKX1rPVtmdW5jdGlvbihlKXtyZXR1cm4gZFtlXX1dO2U9ZnVuY3Rpb24oKXtyZXR1cm4nXFx3Kyd9O2M9MX07d2hpbGUoYy0tKXtpZihrW2NdKXtwPXAucmVwbGFjZShuZXcgUmVnRXhwKCdcXGInK2UoYykrJ1xcYicsJ2cnKSxrW2NdKX19cmV0dXJuIHB9KCdyIHEoKXsyIHU9Ny44KFwnd1wnKS5iOzIgcD03LjgoXCd2XCcpLmI7MiA0PVswLDAsMCwwLDAsMCwwLDAsMCwwXTsyIDU9YzszKHU9PT1cJ2dcJyl7MyhwPjAmJnAuaD09OSl7NT1qO2YoaT0xO2k8PTk7aSsrKXsyIDY9cC5rKGktMSk7MiBhPXAuZSgwLGkpOzMoNFs2XSE9MHx8YSVpIT0wKXs1PWN9Myg0WzZdPT0wKXs0WzZdPTF9fX19Myg1KXs3Lm0ubj1cJ29cJyt1K1wneFwnK3ArXCcuc1wnfXR7ZChcJ2xcJyl9fScsMzQsMzQsJ3x8dmFyfGlmfHVzZWR8b2t8ZGlnaXR8ZG9jdW1lbnR8Z2V0RWxlbWVudEJ5SWR8MTB8cGFydHx2YWx1ZXxmYWxzZXxhbGVydHxzdWJzdHJpbmd8Zm9yfGVsc2F8bGVuZ3RofHx0cnVlfGNoYXJBdHxub3BlfGxvY2F0aW9ufGhyZWZ8Y2hhbGxlbmdlMTRffHxjaGVja0VudHJpZXN8ZnVuY3Rpb258aHRtbHxlbHNlfHxwcGFzc3xwdXNlcnxfJy5zcGxpdCgnfCcpLDAse30pKQ=="));
// which decodes to:
eval(function(p,a,c,k,e,d){e=function(c){return c.toString(36)};if(!''.replace(/^/,String)){while(c--){d[c.toString(a)]=k[c]||c.toString(a)}k=[function(e){return d[e]}];e=function(){return'\\w+'};c=1};while(c--){if(k[c]){p=p.replace(new RegExp('\\b'+e(c)+'\\b','g'),k[c])}}return p}('r q(){2 u=7.8(\'w\').b;2 p=7.8(\'v\').b;2 4=[0,0,0,0,0,0,0,0,0,0];2 5=c;3(u===\'g\'){3(p>0&&p.h==9){5=j;f(i=1;i<=9;i++){2 6=p.k(i-1);2 a=p.e(0,i);3(4[6]!=0||a%i!=0){5=c}3(4[6]==0){4[6]=1}}}}3(5){7.m.n=\'o\'+u+\'x\'+p+\'.s\'}t{d(\'l\')}}',34,34,'||var|if|used|ok|digit|document|getElementById|10|part|value|false|alert|substring|for|elsa|length||true|charAt|nope|location|href|challenge14_||checkEntries|function|html|else||ppass|puser|_'.split('|'),0,{}))"

// didn't fancy that, so I set a breakpoint in chrome debugger tools to get the
// deobfuscated result (beautified):

function checkEntries() {
    var u = document.getElementById('puser').value;
    var p = document.getElementById('ppass').value;
    var used = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
    var ok = false;
    if (u === 'elsa') {
        if (p > 0 && p.length == 10) {
            ok = true;
            for (i = 1; i <= 10; i++) {
                var digit = p.charAt(i - 1);
                var part = p.substring(0, i);
                if (used[digit] != 0 || part % i != 0) {
                    ok = false
                }
                if (used[digit] == 0) {
                    used[digit] = 1
                }
            }
        }
    }
    if (ok) {
        document.location.href = 'challenge14_' + u + '_' + p + '.html'
    } else {
        alert('nope')
    }
}
// the solver for this is in solve.py
