var _0x549b=["value","puser","getElementById","ppass","rolo","length","charAt","href","location","challenge14_","_",".html","nope"];function checkEntries(){var u=document[_0x549b[2]](_0x549b[1])[_0x549b[0]];var p=document[_0x549b[2]](_0x549b[3])[_0x549b[0]];var ok=false;if(u===_0x549b[4]){if(p>0&&p[_0x549b[5]]==10){ok=true;for(i=0;i<=9;i++){var digit=p[_0x549b[6]](i);if(digit!=9-i){ok=false}}}};if(ok){document[_0x549b[8]][_0x549b[7]]=_0x549b[9]+u+_0x549b[10]+p+_0x549b[11]}else {alert(_0x549b[12])}};

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


     function checkEntries() {
    	  var u = document.getElementById('puser').value;
    	  var p = document.getElementById('ppass').value;
    	  if (u === 'yolo' && p === '1337') {
    		  document.location.href = 'challenge14_' + u + '_' + p + '.html';
    	  } else {
    		  alert('nope');
    	  }
      }
      
function checkEntries(){var u=document.getElementById('puser').value;var p=document.getElementById('ppass').value;var used=[0,0,0,0,0,0,0,0,0,0];var ok=false;if(u==='elsa'){if(p>0&&p.length==10){ok=true;for(i=1;i<=10;i++){var digit=p.charAt(i-1);var part=p.substring(0,i);if(used[digit]!=0||part%i!=0){ok=false}if(used[digit]==0){used[digit]=1}}}}if(ok){document.location.href='challenge14_'+u+'_'+p+'.html'}else{alert('nope')}}

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
